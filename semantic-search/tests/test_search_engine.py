"""Tests for SemanticSearchEngine.

This module tests the main orchestration class that ties together:
- Embedding provider
- Vector store
- Chunking strategy

Tests validate:
- Engine initialization
- Indexing flow (chunk -> embed -> store)
- Search flow (embed query -> search store -> return results)
- Book management (add, remove, check indexed)
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import numpy as np
import pytest

from calibre_semantic.core.types import (
    BookIdentifier,
    BookMetadata,
    ChunkingConfig,
    ChunkLocation,
    ChunkType,
    EmbeddedChunk,
    EmbeddingConfig,
    SearchResult,
    SearchResults,
    SemanticSearchConfig,
    TextChunk,
    VectorStoreConfig,
)


# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def sample_book_id() -> BookIdentifier:
    """Sample book identifier for testing."""
    return BookIdentifier("test-lib", 1, "EPUB")


@pytest.fixture
def sample_book_metadata(sample_book_id: BookIdentifier) -> BookMetadata:
    """Sample book metadata for testing."""
    return BookMetadata(
        book_id=sample_book_id,
        title="Test Book",
        authors=["Test Author"],
    )


@pytest.fixture
def sample_text() -> str:
    """Sample text for indexing tests."""
    return """This is the first paragraph about machine learning and artificial intelligence.

This is the second paragraph discussing neural networks and deep learning.

The third paragraph covers natural language processing and text analysis."""


@pytest.fixture
def mock_embedding_provider():
    """Create a mock embedding provider."""
    provider = MagicMock()
    provider.model_id = "test-model"
    provider.dimension = 384
    provider.max_tokens = 512

    # Return deterministic embeddings based on text hash
    def embed_side_effect(texts):
        embeddings = []
        for text in texts:
            # Create reproducible embedding from text
            np.random.seed(hash(text) % 2**32)
            embeddings.append(np.random.randn(384).astype(np.float32))
        return embeddings

    provider.embed.side_effect = embed_side_effect
    provider.embed_query.side_effect = lambda q: embed_side_effect([q])[0]
    return provider


@pytest.fixture
def mock_vector_store():
    """Create a mock vector store with profile support."""
    store = MagicMock()
    store._chunks: dict[str, EmbeddedChunk] = {}
    store._model_id = None

    def add_chunks(chunks, profile_id=None):
        for chunk in chunks:
            store._chunks[chunk.chunk.id] = chunk

    def remove_book(book_id, profile_id=None):
        to_remove = [
            cid for cid, c in store._chunks.items()
            if c.chunk.book_id == book_id
        ]
        for cid in to_remove:
            del store._chunks[cid]
        return len(to_remove)

    def get_indexed_books(profile_id=None):
        return {c.chunk.book_id for c in store._chunks.values()}

    def get_chunk_count(book_id=None, profile_id=None):
        if book_id is None:
            return len(store._chunks)
        return sum(1 for c in store._chunks.values() if c.chunk.book_id == book_id)

    def clear(profile_id=None):
        if profile_id is None:
            store._chunks.clear()

    store.add.side_effect = add_chunks
    store.remove_book.side_effect = remove_book
    store.get_indexed_books.side_effect = get_indexed_books
    store.get_chunk_count.side_effect = get_chunk_count
    store.get_model_id.return_value = None
    store.set_model_id.side_effect = lambda m: setattr(store, '_model_id', m)
    # Use return_value for search so tests can override it
    store.search.return_value = []
    store.clear.side_effect = clear
    store.get_profiles.return_value = []

    return store


@pytest.fixture
def default_config() -> SemanticSearchConfig:
    """Default configuration for testing."""
    return SemanticSearchConfig(
        embedding=EmbeddingConfig(provider="mock"),
        vector_store=VectorStoreConfig(backend="memory"),
        chunking=ChunkingConfig(target_size=200, overlap=50),
    )


# =============================================================================
# Engine Initialization Tests
# =============================================================================


class TestEngineInitialization:
    """Tests for SemanticSearchEngine initialization."""

    def test_engine_can_be_created_with_config(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
    ) -> None:
        """Engine should initialize with provided components."""
        from calibre_semantic.search import SemanticSearchEngine

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
        )

        assert engine is not None
        assert engine.config == default_config

    def test_engine_exposes_model_info(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
    ) -> None:
        """Engine should expose embedding model information."""
        from calibre_semantic.search import SemanticSearchEngine

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
        )

        assert engine.model_id == "test-model"
        assert engine.embedding_dimension == 384


# =============================================================================
# Indexing Tests
# =============================================================================


class TestIndexing:
    """Tests for book indexing functionality."""

    def test_index_text_creates_chunks_and_embeddings(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
        sample_book_id: BookIdentifier,
        sample_text: str,
    ) -> None:
        """Indexing text should create chunks and store embeddings."""
        from calibre_semantic.search import SemanticSearchEngine

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
        )

        engine.index_text(
            text=sample_text,
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
        )

        # Verify embedding was called
        assert mock_embedding_provider.embed.called

        # Verify chunks were added to store
        assert mock_vector_store.add.called

    def test_index_book_calls_index_text_for_each_spine_item(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
        sample_book_id: BookIdentifier,
    ) -> None:
        """Indexing a book should process all spine items."""
        from calibre_semantic.search import SemanticSearchEngine

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
        )

        # Mock spine content
        spine_items = [
            ("chapter1.xhtml", "Content of chapter 1"),
            ("chapter2.xhtml", "Content of chapter 2"),
            ("chapter3.xhtml", "Content of chapter 3"),
        ]

        engine.index_book_content(
            book_id=sample_book_id,
            spine_items=spine_items,
        )

        # Should have called embed for each spine item's content
        assert mock_embedding_provider.embed.call_count >= 1
        assert mock_vector_store.add.called

    def test_reindex_removes_old_chunks_first(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
        sample_book_id: BookIdentifier,
        sample_text: str,
    ) -> None:
        """Re-indexing should remove existing chunks before adding new ones."""
        from calibre_semantic.search import SemanticSearchEngine

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
        )

        # Index once
        engine.index_text(
            text=sample_text,
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
        )

        # Re-index with force=True
        engine.index_text(
            text=sample_text,
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
            force_reindex=True,
        )

        # Should have called remove_book
        assert mock_vector_store.remove_book.called

    def test_index_epub_extracts_and_indexes_content(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
        sample_book_id: BookIdentifier,
    ) -> None:
        """index_epub should extract text from EPUB and index it."""
        from calibre_semantic.search import SemanticSearchEngine
        from tests.test_epub_extraction import create_test_epub

        # Create a test EPUB
        content_files = {
            'chapter1.xhtml': '''<?xml version="1.0"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<body><h1>Chapter 1</h1><p>Machine learning content.</p></body>
</html>''',
            'chapter2.xhtml': '''<?xml version="1.0"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<body><h1>Chapter 2</h1><p>Deep learning content.</p></body>
</html>''',
        }
        epub_bytes = create_test_epub(content_files)

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
        )

        chunk_count = engine.index_epub(epub_bytes, sample_book_id)

        # Should have indexed content from both chapters
        assert chunk_count > 0
        assert mock_embedding_provider.embed.called
        assert mock_vector_store.add.called


# =============================================================================
# Search Tests
# =============================================================================


class TestSearch:
    """Tests for semantic search functionality."""

    def test_search_returns_results(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
        sample_book_id: BookIdentifier,
    ) -> None:
        """Search should return ranked results."""
        from calibre_semantic.search import SemanticSearchEngine

        # Set up mock search results
        mock_chunk = TextChunk(
            id="chunk-1",
            book_id=sample_book_id,
            text="Machine learning is transforming industries.",
            location=ChunkLocation(
                spine_index=0,
                spine_name="chapter1.xhtml",
                start_offset=0,
                end_offset=45,
            ),
            chunk_type=ChunkType.PARAGRAPH,
        )
        mock_vector_store.search.return_value = [(mock_chunk, 0.85)]

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
        )

        results = engine.search("machine learning applications")

        assert isinstance(results, SearchResults)
        assert len(results.results) == 1
        assert results.results[0].score == 0.85
        assert results.results[0].chunk.text == "Machine learning is transforming industries."

    def test_search_filters_by_book(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
        sample_book_id: BookIdentifier,
    ) -> None:
        """Search should filter results by book when specified."""
        from calibre_semantic.search import SemanticSearchEngine

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
        )

        engine.search("query", filter_book_ids=[sample_book_id])

        # Verify filter was passed to store
        call_kwargs = mock_vector_store.search.call_args[1]
        assert call_kwargs.get("filter_book_ids") == [sample_book_id]

    def test_search_filters_by_library(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
    ) -> None:
        """Search should filter results by library when specified."""
        from calibre_semantic.search import SemanticSearchEngine

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
        )

        engine.search("query", filter_libraries=["lib-1", "lib-2"])

        # Verify filter was passed to store
        call_kwargs = mock_vector_store.search.call_args[1]
        assert call_kwargs.get("filter_libraries") == ["lib-1", "lib-2"]

    def test_search_respects_limit(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
    ) -> None:
        """Search should respect result limit."""
        from calibre_semantic.search import SemanticSearchEngine

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
        )

        engine.search("query", limit=5)

        # Verify limit was passed to store
        call_kwargs = mock_vector_store.search.call_args[1]
        assert call_kwargs.get("limit") == 5

    def test_search_records_timing(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
    ) -> None:
        """Search should record timing information."""
        from calibre_semantic.search import SemanticSearchEngine

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
        )

        results = engine.search("query")

        assert results.search_time_ms >= 0
        assert results.model_id == "test-model"


# =============================================================================
# Book Management Tests
# =============================================================================


class TestBookManagement:
    """Tests for book management functionality."""

    def test_is_indexed_returns_false_for_new_book(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
        sample_book_id: BookIdentifier,
    ) -> None:
        """is_indexed should return False for non-indexed books."""
        from calibre_semantic.search import SemanticSearchEngine

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
        )

        assert engine.is_indexed(sample_book_id) is False

    def test_is_indexed_returns_true_after_indexing(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
        sample_book_id: BookIdentifier,
        sample_text: str,
    ) -> None:
        """is_indexed should return True after indexing."""
        from calibre_semantic.search import SemanticSearchEngine

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
        )

        engine.index_text(
            text=sample_text,
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
        )

        assert engine.is_indexed(sample_book_id) is True

    def test_remove_book_clears_index(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
        sample_book_id: BookIdentifier,
        sample_text: str,
    ) -> None:
        """remove_book should clear all indexed chunks for that book."""
        from calibre_semantic.search import SemanticSearchEngine

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
        )

        engine.index_text(
            text=sample_text,
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
        )

        removed_count = engine.remove_book(sample_book_id)

        assert removed_count > 0
        assert engine.is_indexed(sample_book_id) is False

    def test_get_indexed_books(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
        sample_text: str,
    ) -> None:
        """get_indexed_books should return all indexed book IDs."""
        from calibre_semantic.search import SemanticSearchEngine

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
        )

        book1 = BookIdentifier("lib", 1, "EPUB")
        book2 = BookIdentifier("lib", 2, "EPUB")

        engine.index_text(sample_text, book1, 0, "ch1.xhtml")
        engine.index_text(sample_text, book2, 0, "ch1.xhtml")

        indexed = engine.get_indexed_books()
        assert book1 in indexed
        assert book2 in indexed

    def test_get_stats(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
        sample_book_id: BookIdentifier,
        sample_text: str,
    ) -> None:
        """get_stats should return index statistics."""
        from calibre_semantic.search import SemanticSearchEngine

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
        )

        engine.index_text(
            text=sample_text,
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
        )

        stats = engine.get_stats()

        assert "total_chunks" in stats
        assert "total_books" in stats
        assert "model_id" in stats


# =============================================================================
# On-Demand Indexing Tests
# =============================================================================


class TestOnDemandIndexing:
    """Tests for on-demand indexing with ProfileManager integration."""

    @pytest.fixture
    def profile_manager(self):
        """Create an in-memory ProfileManager for testing."""
        from calibre_semantic.core.profiles import ProfileManager
        return ProfileManager()

    @pytest.fixture
    def test_profile_id(self, profile_manager):
        """Create a test profile and return its ID."""
        profile = profile_manager.create_profile(
            name="Test Profile",
            provider="mock",
            model="test-model",
            dimension=384,
            profile_id="test-profile",
        )
        return profile.id

    def test_engine_with_profile_manager(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
        profile_manager,
    ) -> None:
        """Engine should accept ProfileManager."""
        from calibre_semantic.search import SemanticSearchEngine

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
            profile_manager=profile_manager,
        )

        assert engine.has_profile_manager is True
        assert engine.profile_manager is profile_manager

    def test_engine_without_profile_manager(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
    ) -> None:
        """Engine should work without ProfileManager."""
        from calibre_semantic.search import SemanticSearchEngine

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
        )

        assert engine.has_profile_manager is False
        assert engine.profile_manager is None

    def test_indexing_tracks_status(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
        profile_manager,
        test_profile_id: str,
        sample_book_id: BookIdentifier,
        sample_text: str,
    ) -> None:
        """Indexing should track status in ProfileManager."""
        from calibre_semantic.search import SemanticSearchEngine
        from calibre_semantic.core.types import IndexStatus

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
            profile_manager=profile_manager,
        )

        # Use index_book_content (not index_text) to track status
        engine.index_book_content(
            book_id=sample_book_id,
            spine_items=[("chapter1.xhtml", sample_text)],
            profile_id=test_profile_id,
        )

        # Check status was recorded
        status = profile_manager.get_book_status(sample_book_id, test_profile_id)
        assert status is not None
        assert status.status == IndexStatus.COMPLETE
        assert status.chunk_count > 0

    def test_get_book_index_status(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
        profile_manager,
        test_profile_id: str,
        sample_book_id: BookIdentifier,
        sample_text: str,
    ) -> None:
        """get_book_index_status should return status from ProfileManager."""
        from calibre_semantic.search import SemanticSearchEngine
        from calibre_semantic.core.types import IndexStatus

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
            profile_manager=profile_manager,
        )

        # Before indexing - no status
        status = engine.get_book_index_status(sample_book_id, test_profile_id)
        assert status is None

        # After indexing - status should exist
        engine.index_book_content(
            book_id=sample_book_id,
            spine_items=[("chapter1.xhtml", sample_text)],
            profile_id=test_profile_id,
        )

        status = engine.get_book_index_status(sample_book_id, test_profile_id)
        assert status is not None
        assert status.status == IndexStatus.COMPLETE

    def test_needs_indexing_true_for_new_book(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
        profile_manager,
        test_profile_id: str,
        sample_book_id: BookIdentifier,
    ) -> None:
        """needs_indexing should return True for unindexed book."""
        from calibre_semantic.search import SemanticSearchEngine

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
            profile_manager=profile_manager,
        )

        assert engine.needs_indexing(sample_book_id, test_profile_id) is True

    def test_needs_indexing_false_after_indexing(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
        profile_manager,
        test_profile_id: str,
        sample_book_id: BookIdentifier,
        sample_text: str,
    ) -> None:
        """needs_indexing should return False after successful indexing."""
        from calibre_semantic.search import SemanticSearchEngine

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
            profile_manager=profile_manager,
        )

        engine.index_book_content(
            book_id=sample_book_id,
            spine_items=[("chapter1.xhtml", sample_text)],
            profile_id=test_profile_id,
        )

        assert engine.needs_indexing(sample_book_id, test_profile_id) is False

    def test_remove_book_clears_status(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
        profile_manager,
        test_profile_id: str,
        sample_book_id: BookIdentifier,
        sample_text: str,
    ) -> None:
        """remove_book should also remove status from ProfileManager."""
        from calibre_semantic.search import SemanticSearchEngine

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
            profile_manager=profile_manager,
        )

        # Index the book
        engine.index_book_content(
            book_id=sample_book_id,
            spine_items=[("chapter1.xhtml", sample_text)],
            profile_id=test_profile_id,
        )

        # Verify status exists
        assert engine.get_book_index_status(sample_book_id, test_profile_id) is not None

        # Remove the book
        engine.remove_book(sample_book_id, profile_id=test_profile_id)

        # Status should be cleared
        assert engine.get_book_index_status(sample_book_id, test_profile_id) is None

    def test_force_reindex_clears_status(
        self,
        default_config: SemanticSearchConfig,
        mock_embedding_provider,
        mock_vector_store,
        profile_manager,
        test_profile_id: str,
        sample_book_id: BookIdentifier,
        sample_text: str,
    ) -> None:
        """force_reindex should clear and update status."""
        from calibre_semantic.search import SemanticSearchEngine
        from calibre_semantic.core.types import IndexStatus

        engine = SemanticSearchEngine(
            config=default_config,
            embedding_provider=mock_embedding_provider,
            vector_store=mock_vector_store,
            profile_manager=profile_manager,
        )

        # First indexing
        engine.index_book_content(
            book_id=sample_book_id,
            spine_items=[("chapter1.xhtml", sample_text)],
            profile_id=test_profile_id,
        )

        first_status = engine.get_book_index_status(sample_book_id, test_profile_id)
        assert first_status is not None

        # Force reindex
        engine.index_book_content(
            book_id=sample_book_id,
            spine_items=[("chapter1.xhtml", sample_text + " more text")],
            profile_id=test_profile_id,
            force_reindex=True,
        )

        # Status should be updated
        second_status = engine.get_book_index_status(sample_book_id, test_profile_id)
        assert second_status is not None
        assert second_status.status == IndexStatus.COMPLETE
