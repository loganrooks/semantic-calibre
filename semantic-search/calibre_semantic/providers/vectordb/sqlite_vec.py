"""SQLite-vec vector store implementation with profile support.

This store uses SQLite with the sqlite-vec extension for persistent
vector storage and similarity search. It provides:
- ACID-compliant persistence
- Efficient vector similarity search
- Profile-based namespace isolation
- Integration with Calibre's existing SQLite infrastructure

Installation:
    pip install calibre-semantic[sqlite-vec]

Usage:
    >>> from calibre_semantic.providers.vectordb.sqlite_vec import SQLiteVecStore
    >>> from calibre_semantic.core.types import VectorStoreConfig
    >>> from pathlib import Path
    >>> config = VectorStoreConfig(
    ...     backend="sqlite-vec",
    ...     path=Path("/path/to/store.db")
    ... )
    >>> store = SQLiteVecStore(config)
    >>> store.add(embedded_chunks, profile_id="my-profile")
    >>> results = store.search(query_vector, profile_id="my-profile", limit=10)
"""

from __future__ import annotations

import json
import logging
import sqlite3
from pathlib import Path
from typing import Any, Sequence

import numpy as np

from calibre_semantic.core.types import (
    BookIdentifier,
    ChunkLocation,
    ChunkType,
    EmbeddedChunk,
    TextChunk,
    Vector,
    VectorStoreConfig,
)
from calibre_semantic.core.vectordb import BaseVectorStore

logger = logging.getLogger(__name__)

# Default profile for backwards compatibility
DEFAULT_PROFILE_ID = "_default"

# SQL for creating the schema (v2 with profile support)
_CREATE_SCHEMA_V2 = """
-- Metadata table for store configuration
CREATE TABLE IF NOT EXISTS store_metadata (
    key TEXT PRIMARY KEY,
    value TEXT
);

-- Chunks table for storing text chunk data (v2 with profile_id)
CREATE TABLE IF NOT EXISTS chunks (
    id TEXT NOT NULL,
    profile_id TEXT NOT NULL,
    book_library_id TEXT NOT NULL,
    book_id INTEGER NOT NULL,
    book_format TEXT NOT NULL,
    text TEXT NOT NULL,
    spine_index INTEGER NOT NULL,
    spine_name TEXT NOT NULL,
    start_offset INTEGER NOT NULL,
    end_offset INTEGER NOT NULL,
    cfi TEXT,
    chunk_type TEXT NOT NULL,
    chapter_title TEXT,
    section_title TEXT,
    metadata TEXT,
    PRIMARY KEY (id, profile_id)
);

-- Index for efficient book lookups within profile
CREATE INDEX IF NOT EXISTS idx_chunks_profile_book
ON chunks(profile_id, book_library_id, book_id, book_format);

-- Index for profile filtering
CREATE INDEX IF NOT EXISTS idx_chunks_profile
ON chunks(profile_id);

-- Index for library filtering within profile
CREATE INDEX IF NOT EXISTS idx_chunks_profile_library
ON chunks(profile_id, book_library_id);
"""

# SQL for creating the vector table (done after loading sqlite-vec)
_CREATE_VECTOR_TABLE = """
CREATE VIRTUAL TABLE IF NOT EXISTS chunk_vectors USING vec0(
    id TEXT PRIMARY KEY,
    embedding FLOAT[{dimension}]
);
"""


def _migrate_to_v2(conn: sqlite3.Connection) -> None:
    """Migrate database from v1 (no profile) to v2 (with profile).

    Adds profile_id column to existing chunks table and assigns
    all existing data to the default profile.
    """
    cursor = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='chunks'"
    )
    if cursor.fetchone() is None:
        return  # No chunks table, nothing to migrate

    # Check if profile_id column exists
    cursor = conn.execute("PRAGMA table_info(chunks)")
    columns = [row[1] for row in cursor.fetchall()]

    if "profile_id" in columns:
        return  # Already migrated

    logger.info("Migrating SQLite-vec store to v2 (adding profile support)")

    # Create new table with profile_id
    conn.executescript("""
        -- Create new table with profile_id
        CREATE TABLE chunks_v2 (
            id TEXT NOT NULL,
            profile_id TEXT NOT NULL,
            book_library_id TEXT NOT NULL,
            book_id INTEGER NOT NULL,
            book_format TEXT NOT NULL,
            text TEXT NOT NULL,
            spine_index INTEGER NOT NULL,
            spine_name TEXT NOT NULL,
            start_offset INTEGER NOT NULL,
            end_offset INTEGER NOT NULL,
            cfi TEXT,
            chunk_type TEXT NOT NULL,
            chapter_title TEXT,
            section_title TEXT,
            metadata TEXT,
            PRIMARY KEY (id, profile_id)
        );

        -- Copy data with default profile
        INSERT INTO chunks_v2
        SELECT id, '_default', book_library_id, book_id, book_format,
               text, spine_index, spine_name, start_offset, end_offset,
               cfi, chunk_type, chapter_title, section_title, metadata
        FROM chunks;

        -- Drop old table and rename
        DROP TABLE chunks;
        ALTER TABLE chunks_v2 RENAME TO chunks;

        -- Recreate indexes
        CREATE INDEX IF NOT EXISTS idx_chunks_profile_book
        ON chunks(profile_id, book_library_id, book_id, book_format);

        CREATE INDEX IF NOT EXISTS idx_chunks_profile
        ON chunks(profile_id);

        CREATE INDEX IF NOT EXISTS idx_chunks_profile_library
        ON chunks(profile_id, book_library_id);
    """)
    conn.commit()
    logger.info("Migration to v2 complete")


class SQLiteVecStore(BaseVectorStore):
    """SQLite-vec based vector store with profile support.

    Uses sqlite-vec extension for efficient vector similarity search.
    Data is stored in a SQLite database file with profile-based isolation.

    Attributes:
        config: The vector store configuration
        _conn: SQLite connection
        _dimension: Vector dimension (detected from first insert)
    """

    def __init__(self, config: VectorStoreConfig):
        """Initialize the SQLite-vec store.

        Args:
            config: Vector store configuration with path to database file

        Raises:
            ImportError: If sqlite-vec is not installed
        """
        super().__init__(config)

        # Import and load sqlite-vec
        try:
            import sqlite_vec
        except ImportError as e:
            raise ImportError(
                "sqlite-vec is required for this backend. "
                "Install it with: pip install calibre-semantic[sqlite-vec]"
            ) from e

        # Determine database path
        if config.path is None:
            db_path = ":memory:"
        else:
            db_path = str(config.path)
            # Ensure parent directory exists
            Path(config.path).parent.mkdir(parents=True, exist_ok=True)

        # Connect and load extension
        self._conn = sqlite3.connect(db_path)
        self._conn.enable_load_extension(True)
        sqlite_vec.load(self._conn)
        self._conn.enable_load_extension(False)

        # Configure connection
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.execute("PRAGMA synchronous=NORMAL")

        # Migrate if needed (before creating new schema)
        _migrate_to_v2(self._conn)

        # Create base schema (v2)
        self._conn.executescript(_CREATE_SCHEMA_V2)

        # Load stored dimension and model ID
        self._dimension: int | None = self._get_metadata("dimension")
        if self._dimension is not None:
            self._dimension = int(self._dimension)
        stored_model_id = self._get_metadata("model_id")
        if stored_model_id is not None:
            self._model_id = stored_model_id

        # Create vector table if dimension is known
        if self._dimension is not None:
            self._ensure_vector_table()

        logger.info(f"Initialized SQLite-vec store at {db_path}")

    def _get_metadata(self, key: str) -> str | None:
        """Get a metadata value from the store."""
        cursor = self._conn.execute(
            "SELECT value FROM store_metadata WHERE key = ?", (key,)
        )
        row = cursor.fetchone()
        return row["value"] if row else None

    def _set_metadata(self, key: str, value: str) -> None:
        """Set a metadata value in the store."""
        self._conn.execute(
            "INSERT OR REPLACE INTO store_metadata (key, value) VALUES (?, ?)",
            (key, value),
        )
        self._conn.commit()

    def _ensure_vector_table(self) -> None:
        """Create the vector table if it doesn't exist."""
        if self._dimension is None:
            raise RuntimeError("Cannot create vector table without dimension")

        # Check if table exists
        cursor = self._conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='chunk_vectors'"
        )
        if cursor.fetchone() is None:
            self._conn.execute(
                _CREATE_VECTOR_TABLE.format(dimension=self._dimension)
            )
            self._conn.commit()

    def add(
        self,
        chunks: Sequence[EmbeddedChunk],
        profile_id: str | None = None,
    ) -> None:
        """Add embedded chunks to the store.

        Args:
            chunks: Sequence of embedded chunks to store
            profile_id: Profile to add chunks to (uses default if None)
        """
        if not chunks:
            return

        profile_id = profile_id or DEFAULT_PROFILE_ID

        # Initialize dimension from first chunk if needed
        if self._dimension is None:
            self._dimension = len(chunks[0].embedding)
            self._set_metadata("dimension", str(self._dimension))
            self._ensure_vector_table()

        # Prepare batch inserts
        chunk_rows = []
        vector_rows = []

        for embedded_chunk in chunks:
            chunk = embedded_chunk.chunk
            book_id = chunk.book_id

            # Create a unique vector ID that includes profile
            # This allows same chunk to exist in multiple profiles
            vector_id = f"{profile_id}:{chunk.id}"

            chunk_rows.append((
                chunk.id,
                profile_id,
                book_id.library_id,
                book_id.book_id,
                book_id.format,
                chunk.text,
                chunk.location.spine_index,
                chunk.location.spine_name,
                chunk.location.start_offset,
                chunk.location.end_offset,
                chunk.location.cfi,
                chunk.chunk_type.value,
                chunk.chapter_title,
                chunk.section_title,
                json.dumps(chunk.metadata) if chunk.metadata else None,
            ))

            # Convert embedding to bytes for sqlite-vec
            embedding_bytes = embedded_chunk.embedding.astype(np.float32).tobytes()
            vector_rows.append((vector_id, embedding_bytes))

        # Insert chunks
        self._conn.executemany(
            """
            INSERT OR REPLACE INTO chunks (
                id, profile_id, book_library_id, book_id, book_format, text,
                spine_index, spine_name, start_offset, end_offset, cfi,
                chunk_type, chapter_title, section_title, metadata
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            chunk_rows,
        )

        # Insert vectors
        self._conn.executemany(
            "INSERT OR REPLACE INTO chunk_vectors (id, embedding) VALUES (?, ?)",
            vector_rows,
        )

        self._conn.commit()
        logger.debug(f"Added {len(chunks)} chunks to profile '{profile_id}'")

    def remove(
        self,
        chunk_ids: Sequence[str],
        profile_id: str | None = None,
    ) -> None:
        """Remove chunks by ID.

        Args:
            chunk_ids: Sequence of chunk IDs to remove
            profile_id: Profile to remove from (uses default if None)
        """
        if not chunk_ids:
            return

        profile_id = profile_id or DEFAULT_PROFILE_ID

        placeholders = ",".join("?" * len(chunk_ids))

        # Remove from chunks table (profile-specific)
        self._conn.execute(
            f"DELETE FROM chunks WHERE profile_id = ? AND id IN ({placeholders})",
            [profile_id] + list(chunk_ids),
        )

        # Remove from vectors (using profile-prefixed IDs)
        vector_ids = [f"{profile_id}:{cid}" for cid in chunk_ids]
        vector_placeholders = ",".join("?" * len(vector_ids))
        self._conn.execute(
            f"DELETE FROM chunk_vectors WHERE id IN ({vector_placeholders})",
            vector_ids,
        )

        self._conn.commit()

    def remove_book(
        self,
        book_id: BookIdentifier,
        profile_id: str | None = None,
    ) -> int:
        """Remove all chunks for a book from a profile.

        Args:
            book_id: The book whose chunks should be removed
            profile_id: Profile to remove from (uses default if None)

        Returns:
            Number of chunks removed
        """
        profile_id = profile_id or DEFAULT_PROFILE_ID

        # Get chunk IDs for this book in this profile
        cursor = self._conn.execute(
            """
            SELECT id FROM chunks
            WHERE profile_id = ?
              AND book_library_id = ? AND book_id = ? AND book_format = ?
            """,
            (profile_id, book_id.library_id, book_id.book_id, book_id.format),
        )
        chunk_ids = [row["id"] for row in cursor.fetchall()]

        if not chunk_ids:
            return 0

        self.remove(chunk_ids, profile_id)
        return len(chunk_ids)

    def search(
        self,
        query_embedding: Vector,
        limit: int = 10,
        profile_id: str | None = None,
        filter_book_ids: Sequence[BookIdentifier] | None = None,
        filter_libraries: Sequence[str] | None = None,
        min_score: float = 0.0,
    ) -> list[tuple[TextChunk, float]]:
        """Search for similar chunks using vector similarity.

        Uses sqlite-vec's vec_distance_cosine for similarity scoring.

        Args:
            query_embedding: The query vector to search for
            limit: Maximum number of results
            profile_id: Profile to search in (uses default if None)
            filter_book_ids: Optional filter to specific books
            filter_libraries: Optional filter to specific libraries
            min_score: Minimum similarity score threshold

        Returns:
            List of (chunk, score) tuples, ordered by descending score
        """
        if self._dimension is None:
            return []

        profile_id = profile_id or DEFAULT_PROFILE_ID

        # Convert query to bytes
        query_bytes = query_embedding.astype(np.float32).tobytes()

        # Build query with filters
        # sqlite-vec returns distance, we convert to similarity (1 - distance/2 for cosine)
        # Vector IDs are prefixed with profile_id
        sql = """
            SELECT
                c.*,
                1.0 - (vec_distance_cosine(v.embedding, ?) / 2.0) as similarity
            FROM chunk_vectors v
            JOIN chunks c ON c.id = substr(v.id, length(c.profile_id) + 2)
                         AND c.profile_id = ?
            WHERE c.profile_id = ?
        """
        params: list[Any] = [query_bytes, profile_id, profile_id]

        if filter_book_ids:
            book_conditions = []
            for bid in filter_book_ids:
                book_conditions.append(
                    "(c.book_library_id = ? AND c.book_id = ? AND c.book_format = ?)"
                )
                params.extend([bid.library_id, bid.book_id, bid.format])
            sql += f" AND ({' OR '.join(book_conditions)})"

        if filter_libraries:
            placeholders = ",".join("?" * len(filter_libraries))
            sql += f" AND c.book_library_id IN ({placeholders})"
            params.extend(filter_libraries)

        if min_score > 0:
            # Convert min_score to max_distance
            max_distance = 2.0 * (1.0 - min_score)
            sql += " AND vec_distance_cosine(v.embedding, ?) <= ?"
            params.extend([query_bytes, max_distance])

        sql += " ORDER BY similarity DESC LIMIT ?"
        params.append(limit)

        cursor = self._conn.execute(sql, params)
        rows = cursor.fetchall()

        results = []
        for row in rows:
            chunk = self._row_to_chunk(row)
            score = float(row["similarity"])
            results.append((chunk, score))

        return results

    def _row_to_chunk(self, row: sqlite3.Row) -> TextChunk:
        """Convert a database row to a TextChunk."""
        return TextChunk(
            id=row["id"],
            book_id=BookIdentifier(
                library_id=row["book_library_id"],
                book_id=row["book_id"],
                format=row["book_format"],
            ),
            text=row["text"],
            location=ChunkLocation(
                spine_index=row["spine_index"],
                spine_name=row["spine_name"],
                start_offset=row["start_offset"],
                end_offset=row["end_offset"],
                cfi=row["cfi"],
            ),
            chunk_type=ChunkType(row["chunk_type"]),
            chapter_title=row["chapter_title"],
            section_title=row["section_title"],
            metadata=json.loads(row["metadata"]) if row["metadata"] else {},
        )

    def get_indexed_books(
        self,
        profile_id: str | None = None,
    ) -> set[BookIdentifier]:
        """Get set of all indexed book identifiers in a profile.

        Args:
            profile_id: Profile to query (uses default if None)

        Returns:
            Set of BookIdentifier for all indexed books
        """
        profile_id = profile_id or DEFAULT_PROFILE_ID

        cursor = self._conn.execute(
            """
            SELECT DISTINCT book_library_id, book_id, book_format
            FROM chunks
            WHERE profile_id = ?
            """,
            (profile_id,),
        )
        return {
            BookIdentifier(
                library_id=row["book_library_id"],
                book_id=row["book_id"],
                format=row["book_format"],
            )
            for row in cursor.fetchall()
        }

    def get_chunk_count(
        self,
        book_id: BookIdentifier | None = None,
        profile_id: str | None = None,
    ) -> int:
        """Get total chunk count.

        Args:
            book_id: Optional filter to count chunks for specific book
            profile_id: Profile to query (uses default if None)

        Returns:
            Number of chunks in store
        """
        profile_id = profile_id or DEFAULT_PROFILE_ID

        if book_id is None:
            cursor = self._conn.execute(
                "SELECT COUNT(*) as count FROM chunks WHERE profile_id = ?",
                (profile_id,),
            )
        else:
            cursor = self._conn.execute(
                """
                SELECT COUNT(*) as count FROM chunks
                WHERE profile_id = ?
                  AND book_library_id = ? AND book_id = ? AND book_format = ?
                """,
                (profile_id, book_id.library_id, book_id.book_id, book_id.format),
            )
        return cursor.fetchone()["count"]

    def get_profiles(self) -> list[str]:
        """Get list of all profiles with data in the store.

        Returns:
            List of profile IDs
        """
        cursor = self._conn.execute(
            "SELECT DISTINCT profile_id FROM chunks ORDER BY profile_id"
        )
        return [row["profile_id"] for row in cursor.fetchall()]

    def get_model_id(self) -> str | None:
        """Get the model ID from store metadata."""
        return self._get_metadata("model_id")

    def set_model_id(self, model_id: str) -> None:
        """Set the model ID in store metadata."""
        self._model_id = model_id
        self._set_metadata("model_id", model_id)

    def clear(self, profile_id: str | None = None) -> None:
        """Remove all data from the store or a specific profile.

        Args:
            profile_id: If provided, only clear that profile.
                       If None, clear entire store.
        """
        if profile_id is not None:
            # Clear specific profile
            cursor = self._conn.execute(
                "SELECT id FROM chunks WHERE profile_id = ?", (profile_id,)
            )
            chunk_ids = [row["id"] for row in cursor.fetchall()]
            vector_ids = [f"{profile_id}:{cid}" for cid in chunk_ids]

            if vector_ids:
                placeholders = ",".join("?" * len(vector_ids))
                self._conn.execute(
                    f"DELETE FROM chunk_vectors WHERE id IN ({placeholders})",
                    vector_ids,
                )

            self._conn.execute(
                "DELETE FROM chunks WHERE profile_id = ?", (profile_id,)
            )
            self._conn.commit()
            logger.info(f"Cleared profile '{profile_id}' from SQLite-vec store")
        else:
            # Clear entire store
            self._conn.execute("DELETE FROM chunks")
            self._conn.execute("DELETE FROM chunk_vectors")
            self._conn.execute("DELETE FROM store_metadata")
            self._conn.commit()
            self._dimension = None
            self._model_id = None
            logger.info("Cleared entire SQLite-vec store")

    def close(self) -> None:
        """Close the database connection."""
        self._conn.close()

    def __del__(self):
        """Ensure connection is closed."""
        try:
            self._conn.close()
        except Exception:
            pass
