"""In-memory vector store implementation.

This store keeps all vectors in memory using NumPy arrays.
It's useful for:
- Testing without external dependencies
- Small datasets that fit in memory
- Single-book search in the viewer

For persistence and larger datasets, use SQLiteVecStore or ChromaDBStore.

Usage:
    >>> from calibre_semantic.providers.vectordb.memory import InMemoryVectorStore
    >>> from calibre_semantic.core.types import VectorStoreConfig
    >>> config = VectorStoreConfig(backend="memory")
    >>> store = InMemoryVectorStore(config)
    >>> store.add(embedded_chunks)
    >>> results = store.search(query_vector, limit=10)
"""

from __future__ import annotations

import logging
from typing import Sequence

import numpy as np

from calibre_semantic.core.types import (
    BookIdentifier,
    EmbeddedChunk,
    TextChunk,
    Vector,
    VectorStoreConfig,
)
from calibre_semantic.core.vectordb import BaseVectorStore

logger = logging.getLogger(__name__)


class InMemoryVectorStore(BaseVectorStore):
    """In-memory vector store using NumPy for similarity search.

    Stores vectors in a NumPy matrix and uses dot product for
    cosine similarity (vectors are expected to be normalized).

    This implementation is simple and efficient for small to medium
    datasets (up to ~100k vectors). For larger datasets, consider
    using FAISS or another optimized backend.

    Attributes:
        config: The vector store configuration
        _chunks: Dict mapping chunk ID to TextChunk
        _vectors: Dict mapping chunk ID to embedding vector
        _model_id: The embedding model ID for cache invalidation
    """

    def __init__(self, config: VectorStoreConfig):
        """Initialize the in-memory store.

        Args:
            config: Vector store configuration (path is ignored)
        """
        super().__init__(config)
        self._chunks: dict[str, TextChunk] = {}
        self._vectors: dict[str, Vector] = {}
        logger.info("Initialized in-memory vector store")

    def add(self, chunks: Sequence[EmbeddedChunk]) -> None:
        """Add embedded chunks to the store.

        Args:
            chunks: Sequence of embedded chunks to store
        """
        if not chunks:
            return

        for embedded_chunk in chunks:
            chunk_id = embedded_chunk.chunk.id
            self._chunks[chunk_id] = embedded_chunk.chunk
            self._vectors[chunk_id] = embedded_chunk.embedding

        logger.debug(f"Added {len(chunks)} chunks to store (total: {len(self._chunks)})")

    def remove(self, chunk_ids: Sequence[str]) -> None:
        """Remove chunks by ID.

        Args:
            chunk_ids: Sequence of chunk IDs to remove
        """
        for chunk_id in chunk_ids:
            self._chunks.pop(chunk_id, None)
            self._vectors.pop(chunk_id, None)

        logger.debug(f"Removed {len(chunk_ids)} chunks")

    def remove_book(self, book_id: BookIdentifier) -> int:
        """Remove all chunks for a book.

        Args:
            book_id: The book whose chunks should be removed

        Returns:
            Number of chunks removed
        """
        ids_to_remove = [
            chunk_id
            for chunk_id, chunk in self._chunks.items()
            if chunk.book_id == book_id
        ]

        for chunk_id in ids_to_remove:
            del self._chunks[chunk_id]
            del self._vectors[chunk_id]

        logger.debug(f"Removed {len(ids_to_remove)} chunks for book {book_id}")
        return len(ids_to_remove)

    def search(
        self,
        query_embedding: Vector,
        limit: int = 10,
        filter_book_ids: Sequence[BookIdentifier] | None = None,
        filter_libraries: Sequence[str] | None = None,
        min_score: float = 0.0,
    ) -> list[tuple[TextChunk, float]]:
        """Search for similar chunks using cosine similarity.

        Uses dot product for similarity since vectors are normalized.

        Args:
            query_embedding: The query vector to search for
            limit: Maximum number of results
            filter_book_ids: Optional filter to specific books
            filter_libraries: Optional filter to specific libraries
            min_score: Minimum similarity score threshold

        Returns:
            List of (chunk, score) tuples, ordered by descending score
        """
        if not self._chunks:
            return []

        # Apply filters to get candidate chunks
        candidates = self._get_filtered_candidates(filter_book_ids, filter_libraries)

        if not candidates:
            return []

        # Build matrix of candidate vectors
        chunk_ids = list(candidates.keys())
        vectors = np.array([self._vectors[cid] for cid in chunk_ids])

        # Compute cosine similarities (dot product since normalized)
        # query_embedding shape: (dim,)
        # vectors shape: (n_candidates, dim)
        similarities = np.dot(vectors, query_embedding)

        # Get top-k indices
        if min_score > 0:
            # Filter by minimum score first
            valid_indices = np.where(similarities >= min_score)[0]
            if len(valid_indices) == 0:
                return []
            similarities = similarities[valid_indices]
            chunk_ids = [chunk_ids[i] for i in valid_indices]

        # Sort by similarity (descending)
        top_k = min(limit, len(chunk_ids))
        top_indices = np.argsort(similarities)[-top_k:][::-1]

        # Build results
        results = []
        for idx in top_indices:
            chunk_id = chunk_ids[idx]
            score = float(similarities[idx])
            results.append((candidates[chunk_id], score))

        return results

    def _get_filtered_candidates(
        self,
        filter_book_ids: Sequence[BookIdentifier] | None,
        filter_libraries: Sequence[str] | None,
    ) -> dict[str, TextChunk]:
        """Get chunks that match the filters.

        Args:
            filter_book_ids: Optional filter to specific books
            filter_libraries: Optional filter to specific libraries

        Returns:
            Dict mapping chunk ID to TextChunk for matching chunks
        """
        candidates = self._chunks

        if filter_book_ids is not None:
            filter_set = set(filter_book_ids)
            candidates = {
                cid: chunk
                for cid, chunk in candidates.items()
                if chunk.book_id in filter_set
            }

        if filter_libraries is not None:
            filter_set = set(filter_libraries)
            candidates = {
                cid: chunk
                for cid, chunk in candidates.items()
                if chunk.book_id.library_id in filter_set
            }

        return candidates

    def get_indexed_books(self) -> set[BookIdentifier]:
        """Get set of all indexed book identifiers.

        Returns:
            Set of BookIdentifier for all indexed books
        """
        return {chunk.book_id for chunk in self._chunks.values()}

    def get_chunk_count(self, book_id: BookIdentifier | None = None) -> int:
        """Get total chunk count.

        Args:
            book_id: Optional filter to count chunks for specific book

        Returns:
            Number of chunks in store
        """
        if book_id is None:
            return len(self._chunks)

        return sum(1 for chunk in self._chunks.values() if chunk.book_id == book_id)

    def clear(self) -> None:
        """Remove all data from the store."""
        self._chunks.clear()
        self._vectors.clear()
        self._model_id = None
        logger.info("Cleared in-memory vector store")
