"""In-memory vector store implementation with profile support.

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
    >>> store.add(embedded_chunks, profile_id="my-profile")
    >>> results = store.search(query_vector, profile_id="my-profile", limit=10)
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

# Default profile for backwards compatibility
DEFAULT_PROFILE_ID = "_default"


class InMemoryVectorStore(BaseVectorStore):
    """In-memory vector store using NumPy for similarity search.

    Stores vectors in a NumPy matrix and uses dot product for
    cosine similarity (vectors are expected to be normalized).

    This implementation is simple and efficient for small to medium
    datasets (up to ~100k vectors). For larger datasets, consider
    using FAISS or another optimized backend.

    Profile Support:
        All operations accept an optional profile_id parameter.
        Data is stored in separate namespaces per profile.

    Attributes:
        config: The vector store configuration
        _profile_chunks: Dict mapping profile_id to {chunk_id: TextChunk}
        _profile_vectors: Dict mapping profile_id to {chunk_id: Vector}
        _model_id: The embedding model ID for cache invalidation
    """

    def __init__(self, config: VectorStoreConfig):
        """Initialize the in-memory store.

        Args:
            config: Vector store configuration (path is ignored)
        """
        super().__init__(config)
        # Store data per profile
        self._profile_chunks: dict[str, dict[str, TextChunk]] = {}
        self._profile_vectors: dict[str, dict[str, Vector]] = {}
        logger.info("Initialized in-memory vector store")

    def _get_profile_data(
        self, profile_id: str | None, create: bool = False
    ) -> tuple[dict[str, TextChunk], dict[str, Vector]] | tuple[None, None]:
        """Get chunks and vectors dicts for a profile.

        Args:
            profile_id: Profile ID (uses default if None)
            create: If True, create profile data structures if missing

        Returns:
            Tuple of (chunks_dict, vectors_dict) or (None, None) if not found
        """
        profile_id = profile_id or DEFAULT_PROFILE_ID

        if profile_id not in self._profile_chunks:
            if create:
                self._profile_chunks[profile_id] = {}
                self._profile_vectors[profile_id] = {}
            else:
                return None, None

        return self._profile_chunks[profile_id], self._profile_vectors[profile_id]

    def add(
        self,
        chunks: Sequence[EmbeddedChunk],
        profile_id: str | None = None,
    ) -> None:
        """Add embedded chunks to the store.

        Args:
            chunks: Sequence of embedded chunks to store
            profile_id: Profile namespace (uses default if None)
        """
        if not chunks:
            return

        chunks_dict, vectors_dict = self._get_profile_data(profile_id, create=True)

        for embedded_chunk in chunks:
            chunk_id = embedded_chunk.chunk.id
            chunks_dict[chunk_id] = embedded_chunk.chunk
            vectors_dict[chunk_id] = embedded_chunk.embedding

        profile_id = profile_id or DEFAULT_PROFILE_ID
        logger.debug(
            f"Added {len(chunks)} chunks to profile '{profile_id}' "
            f"(total: {len(chunks_dict)})"
        )

    def remove(
        self,
        chunk_ids: Sequence[str],
        profile_id: str | None = None,
    ) -> None:
        """Remove chunks by ID.

        Args:
            chunk_ids: Sequence of chunk IDs to remove
            profile_id: Profile namespace (uses default if None)
        """
        chunks_dict, vectors_dict = self._get_profile_data(profile_id)
        if chunks_dict is None:
            return

        for chunk_id in chunk_ids:
            chunks_dict.pop(chunk_id, None)
            vectors_dict.pop(chunk_id, None)

        logger.debug(f"Removed {len(chunk_ids)} chunks")

    def remove_book(
        self,
        book_id: BookIdentifier,
        profile_id: str | None = None,
    ) -> int:
        """Remove all chunks for a book from a profile.

        Args:
            book_id: The book whose chunks should be removed
            profile_id: Profile namespace (uses default if None)

        Returns:
            Number of chunks removed
        """
        chunks_dict, vectors_dict = self._get_profile_data(profile_id)
        if chunks_dict is None:
            return 0

        ids_to_remove = [
            chunk_id
            for chunk_id, chunk in chunks_dict.items()
            if chunk.book_id == book_id
        ]

        for chunk_id in ids_to_remove:
            del chunks_dict[chunk_id]
            del vectors_dict[chunk_id]

        logger.debug(f"Removed {len(ids_to_remove)} chunks for book {book_id}")
        return len(ids_to_remove)

    def search(
        self,
        query_embedding: Vector,
        limit: int = 10,
        profile_id: str | None = None,
        filter_book_ids: Sequence[BookIdentifier] | None = None,
        filter_libraries: Sequence[str] | None = None,
        min_score: float = 0.0,
    ) -> list[tuple[TextChunk, float]]:
        """Search for similar chunks using cosine similarity.

        Uses dot product for similarity since vectors are normalized.

        Args:
            query_embedding: The query vector to search for
            limit: Maximum number of results
            profile_id: Profile namespace to search (uses default if None)
            filter_book_ids: Optional filter to specific books
            filter_libraries: Optional filter to specific libraries
            min_score: Minimum similarity score threshold

        Returns:
            List of (chunk, score) tuples, ordered by descending score
        """
        chunks_dict, vectors_dict = self._get_profile_data(profile_id)
        if chunks_dict is None or not chunks_dict:
            return []

        # Apply filters to get candidate chunks
        candidates = self._get_filtered_candidates(
            chunks_dict, filter_book_ids, filter_libraries
        )

        if not candidates:
            return []

        # Build matrix of candidate vectors
        chunk_ids = list(candidates.keys())
        vectors = np.array([vectors_dict[cid] for cid in chunk_ids])

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
        chunks_dict: dict[str, TextChunk],
        filter_book_ids: Sequence[BookIdentifier] | None,
        filter_libraries: Sequence[str] | None,
    ) -> dict[str, TextChunk]:
        """Get chunks that match the filters.

        Args:
            chunks_dict: The chunks dictionary to filter
            filter_book_ids: Optional filter to specific books
            filter_libraries: Optional filter to specific libraries

        Returns:
            Dict mapping chunk ID to TextChunk for matching chunks
        """
        candidates = chunks_dict

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

    def get_indexed_books(
        self,
        profile_id: str | None = None,
    ) -> set[BookIdentifier]:
        """Get set of all indexed book identifiers in a profile.

        Args:
            profile_id: Profile namespace (uses default if None)

        Returns:
            Set of BookIdentifier for all indexed books
        """
        chunks_dict, _ = self._get_profile_data(profile_id)
        if chunks_dict is None:
            return set()
        return {chunk.book_id for chunk in chunks_dict.values()}

    def get_chunk_count(
        self,
        book_id: BookIdentifier | None = None,
        profile_id: str | None = None,
    ) -> int:
        """Get total chunk count in a profile.

        Args:
            book_id: Optional filter to count chunks for specific book
            profile_id: Profile namespace (uses default if None)

        Returns:
            Number of chunks in store
        """
        chunks_dict, _ = self._get_profile_data(profile_id)
        if chunks_dict is None:
            return 0

        if book_id is None:
            return len(chunks_dict)

        return sum(1 for chunk in chunks_dict.values() if chunk.book_id == book_id)

    def get_profiles(self) -> list[str]:
        """Get list of all profiles with data in the store.

        Returns:
            List of profile IDs
        """
        return list(self._profile_chunks.keys())

    def clear(self, profile_id: str | None = None) -> None:
        """Remove all data from the store or a specific profile.

        Args:
            profile_id: If provided, only clear that profile.
                       If None, clear entire store.
        """
        if profile_id is not None:
            # Clear specific profile
            self._profile_chunks.pop(profile_id, None)
            self._profile_vectors.pop(profile_id, None)
            logger.info(f"Cleared profile '{profile_id}' from in-memory store")
        else:
            # Clear entire store
            self._profile_chunks.clear()
            self._profile_vectors.clear()
            self._model_id = None
            logger.info("Cleared entire in-memory vector store")
