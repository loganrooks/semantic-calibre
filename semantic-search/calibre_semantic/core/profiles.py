"""Profile management for embedding configurations.

This module provides the ProfileManager class for managing embedding profiles
and tracking which books are indexed in which profiles.

Profiles are stored in a SQLite database alongside the vector store data.
Each profile has its own vector storage namespace to keep embeddings separate.

Usage:
    >>> from calibre_semantic.core.profiles import ProfileManager
    >>> manager = ProfileManager(db_path="./semantic_index.db")
    >>>
    >>> # Create a profile
    >>> profile = manager.create_profile(
    ...     name="Philosophy Research",
    ...     provider="google",
    ...     model="models/text-embedding-004",
    ...     dimension=768,
    ... )
    >>>
    >>> # Get all profiles
    >>> profiles = manager.list_profiles()
"""

from __future__ import annotations

import json
import logging
import sqlite3
import uuid
from datetime import datetime
from pathlib import Path
from typing import Sequence

from calibre_semantic.core.types import (
    BookIdentifier,
    BookIndexStatus,
    EmbeddingProfile,
    IndexStatus,
    IndexStrategy,
)

logger = logging.getLogger(__name__)


def generate_profile_id(name: str, provider: str, dimension: int) -> str:
    """Generate a unique profile ID from components.

    Args:
        name: Profile name
        provider: Embedding provider
        dimension: Embedding dimension

    Returns:
        A URL-safe unique identifier
    """
    # Create a slug from the name
    slug = name.lower().replace(" ", "-")[:20]
    # Add short uuid for uniqueness
    short_uuid = uuid.uuid4().hex[:8]
    return f"{slug}-{provider}-{dimension}d-{short_uuid}"


class ProfileManager:
    """Manages embedding profiles and book index status.

    This class provides CRUD operations for profiles and tracks
    which books are indexed in which profiles.

    Attributes:
        db_path: Path to the SQLite database

    Thread Safety:
        This class is NOT thread-safe. Use a separate instance per thread
        or implement external locking.
    """

    def __init__(self, db_path: Path | str | None = None):
        """Initialize the profile manager.

        Args:
            db_path: Path to SQLite database. If None, uses in-memory database.
        """
        if db_path is None:
            self._db_path = ":memory:"
        else:
            self._db_path = str(db_path)

        self._conn: sqlite3.Connection | None = None
        self._ensure_tables()

    def _get_connection(self) -> sqlite3.Connection:
        """Get or create database connection."""
        if self._conn is None:
            self._conn = sqlite3.connect(self._db_path)
            self._conn.row_factory = sqlite3.Row
        return self._conn

    def _ensure_tables(self) -> None:
        """Create tables if they don't exist."""
        conn = self._get_connection()
        cursor = conn.cursor()

        # Profiles table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS embedding_profiles (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                provider TEXT NOT NULL,
                model TEXT NOT NULL,
                dimension INTEGER NOT NULL,
                index_strategy TEXT NOT NULL DEFAULT 'flat',
                index_options TEXT,
                created_at TEXT NOT NULL,
                description TEXT
            )
        """)

        # Book index status table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS book_index_status (
                book_library_id TEXT NOT NULL,
                book_id INTEGER NOT NULL,
                book_format TEXT NOT NULL,
                profile_id TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'pending',
                indexed_at TEXT,
                chunk_count INTEGER DEFAULT 0,
                error_message TEXT,
                PRIMARY KEY (book_library_id, book_id, book_format, profile_id),
                FOREIGN KEY (profile_id) REFERENCES embedding_profiles(id)
                    ON DELETE CASCADE
            )
        """)

        # Index for fast lookups by profile
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_book_status_profile
            ON book_index_status(profile_id)
        """)

        conn.commit()

    def close(self) -> None:
        """Close the database connection."""
        if self._conn is not None:
            self._conn.close()
            self._conn = None

    # =========================================================================
    # Profile CRUD Operations
    # =========================================================================

    def create_profile(
        self,
        name: str,
        provider: str,
        model: str,
        dimension: int,
        index_strategy: IndexStrategy = IndexStrategy.FLAT,
        index_options: dict | None = None,
        description: str | None = None,
        profile_id: str | None = None,
    ) -> EmbeddingProfile:
        """Create a new embedding profile.

        Args:
            name: Human-readable name for the profile
            provider: Embedding provider (google, openai, sentence-transformers)
            model: Model identifier
            dimension: Embedding dimension
            index_strategy: Vector index strategy
            index_options: Strategy-specific options
            description: Optional description
            profile_id: Optional custom ID (auto-generated if not provided)

        Returns:
            The created EmbeddingProfile

        Raises:
            ValueError: If a profile with the same ID already exists
        """
        if profile_id is None:
            profile_id = generate_profile_id(name, provider, dimension)

        profile = EmbeddingProfile(
            id=profile_id,
            name=name,
            provider=provider,
            model=model,
            dimension=dimension,
            index_strategy=index_strategy,
            index_options=index_options or {},
            created_at=datetime.now(),
            description=description,
        )

        conn = self._get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO embedding_profiles
                (id, name, provider, model, dimension, index_strategy,
                 index_options, created_at, description)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    profile.id,
                    profile.name,
                    profile.provider,
                    profile.model,
                    profile.dimension,
                    profile.index_strategy.value,
                    json.dumps(profile.index_options),
                    profile.created_at.isoformat(),
                    profile.description,
                ),
            )
            conn.commit()
            logger.info(f"Created profile: {profile.id}")
            return profile
        except sqlite3.IntegrityError:
            raise ValueError(f"Profile with ID '{profile_id}' already exists")

    def get_profile(self, profile_id: str) -> EmbeddingProfile | None:
        """Get a profile by ID.

        Args:
            profile_id: The profile identifier

        Returns:
            EmbeddingProfile or None if not found
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM embedding_profiles WHERE id = ?",
            (profile_id,),
        )
        row = cursor.fetchone()

        if row is None:
            return None

        return self._row_to_profile(row)

    def list_profiles(self) -> list[EmbeddingProfile]:
        """List all profiles.

        Returns:
            List of all EmbeddingProfile instances
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM embedding_profiles ORDER BY created_at DESC")
        rows = cursor.fetchall()

        return [self._row_to_profile(row) for row in rows]

    def update_profile(
        self,
        profile_id: str,
        name: str | None = None,
        description: str | None = None,
        index_options: dict | None = None,
    ) -> EmbeddingProfile | None:
        """Update a profile's mutable fields.

        Note: provider, model, and dimension cannot be changed as this
        would invalidate existing embeddings.

        Args:
            profile_id: The profile to update
            name: New name (optional)
            description: New description (optional)
            index_options: New index options (optional)

        Returns:
            Updated EmbeddingProfile or None if not found
        """
        profile = self.get_profile(profile_id)
        if profile is None:
            return None

        conn = self._get_connection()
        cursor = conn.cursor()

        updates = []
        params = []

        if name is not None:
            updates.append("name = ?")
            params.append(name)
        if description is not None:
            updates.append("description = ?")
            params.append(description)
        if index_options is not None:
            updates.append("index_options = ?")
            params.append(json.dumps(index_options))

        if not updates:
            return profile

        params.append(profile_id)
        cursor.execute(
            f"UPDATE embedding_profiles SET {', '.join(updates)} WHERE id = ?",
            params,
        )
        conn.commit()

        return self.get_profile(profile_id)

    def delete_profile(self, profile_id: str) -> bool:
        """Delete a profile and all associated index data.

        Args:
            profile_id: The profile to delete

        Returns:
            True if profile was deleted, False if not found
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM embedding_profiles WHERE id = ?", (profile_id,))
        if cursor.fetchone() is None:
            return False

        # Delete profile (cascade will delete book_index_status entries)
        cursor.execute("DELETE FROM embedding_profiles WHERE id = ?", (profile_id,))
        conn.commit()

        logger.info(f"Deleted profile: {profile_id}")
        return True

    def _row_to_profile(self, row: sqlite3.Row) -> EmbeddingProfile:
        """Convert database row to EmbeddingProfile."""
        return EmbeddingProfile(
            id=row["id"],
            name=row["name"],
            provider=row["provider"],
            model=row["model"],
            dimension=row["dimension"],
            index_strategy=IndexStrategy(row["index_strategy"]),
            index_options=json.loads(row["index_options"] or "{}"),
            created_at=datetime.fromisoformat(row["created_at"]),
            description=row["description"],
        )

    # =========================================================================
    # Book Index Status Operations
    # =========================================================================

    def set_book_status(
        self,
        book_id: BookIdentifier,
        profile_id: str,
        status: IndexStatus,
        chunk_count: int = 0,
        error_message: str | None = None,
    ) -> BookIndexStatus:
        """Set or update the indexing status for a book in a profile.

        Args:
            book_id: The book identifier
            profile_id: The profile identifier
            status: New indexing status
            chunk_count: Number of chunks indexed
            error_message: Error message if status is FAILED

        Returns:
            Updated BookIndexStatus
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        indexed_at = datetime.now() if status == IndexStatus.COMPLETE else None

        cursor.execute(
            """
            INSERT INTO book_index_status
            (book_library_id, book_id, book_format, profile_id, status,
             indexed_at, chunk_count, error_message)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT (book_library_id, book_id, book_format, profile_id)
            DO UPDATE SET
                status = excluded.status,
                indexed_at = excluded.indexed_at,
                chunk_count = excluded.chunk_count,
                error_message = excluded.error_message
            """,
            (
                book_id.library_id,
                book_id.book_id,
                book_id.format,
                profile_id,
                status.value,
                indexed_at.isoformat() if indexed_at else None,
                chunk_count,
                error_message,
            ),
        )
        conn.commit()

        return BookIndexStatus(
            book_id=book_id,
            profile_id=profile_id,
            status=status,
            indexed_at=indexed_at,
            chunk_count=chunk_count,
            error_message=error_message,
        )

    def get_book_status(
        self,
        book_id: BookIdentifier,
        profile_id: str,
    ) -> BookIndexStatus | None:
        """Get the indexing status for a book in a profile.

        Args:
            book_id: The book identifier
            profile_id: The profile identifier

        Returns:
            BookIndexStatus or None if not found
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT * FROM book_index_status
            WHERE book_library_id = ? AND book_id = ? AND book_format = ?
                  AND profile_id = ?
            """,
            (book_id.library_id, book_id.book_id, book_id.format, profile_id),
        )
        row = cursor.fetchone()

        if row is None:
            return None

        return self._row_to_book_status(row)

    def get_books_in_profile(
        self,
        profile_id: str,
        status: IndexStatus | None = None,
    ) -> list[BookIndexStatus]:
        """Get all books indexed in a profile.

        Args:
            profile_id: The profile identifier
            status: Optional filter by status

        Returns:
            List of BookIndexStatus for books in the profile
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        if status is not None:
            cursor.execute(
                """
                SELECT * FROM book_index_status
                WHERE profile_id = ? AND status = ?
                ORDER BY indexed_at DESC
                """,
                (profile_id, status.value),
            )
        else:
            cursor.execute(
                """
                SELECT * FROM book_index_status
                WHERE profile_id = ?
                ORDER BY indexed_at DESC
                """,
                (profile_id,),
            )

        return [self._row_to_book_status(row) for row in cursor.fetchall()]

    def get_profiles_for_book(
        self,
        book_id: BookIdentifier,
    ) -> list[tuple[EmbeddingProfile, BookIndexStatus]]:
        """Get all profiles that contain a specific book.

        Args:
            book_id: The book identifier

        Returns:
            List of (profile, status) tuples
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT p.*, s.status, s.indexed_at, s.chunk_count, s.error_message
            FROM embedding_profiles p
            JOIN book_index_status s ON p.id = s.profile_id
            WHERE s.book_library_id = ? AND s.book_id = ? AND s.book_format = ?
            """,
            (book_id.library_id, book_id.book_id, book_id.format),
        )

        results = []
        for row in cursor.fetchall():
            profile = self._row_to_profile(row)
            status = BookIndexStatus(
                book_id=book_id,
                profile_id=profile.id,
                status=IndexStatus(row["status"]),
                indexed_at=datetime.fromisoformat(row["indexed_at"])
                if row["indexed_at"]
                else None,
                chunk_count=row["chunk_count"],
                error_message=row["error_message"],
            )
            results.append((profile, status))

        return results

    def remove_book_from_profile(
        self,
        book_id: BookIdentifier,
        profile_id: str,
    ) -> bool:
        """Remove a book's index status from a profile.

        Note: This only removes the status record. The actual vector
        data should be removed separately via the vector store.

        Args:
            book_id: The book identifier
            profile_id: The profile identifier

        Returns:
            True if removed, False if not found
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM book_index_status
            WHERE book_library_id = ? AND book_id = ? AND book_format = ?
                  AND profile_id = ?
            """,
            (book_id.library_id, book_id.book_id, book_id.format, profile_id),
        )
        conn.commit()

        return cursor.rowcount > 0

    def _row_to_book_status(self, row: sqlite3.Row) -> BookIndexStatus:
        """Convert database row to BookIndexStatus."""
        return BookIndexStatus(
            book_id=BookIdentifier(
                library_id=row["book_library_id"],
                book_id=row["book_id"],
                format=row["book_format"],
            ),
            profile_id=row["profile_id"],
            status=IndexStatus(row["status"]),
            indexed_at=datetime.fromisoformat(row["indexed_at"])
            if row["indexed_at"]
            else None,
            chunk_count=row["chunk_count"],
            error_message=row["error_message"],
        )

    # =========================================================================
    # Statistics
    # =========================================================================

    def get_profile_stats(self, profile_id: str) -> dict:
        """Get statistics for a profile.

        Args:
            profile_id: The profile identifier

        Returns:
            Dictionary with profile statistics
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                COUNT(*) as total_books,
                SUM(CASE WHEN status = 'complete' THEN 1 ELSE 0 END) as indexed_books,
                SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) as failed_books,
                SUM(chunk_count) as total_chunks
            FROM book_index_status
            WHERE profile_id = ?
            """,
            (profile_id,),
        )
        row = cursor.fetchone()

        return {
            "total_books": row["total_books"] or 0,
            "indexed_books": row["indexed_books"] or 0,
            "failed_books": row["failed_books"] or 0,
            "total_chunks": row["total_chunks"] or 0,
        }
