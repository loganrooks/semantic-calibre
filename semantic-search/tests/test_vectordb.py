"""Tests for vector store implementations.

This module tests:
1. The VectorStore protocol contract
2. InMemoryVectorStore implementation (for testing)
3. SQLiteVecStore implementation

Tests validate:
- Interface compliance
- Add/remove operations
- Search functionality with filtering
- Index management
- Model ID tracking for cache invalidation
"""

from __future__ import annotations

import numpy as np
import pytest
from typing import TYPE_CHECKING

from calibre_semantic.core.types import (
    BookIdentifier,
    ChunkLocation,
    ChunkType,
    EmbeddedChunk,
    TextChunk,
    Vector,
    VectorStore,
    VectorStoreConfig,
)

if TYPE_CHECKING:
    from conftest import MockEmbeddingProvider


# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def vector_store_config() -> VectorStoreConfig:
    """Default vector store configuration for testing."""
    return VectorStoreConfig(
        backend="memory",
        path=None,  # In-memory
    )


@pytest.fixture
def sample_book_ids() -> list[BookIdentifier]:
    """Create sample book identifiers for testing."""
    return [
        BookIdentifier("lib-1", 1, "EPUB"),
        BookIdentifier("lib-1", 2, "EPUB"),
        BookIdentifier("lib-2", 1, "PDF"),
    ]


@pytest.fixture
def sample_chunks(sample_book_ids: list[BookIdentifier]) -> list[TextChunk]:
    """Create sample text chunks for testing."""
    chunks = []
    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Machine learning transforms data into insights.",
        "Philosophy explores fundamental questions about existence.",
        "The cat sat on the mat quietly.",
        "Artificial intelligence is reshaping industries.",
    ]

    for i, text in enumerate(texts):
        book_id = sample_book_ids[i % len(sample_book_ids)]
        chunk = TextChunk(
            id=f"chunk-{i:03d}",
            book_id=book_id,
            text=text,
            location=ChunkLocation(
                spine_index=0,
                spine_name="chapter1.xhtml",
                start_offset=i * 100,
                end_offset=(i + 1) * 100,
            ),
            chunk_type=ChunkType.PARAGRAPH,
            chapter_title=f"Chapter {i + 1}",
        )
        chunks.append(chunk)

    return chunks


@pytest.fixture
def sample_embedded_chunks(
    sample_chunks: list[TextChunk],
    mock_embedding_provider: "MockEmbeddingProvider",
) -> list[EmbeddedChunk]:
    """Create sample embedded chunks for testing."""
    texts = [c.text for c in sample_chunks]
    embeddings = mock_embedding_provider.embed(texts)

    return [
        EmbeddedChunk(
            chunk=chunk,
            embedding=embedding,
            model_id=mock_embedding_provider.model_id,
        )
        for chunk, embedding in zip(sample_chunks, embeddings)
    ]


@pytest.fixture
def memory_store() -> "InMemoryVectorStore":
    """Create an in-memory vector store for testing."""
    from calibre_semantic.providers.vectordb.memory import InMemoryVectorStore

    config = VectorStoreConfig(backend="memory", path=None)
    return InMemoryVectorStore(config)


# =============================================================================
# Protocol Tests
# =============================================================================


class TestVectorStoreProtocol:
    """Test that stores implement the VectorStore protocol correctly."""

    def test_memory_store_implements_protocol(self, memory_store) -> None:
        """InMemoryVectorStore should implement VectorStore protocol."""
        assert isinstance(memory_store, VectorStore)

    def test_protocol_requires_add_method(self, memory_store) -> None:
        """Store must have add method."""
        assert hasattr(memory_store, "add")
        assert callable(memory_store.add)

    def test_protocol_requires_remove_method(self, memory_store) -> None:
        """Store must have remove method."""
        assert hasattr(memory_store, "remove")
        assert callable(memory_store.remove)

    def test_protocol_requires_remove_book_method(self, memory_store) -> None:
        """Store must have remove_book method."""
        assert hasattr(memory_store, "remove_book")
        assert callable(memory_store.remove_book)

    def test_protocol_requires_search_method(self, memory_store) -> None:
        """Store must have search method."""
        assert hasattr(memory_store, "search")
        assert callable(memory_store.search)

    def test_protocol_requires_get_indexed_books_method(self, memory_store) -> None:
        """Store must have get_indexed_books method."""
        assert hasattr(memory_store, "get_indexed_books")
        assert callable(memory_store.get_indexed_books)

    def test_protocol_requires_get_chunk_count_method(self, memory_store) -> None:
        """Store must have get_chunk_count method."""
        assert hasattr(memory_store, "get_chunk_count")
        assert callable(memory_store.get_chunk_count)

    def test_protocol_requires_model_id_methods(self, memory_store) -> None:
        """Store must have get_model_id and set_model_id methods."""
        assert hasattr(memory_store, "get_model_id")
        assert hasattr(memory_store, "set_model_id")

    def test_protocol_requires_clear_method(self, memory_store) -> None:
        """Store must have clear method."""
        assert hasattr(memory_store, "clear")
        assert callable(memory_store.clear)


# =============================================================================
# InMemoryVectorStore Tests
# =============================================================================


class TestInMemoryVectorStore:
    """Tests for InMemoryVectorStore implementation."""

    def test_add_chunks(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
    ) -> None:
        """Should add embedded chunks to the store."""
        memory_store.add(sample_embedded_chunks)
        assert memory_store.get_chunk_count() == len(sample_embedded_chunks)

    def test_add_empty_list(self, memory_store) -> None:
        """Adding empty list should be no-op."""
        memory_store.add([])
        assert memory_store.get_chunk_count() == 0

    def test_get_chunk_count_empty(self, memory_store) -> None:
        """Empty store should have zero chunks."""
        assert memory_store.get_chunk_count() == 0

    def test_get_chunk_count_filtered(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
        sample_book_ids: list[BookIdentifier],
    ) -> None:
        """Should count chunks for specific book."""
        memory_store.add(sample_embedded_chunks)

        # Count for first book
        count = memory_store.get_chunk_count(sample_book_ids[0])
        # At least one chunk should be from this book
        assert count >= 1
        assert count < len(sample_embedded_chunks)

    def test_get_indexed_books(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
    ) -> None:
        """Should return set of indexed book identifiers."""
        memory_store.add(sample_embedded_chunks)

        indexed = memory_store.get_indexed_books()
        assert isinstance(indexed, set)
        assert len(indexed) > 0

        # All book IDs from chunks should be in indexed set
        for chunk in sample_embedded_chunks:
            assert chunk.chunk.book_id in indexed

    def test_get_indexed_books_empty(self, memory_store) -> None:
        """Empty store should return empty set."""
        indexed = memory_store.get_indexed_books()
        assert indexed == set()

    def test_remove_chunks_by_id(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
    ) -> None:
        """Should remove specific chunks by ID."""
        memory_store.add(sample_embedded_chunks)
        initial_count = memory_store.get_chunk_count()

        # Remove first two chunks
        ids_to_remove = [sample_embedded_chunks[0].chunk.id, sample_embedded_chunks[1].chunk.id]
        memory_store.remove(ids_to_remove)

        assert memory_store.get_chunk_count() == initial_count - 2

    def test_remove_nonexistent_chunk(self, memory_store) -> None:
        """Removing nonexistent chunk should not raise."""
        memory_store.remove(["nonexistent-id"])
        assert memory_store.get_chunk_count() == 0

    def test_remove_book(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
        sample_book_ids: list[BookIdentifier],
    ) -> None:
        """Should remove all chunks for a book."""
        memory_store.add(sample_embedded_chunks)

        book_to_remove = sample_book_ids[0]
        chunks_for_book = sum(
            1 for c in sample_embedded_chunks if c.chunk.book_id == book_to_remove
        )

        removed = memory_store.remove_book(book_to_remove)
        assert removed == chunks_for_book
        assert book_to_remove not in memory_store.get_indexed_books()

    def test_remove_book_not_in_store(
        self,
        memory_store,
    ) -> None:
        """Removing book not in store should return 0."""
        book_id = BookIdentifier("nonexistent", 999, "EPUB")
        removed = memory_store.remove_book(book_id)
        assert removed == 0

    def test_clear(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
    ) -> None:
        """Clear should remove all data."""
        memory_store.add(sample_embedded_chunks)
        memory_store.set_model_id("test-model")

        memory_store.clear()

        assert memory_store.get_chunk_count() == 0
        assert memory_store.get_indexed_books() == set()
        assert memory_store.get_model_id() is None

    def test_model_id_tracking(self, memory_store) -> None:
        """Should track model ID for cache invalidation."""
        assert memory_store.get_model_id() is None

        memory_store.set_model_id("model-v1")
        assert memory_store.get_model_id() == "model-v1"

        memory_store.set_model_id("model-v2")
        assert memory_store.get_model_id() == "model-v2"


# =============================================================================
# Search Tests
# =============================================================================


class TestVectorStoreSearch:
    """Tests for vector store search functionality."""

    def test_search_returns_results(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
        mock_embedding_provider: "MockEmbeddingProvider",
    ) -> None:
        """Search should return results sorted by score."""
        memory_store.add(sample_embedded_chunks)

        # Use embedding of first chunk as query
        query_embedding = sample_embedded_chunks[0].embedding

        results = memory_store.search(query_embedding, limit=3)

        assert len(results) == 3
        # Results should be (chunk, score) tuples
        for chunk, score in results:
            assert isinstance(chunk, TextChunk)
            assert isinstance(score, float)
            # Allow small floating point tolerance (cosine similarity can slightly exceed 1.0)
            assert 0.0 <= score <= 1.0 + 1e-6

    def test_search_scores_descending(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
    ) -> None:
        """Search results should be sorted by descending score."""
        memory_store.add(sample_embedded_chunks)

        query_embedding = sample_embedded_chunks[0].embedding
        results = memory_store.search(query_embedding, limit=5)

        scores = [score for _, score in results]
        assert scores == sorted(scores, reverse=True)

    def test_search_limit(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
    ) -> None:
        """Search should respect limit parameter."""
        memory_store.add(sample_embedded_chunks)

        query_embedding = sample_embedded_chunks[0].embedding

        results_2 = memory_store.search(query_embedding, limit=2)
        results_10 = memory_store.search(query_embedding, limit=10)

        assert len(results_2) == 2
        assert len(results_10) == min(10, len(sample_embedded_chunks))

    def test_search_min_score_filter(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
    ) -> None:
        """Search should filter by minimum score."""
        memory_store.add(sample_embedded_chunks)

        query_embedding = sample_embedded_chunks[0].embedding

        # Very high threshold should return fewer results
        results_high = memory_store.search(query_embedding, limit=10, min_score=0.99)
        results_low = memory_store.search(query_embedding, limit=10, min_score=0.0)

        # All results should meet minimum score
        for _, score in results_high:
            assert score >= 0.99

        assert len(results_low) >= len(results_high)

    def test_search_filter_by_book_ids(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
        sample_book_ids: list[BookIdentifier],
    ) -> None:
        """Search should filter by book IDs."""
        memory_store.add(sample_embedded_chunks)

        query_embedding = sample_embedded_chunks[0].embedding
        filter_books = [sample_book_ids[0]]

        results = memory_store.search(
            query_embedding,
            limit=10,
            filter_book_ids=filter_books,
        )

        # All results should be from filtered books
        for chunk, _ in results:
            assert chunk.book_id in filter_books

    def test_search_filter_by_library(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
    ) -> None:
        """Search should filter by library IDs."""
        memory_store.add(sample_embedded_chunks)

        query_embedding = sample_embedded_chunks[0].embedding
        filter_libs = ["lib-1"]

        results = memory_store.search(
            query_embedding,
            limit=10,
            filter_libraries=filter_libs,
        )

        # All results should be from filtered libraries
        for chunk, _ in results:
            assert chunk.book_id.library_id in filter_libs

    def test_search_empty_store(self, memory_store) -> None:
        """Searching empty store should return empty list."""
        query = np.random.rand(384).astype(np.float32)
        results = memory_store.search(query, limit=10)
        assert results == []

    def test_search_exact_match_highest_score(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
    ) -> None:
        """Exact embedding match should have highest score."""
        memory_store.add(sample_embedded_chunks)

        # Query with exact embedding from first chunk
        target_chunk = sample_embedded_chunks[0]
        query_embedding = target_chunk.embedding

        results = memory_store.search(query_embedding, limit=1)

        assert len(results) == 1
        result_chunk, score = results[0]
        assert result_chunk.id == target_chunk.chunk.id
        assert score > 0.99  # Should be very close to 1.0


# =============================================================================
# SQLiteVecStore Tests
# =============================================================================


class TestSQLiteVecStore:
    """Tests for SQLiteVecStore implementation.

    These tests require sqlite-vec to be installed.
    They are skipped if the dependency is not available.
    """

    @pytest.fixture
    def sqlite_vec_store(self, tmp_path):
        """Create a SQLiteVecStore for testing."""
        try:
            import sqlite_vec  # noqa: F401
        except ImportError:
            pytest.skip("sqlite-vec not installed")

        from calibre_semantic.providers.vectordb.sqlite_vec import SQLiteVecStore

        config = VectorStoreConfig(
            backend="sqlite-vec",
            path=tmp_path / "test.db",
        )
        return SQLiteVecStore(config)

    def test_implements_protocol(self, sqlite_vec_store) -> None:
        """SQLiteVecStore should implement VectorStore protocol."""
        assert isinstance(sqlite_vec_store, VectorStore)

    def test_add_and_search(
        self,
        sqlite_vec_store,
        sample_embedded_chunks: list[EmbeddedChunk],
    ) -> None:
        """Should add chunks and search them."""
        sqlite_vec_store.add(sample_embedded_chunks)

        query = sample_embedded_chunks[0].embedding
        results = sqlite_vec_store.search(query, limit=3)

        assert len(results) == 3
        # First result should be exact match
        assert results[0][0].id == sample_embedded_chunks[0].chunk.id

    def test_persistence(
        self,
        tmp_path,
        sample_embedded_chunks: list[EmbeddedChunk],
    ) -> None:
        """Data should persist across store instances."""
        try:
            import sqlite_vec  # noqa: F401
        except ImportError:
            pytest.skip("sqlite-vec not installed")

        from calibre_semantic.providers.vectordb.sqlite_vec import SQLiteVecStore

        db_path = tmp_path / "persist_test.db"
        config = VectorStoreConfig(backend="sqlite-vec", path=db_path)

        # Add data
        store1 = SQLiteVecStore(config)
        store1.add(sample_embedded_chunks)
        store1.set_model_id("test-model")
        count1 = store1.get_chunk_count()

        # Create new instance with same path
        store2 = SQLiteVecStore(config)
        assert store2.get_chunk_count() == count1
        assert store2.get_model_id() == "test-model"


# =============================================================================
# Factory Tests
# =============================================================================


class TestVectorStoreFactory:
    """Tests for the vector store factory function."""

    def test_create_memory_store(self) -> None:
        """Factory should create InMemoryVectorStore for memory backend."""
        from calibre_semantic.core.vectordb import create_vector_store

        config = VectorStoreConfig(backend="memory")
        store = create_vector_store(config)

        assert isinstance(store, VectorStore)

    def test_create_sqlite_vec_store(self, tmp_path) -> None:
        """Factory should create SQLiteVecStore for sqlite-vec backend."""
        try:
            import sqlite_vec  # noqa: F401
        except ImportError:
            pytest.skip("sqlite-vec not installed")

        from calibre_semantic.core.vectordb import create_vector_store

        config = VectorStoreConfig(
            backend="sqlite-vec",
            path=tmp_path / "factory_test.db",
        )
        store = create_vector_store(config)

        assert isinstance(store, VectorStore)

    def test_create_unknown_backend_raises(self) -> None:
        """Factory should raise ValueError for unknown backend."""
        from calibre_semantic.core.vectordb import create_vector_store

        config = VectorStoreConfig(backend="unknown-backend")

        with pytest.raises(ValueError, match="Unknown vector store backend"):
            create_vector_store(config)


# =============================================================================
# Profile Support Tests
# =============================================================================


class TestVectorStoreProfileSupport:
    """Tests for profile-based namespace isolation in vector stores."""

    def test_add_to_different_profiles(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
    ) -> None:
        """Chunks added to different profiles should be isolated."""
        # Split chunks between two profiles
        profile_a_chunks = sample_embedded_chunks[:2]
        profile_b_chunks = sample_embedded_chunks[2:]

        memory_store.add(profile_a_chunks, profile_id="profile-a")
        memory_store.add(profile_b_chunks, profile_id="profile-b")

        # Each profile should only contain its own chunks
        assert memory_store.get_chunk_count(profile_id="profile-a") == len(profile_a_chunks)
        assert memory_store.get_chunk_count(profile_id="profile-b") == len(profile_b_chunks)

    def test_search_isolated_by_profile(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
    ) -> None:
        """Search should only return results from the specified profile."""
        # Add same chunks to different profiles
        memory_store.add(sample_embedded_chunks[:2], profile_id="profile-a")
        memory_store.add(sample_embedded_chunks[2:], profile_id="profile-b")

        query = sample_embedded_chunks[0].embedding

        # Search in profile-a should only find chunks from profile-a
        results_a = memory_store.search(query, limit=10, profile_id="profile-a")
        for chunk, _ in results_a:
            assert chunk.id in [c.chunk.id for c in sample_embedded_chunks[:2]]

    def test_remove_book_isolated_by_profile(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
    ) -> None:
        """Removing a book should only affect the specified profile."""
        book_id = sample_embedded_chunks[0].chunk.book_id

        # Add same chunk to both profiles
        memory_store.add([sample_embedded_chunks[0]], profile_id="profile-a")
        memory_store.add([sample_embedded_chunks[0]], profile_id="profile-b")

        # Remove from profile-a only
        memory_store.remove_book(book_id, profile_id="profile-a")

        # Profile-a should be empty, profile-b should still have the chunk
        assert memory_store.get_chunk_count(profile_id="profile-a") == 0
        assert memory_store.get_chunk_count(profile_id="profile-b") == 1

    def test_get_indexed_books_isolated_by_profile(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
        sample_book_ids: list[BookIdentifier],
    ) -> None:
        """get_indexed_books should only return books from specified profile."""
        # Add different books to different profiles
        book_a_chunks = [c for c in sample_embedded_chunks if c.chunk.book_id == sample_book_ids[0]]
        book_b_chunks = [c for c in sample_embedded_chunks if c.chunk.book_id == sample_book_ids[1]]

        memory_store.add(book_a_chunks, profile_id="profile-a")
        memory_store.add(book_b_chunks, profile_id="profile-b")

        books_a = memory_store.get_indexed_books(profile_id="profile-a")
        books_b = memory_store.get_indexed_books(profile_id="profile-b")

        assert sample_book_ids[0] in books_a
        assert sample_book_ids[1] not in books_a
        assert sample_book_ids[0] not in books_b
        assert sample_book_ids[1] in books_b

    def test_clear_profile_only(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
    ) -> None:
        """Clearing a profile should not affect other profiles."""
        memory_store.add(sample_embedded_chunks[:2], profile_id="profile-a")
        memory_store.add(sample_embedded_chunks[2:], profile_id="profile-b")

        # Clear only profile-a
        memory_store.clear(profile_id="profile-a")

        assert memory_store.get_chunk_count(profile_id="profile-a") == 0
        assert memory_store.get_chunk_count(profile_id="profile-b") == len(sample_embedded_chunks) - 2

    def test_clear_all_profiles(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
    ) -> None:
        """Clearing without profile_id should clear all profiles."""
        memory_store.add(sample_embedded_chunks[:2], profile_id="profile-a")
        memory_store.add(sample_embedded_chunks[2:], profile_id="profile-b")

        memory_store.clear()

        assert memory_store.get_chunk_count(profile_id="profile-a") == 0
        assert memory_store.get_chunk_count(profile_id="profile-b") == 0

    def test_get_profiles(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
    ) -> None:
        """get_profiles should return list of profiles with data."""
        memory_store.add(sample_embedded_chunks[:1], profile_id="profile-a")
        memory_store.add(sample_embedded_chunks[1:2], profile_id="profile-b")

        profiles = memory_store.get_profiles()

        assert "profile-a" in profiles
        assert "profile-b" in profiles

    def test_default_profile(
        self,
        memory_store,
        sample_embedded_chunks: list[EmbeddedChunk],
    ) -> None:
        """Adding without profile_id should use default profile."""
        memory_store.add(sample_embedded_chunks)

        # Should be able to retrieve with profile_id=None
        assert memory_store.get_chunk_count() == len(sample_embedded_chunks)

        # Default profile should be in the profiles list
        profiles = memory_store.get_profiles()
        assert len(profiles) == 1  # Only default profile
