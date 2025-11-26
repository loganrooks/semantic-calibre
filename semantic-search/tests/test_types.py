"""Tests for core types module.

These tests verify the data structures and their serialization behavior.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from calibre_semantic.core.types import (
    BookIdentifier,
    BookMetadata,
    ChunkLocation,
    ChunkType,
    ChunkingConfig,
    EmbeddedChunk,
    EmbeddingConfig,
    EmbeddingProvider,
    IndexingProgress,
    SearchResult,
    SearchResults,
    SemanticSearchConfig,
    TextChunk,
    VectorStoreConfig,
)


class TestBookIdentifier:
    """Tests for BookIdentifier dataclass."""

    def test_create_book_identifier(self) -> None:
        """Should create BookIdentifier with correct attributes."""
        book_id = BookIdentifier(
            library_id="lib-uuid-123",
            book_id=42,
            format="EPUB",
        )
        assert book_id.library_id == "lib-uuid-123"
        assert book_id.book_id == 42
        assert book_id.format == "EPUB"

    def test_str_representation(self) -> None:
        """String representation should be colon-separated."""
        book_id = BookIdentifier("lib-123", 42, "PDF")
        assert str(book_id) == "lib-123:42:PDF"

    def test_from_string(self) -> None:
        """Should parse string representation correctly."""
        book_id = BookIdentifier.from_string("lib-123:42:EPUB")
        assert book_id.library_id == "lib-123"
        assert book_id.book_id == 42
        assert book_id.format == "EPUB"

    def test_from_string_invalid(self) -> None:
        """Should raise ValueError for invalid string."""
        with pytest.raises(ValueError):
            BookIdentifier.from_string("invalid")

    def test_frozen(self) -> None:
        """BookIdentifier should be immutable."""
        book_id = BookIdentifier("lib", 1, "EPUB")
        with pytest.raises(AttributeError):
            book_id.book_id = 2  # type: ignore

    def test_hashable(self) -> None:
        """BookIdentifier should be hashable for use in sets/dicts."""
        book_id1 = BookIdentifier("lib", 1, "EPUB")
        book_id2 = BookIdentifier("lib", 1, "EPUB")
        book_id3 = BookIdentifier("lib", 2, "EPUB")

        # Same values should be equal and have same hash
        assert book_id1 == book_id2
        assert hash(book_id1) == hash(book_id2)

        # Different values should not be equal
        assert book_id1 != book_id3

        # Should work in sets
        book_set = {book_id1, book_id2, book_id3}
        assert len(book_set) == 2


class TestChunkLocation:
    """Tests for ChunkLocation dataclass."""

    def test_create_chunk_location(self) -> None:
        """Should create ChunkLocation with correct attributes."""
        loc = ChunkLocation(
            spine_index=0,
            spine_name="chapter1.xhtml",
            start_offset=100,
            end_offset=500,
            cfi="/4/2/1:0",
        )
        assert loc.spine_index == 0
        assert loc.spine_name == "chapter1.xhtml"
        assert loc.start_offset == 100
        assert loc.end_offset == 500
        assert loc.cfi == "/4/2/1:0"

    def test_to_dict(self) -> None:
        """Should convert to dictionary correctly."""
        loc = ChunkLocation(0, "ch1.xhtml", 0, 100, "/4/2:0")
        d = loc.to_dict()
        assert d == {
            "spine_index": 0,
            "spine_name": "ch1.xhtml",
            "start_offset": 0,
            "end_offset": 100,
            "cfi": "/4/2:0",
        }

    def test_from_dict(self) -> None:
        """Should create from dictionary correctly."""
        d = {
            "spine_index": 1,
            "spine_name": "ch2.xhtml",
            "start_offset": 200,
            "end_offset": 400,
        }
        loc = ChunkLocation.from_dict(d)
        assert loc.spine_index == 1
        assert loc.spine_name == "ch2.xhtml"
        assert loc.cfi is None  # Optional field


class TestTextChunk:
    """Tests for TextChunk dataclass."""

    def test_create_text_chunk(
        self,
        sample_book_id: BookIdentifier,
        sample_chunk_location: ChunkLocation,
    ) -> None:
        """Should create TextChunk with correct attributes."""
        chunk = TextChunk(
            id="chunk-001",
            book_id=sample_book_id,
            text="Sample text content.",
            location=sample_chunk_location,
            chunk_type=ChunkType.PARAGRAPH,
            chapter_title="Chapter 1",
        )
        assert chunk.id == "chunk-001"
        assert chunk.text == "Sample text content."
        assert chunk.chunk_type == ChunkType.PARAGRAPH

    def test_default_metadata(
        self,
        sample_book_id: BookIdentifier,
        sample_chunk_location: ChunkLocation,
    ) -> None:
        """Metadata should default to empty dict."""
        chunk = TextChunk(
            id="chunk",
            book_id=sample_book_id,
            text="text",
            location=sample_chunk_location,
            chunk_type=ChunkType.SECTION,
        )
        assert chunk.metadata == {}


class TestEmbeddingConfig:
    """Tests for EmbeddingConfig dataclass."""

    def test_default_values(self) -> None:
        """Should have sensible defaults."""
        config = EmbeddingConfig()
        assert config.provider == "sentence-transformers"
        assert config.model == "all-MiniLM-L6-v2"
        assert config.batch_size == 32
        assert config.device == "auto"
        assert config.api_key is None

    def test_custom_values(self) -> None:
        """Should accept custom values."""
        config = EmbeddingConfig(
            provider="openai",
            model="text-embedding-3-small",
            api_key="sk-xxx",
            batch_size=64,
        )
        assert config.provider == "openai"
        assert config.model == "text-embedding-3-small"
        assert config.api_key == "sk-xxx"


class TestSemanticSearchConfig:
    """Tests for SemanticSearchConfig dataclass."""

    def test_default_values(self) -> None:
        """Should have sensible defaults."""
        config = SemanticSearchConfig()
        assert config.embedding.provider == "sentence-transformers"
        assert config.vector_store.backend == "sqlite-vec"
        assert config.chunking.strategy == "semantic"
        assert config.default_result_limit == 20
        assert config.min_similarity_score == 0.3

    def test_to_dict(self) -> None:
        """Should convert to dictionary correctly."""
        config = SemanticSearchConfig()
        d = config.to_dict()
        assert d["embedding"]["provider"] == "sentence-transformers"
        assert d["vector_store"]["backend"] == "sqlite-vec"
        assert d["chunking"]["target_size"] == 512

    def test_from_dict(self) -> None:
        """Should create from dictionary correctly."""
        d = {
            "embedding": {
                "provider": "openai",
                "model": "text-embedding-3-small",
            },
            "default_result_limit": 50,
        }
        config = SemanticSearchConfig.from_dict(d)
        assert config.embedding.provider == "openai"
        assert config.default_result_limit == 50
        # Defaults should still apply
        assert config.vector_store.backend == "sqlite-vec"

    def test_to_dict_from_dict_roundtrip(self) -> None:
        """Converting to dict and back should preserve values."""
        original = SemanticSearchConfig(
            embedding=EmbeddingConfig(model="custom-model"),
            default_result_limit=100,
        )
        d = original.to_dict()
        restored = SemanticSearchConfig.from_dict(d)

        assert restored.embedding.model == original.embedding.model
        assert restored.default_result_limit == original.default_result_limit


class TestSearchResult:
    """Tests for SearchResult dataclass."""

    def test_create_search_result(self, sample_text_chunk: TextChunk) -> None:
        """Should create SearchResult with correct attributes."""
        result = SearchResult(
            chunk=sample_text_chunk,
            score=0.85,
            highlights=[(0, 10), (20, 30)],
        )
        assert result.chunk == sample_text_chunk
        assert result.score == 0.85
        assert len(result.highlights) == 2

    def test_default_highlights(self, sample_text_chunk: TextChunk) -> None:
        """Highlights should default to empty list."""
        result = SearchResult(chunk=sample_text_chunk, score=0.5)
        assert result.highlights == []


class TestSearchResults:
    """Tests for SearchResults dataclass."""

    def test_create_search_results(self, sample_text_chunk: TextChunk) -> None:
        """Should create SearchResults with correct attributes."""
        results = SearchResults(
            query="test query",
            results=[SearchResult(chunk=sample_text_chunk, score=0.8)],
            total_searched=1000,
            search_time_ms=15.5,
            model_id="test-model",
        )
        assert results.query == "test query"
        assert len(results.results) == 1
        assert results.total_searched == 1000
        assert results.search_time_ms == 15.5


class TestIndexingProgress:
    """Tests for IndexingProgress dataclass."""

    def test_create_progress(self, sample_book_id: BookIdentifier) -> None:
        """Should create IndexingProgress correctly."""
        progress = IndexingProgress(
            book_id=sample_book_id,
            status="embedding",
            progress=0.5,
            message="Processing chunks",
        )
        assert progress.status == "embedding"
        assert progress.progress == 0.5
        assert progress.error is None


class TestEmbeddingProviderProtocol:
    """Tests for EmbeddingProvider protocol checking."""

    def test_protocol_is_runtime_checkable(self) -> None:
        """EmbeddingProvider should be runtime checkable."""
        # Create a minimal class that implements the protocol
        class MinimalProvider:
            @property
            def model_id(self) -> str:
                return "test"

            @property
            def dimension(self) -> int:
                return 384

            @property
            def max_tokens(self) -> int:
                return 512

            def embed(self, texts):
                return [np.zeros(384) for _ in texts]

            async def embed_async(self, texts):
                return self.embed(texts)

            def embed_query(self, query):
                return np.zeros(384)

        provider = MinimalProvider()
        assert isinstance(provider, EmbeddingProvider)

    def test_incomplete_implementation_fails_check(self) -> None:
        """Incomplete implementation should fail isinstance check."""
        class IncompleteProvider:
            @property
            def model_id(self) -> str:
                return "test"
            # Missing other required methods

        provider = IncompleteProvider()
        assert not isinstance(provider, EmbeddingProvider)
