"""SQLite-vec vector store implementation.

This store uses SQLite with the sqlite-vec extension for persistent
vector storage and similarity search. It provides:
- ACID-compliant persistence
- Efficient vector similarity search
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
    >>> store.add(embedded_chunks)
    >>> results = store.search(query_vector, limit=10)
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

# SQL for creating the schema
_CREATE_SCHEMA = """
-- Metadata table for store configuration
CREATE TABLE IF NOT EXISTS store_metadata (
    key TEXT PRIMARY KEY,
    value TEXT
);

-- Chunks table for storing text chunk data
CREATE TABLE IF NOT EXISTS chunks (
    id TEXT PRIMARY KEY,
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
    metadata TEXT
);

-- Index for efficient book lookups
CREATE INDEX IF NOT EXISTS idx_chunks_book
ON chunks(book_library_id, book_id, book_format);

-- Index for library filtering
CREATE INDEX IF NOT EXISTS idx_chunks_library
ON chunks(book_library_id);
"""

# SQL for creating the vector table (done after loading sqlite-vec)
_CREATE_VECTOR_TABLE = """
CREATE VIRTUAL TABLE IF NOT EXISTS chunk_vectors USING vec0(
    id TEXT PRIMARY KEY,
    embedding FLOAT[{dimension}]
);
"""


class SQLiteVecStore(BaseVectorStore):
    """SQLite-vec based vector store for persistent storage.

    Uses sqlite-vec extension for efficient vector similarity search.
    Data is stored in a SQLite database file.

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

        # Create base schema
        self._conn.executescript(_CREATE_SCHEMA)

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

    def add(self, chunks: Sequence[EmbeddedChunk]) -> None:
        """Add embedded chunks to the store.

        Args:
            chunks: Sequence of embedded chunks to store
        """
        if not chunks:
            return

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

            chunk_rows.append((
                chunk.id,
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
            vector_rows.append((chunk.id, embedding_bytes))

        # Insert chunks
        self._conn.executemany(
            """
            INSERT OR REPLACE INTO chunks (
                id, book_library_id, book_id, book_format, text,
                spine_index, spine_name, start_offset, end_offset, cfi,
                chunk_type, chapter_title, section_title, metadata
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            chunk_rows,
        )

        # Insert vectors
        self._conn.executemany(
            "INSERT OR REPLACE INTO chunk_vectors (id, embedding) VALUES (?, ?)",
            vector_rows,
        )

        self._conn.commit()
        logger.debug(f"Added {len(chunks)} chunks to SQLite-vec store")

    def remove(self, chunk_ids: Sequence[str]) -> None:
        """Remove chunks by ID.

        Args:
            chunk_ids: Sequence of chunk IDs to remove
        """
        if not chunk_ids:
            return

        placeholders = ",".join("?" * len(chunk_ids))
        self._conn.execute(
            f"DELETE FROM chunks WHERE id IN ({placeholders})", list(chunk_ids)
        )
        self._conn.execute(
            f"DELETE FROM chunk_vectors WHERE id IN ({placeholders})", list(chunk_ids)
        )
        self._conn.commit()

    def remove_book(self, book_id: BookIdentifier) -> int:
        """Remove all chunks for a book.

        Args:
            book_id: The book whose chunks should be removed

        Returns:
            Number of chunks removed
        """
        # Get chunk IDs for this book
        cursor = self._conn.execute(
            """
            SELECT id FROM chunks
            WHERE book_library_id = ? AND book_id = ? AND book_format = ?
            """,
            (book_id.library_id, book_id.book_id, book_id.format),
        )
        chunk_ids = [row["id"] for row in cursor.fetchall()]

        if not chunk_ids:
            return 0

        self.remove(chunk_ids)
        return len(chunk_ids)

    def search(
        self,
        query_embedding: Vector,
        limit: int = 10,
        filter_book_ids: Sequence[BookIdentifier] | None = None,
        filter_libraries: Sequence[str] | None = None,
        min_score: float = 0.0,
    ) -> list[tuple[TextChunk, float]]:
        """Search for similar chunks using vector similarity.

        Uses sqlite-vec's vec_distance_cosine for similarity scoring.

        Args:
            query_embedding: The query vector to search for
            limit: Maximum number of results
            filter_book_ids: Optional filter to specific books
            filter_libraries: Optional filter to specific libraries
            min_score: Minimum similarity score threshold

        Returns:
            List of (chunk, score) tuples, ordered by descending score
        """
        if self._dimension is None:
            return []

        # Convert query to bytes
        query_bytes = query_embedding.astype(np.float32).tobytes()

        # Build query with filters
        # sqlite-vec returns distance, we convert to similarity (1 - distance/2 for cosine)
        sql = """
            SELECT
                c.*,
                1.0 - (vec_distance_cosine(v.embedding, ?) / 2.0) as similarity
            FROM chunk_vectors v
            JOIN chunks c ON c.id = v.id
            WHERE 1=1
        """
        params: list[Any] = [query_bytes]

        if filter_book_ids:
            book_conditions = []
            for book_id in filter_book_ids:
                book_conditions.append(
                    "(c.book_library_id = ? AND c.book_id = ? AND c.book_format = ?)"
                )
                params.extend([book_id.library_id, book_id.book_id, book_id.format])
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

    def get_indexed_books(self) -> set[BookIdentifier]:
        """Get set of all indexed book identifiers.

        Returns:
            Set of BookIdentifier for all indexed books
        """
        cursor = self._conn.execute(
            "SELECT DISTINCT book_library_id, book_id, book_format FROM chunks"
        )
        return {
            BookIdentifier(
                library_id=row["book_library_id"],
                book_id=row["book_id"],
                format=row["book_format"],
            )
            for row in cursor.fetchall()
        }

    def get_chunk_count(self, book_id: BookIdentifier | None = None) -> int:
        """Get total chunk count.

        Args:
            book_id: Optional filter to count chunks for specific book

        Returns:
            Number of chunks in store
        """
        if book_id is None:
            cursor = self._conn.execute("SELECT COUNT(*) as count FROM chunks")
        else:
            cursor = self._conn.execute(
                """
                SELECT COUNT(*) as count FROM chunks
                WHERE book_library_id = ? AND book_id = ? AND book_format = ?
                """,
                (book_id.library_id, book_id.book_id, book_id.format),
            )
        return cursor.fetchone()["count"]

    def get_model_id(self) -> str | None:
        """Get the model ID from store metadata."""
        return self._get_metadata("model_id")

    def set_model_id(self, model_id: str) -> None:
        """Set the model ID in store metadata."""
        self._model_id = model_id
        self._set_metadata("model_id", model_id)

    def clear(self) -> None:
        """Remove all data from the store."""
        self._conn.execute("DELETE FROM chunks")
        self._conn.execute("DELETE FROM chunk_vectors")
        self._conn.execute("DELETE FROM store_metadata")
        self._conn.commit()
        self._dimension = None
        self._model_id = None
        logger.info("Cleared SQLite-vec store")

    def close(self) -> None:
        """Close the database connection."""
        self._conn.close()

    def __del__(self):
        """Ensure connection is closed."""
        try:
            self._conn.close()
        except Exception:
            pass
