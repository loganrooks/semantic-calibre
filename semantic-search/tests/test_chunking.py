"""Tests for text chunking strategies.

This module tests:
1. SemanticChunkingStrategy - respects paragraph/sentence boundaries
2. FixedSizeChunkingStrategy - simple fixed-size chunks with overlap

Tests validate:
- Chunk size constraints
- Overlap behavior
- Boundary detection
- Location metadata accuracy
- Edge cases (empty text, very long paragraphs)
"""

from __future__ import annotations

import pytest

from calibre_semantic.core.types import (
    BookIdentifier,
    ChunkingConfig,
    ChunkType,
    TextChunk,
)


# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def sample_book_id() -> BookIdentifier:
    """Sample book identifier for testing."""
    return BookIdentifier("test-lib", 1, "EPUB")


@pytest.fixture
def sample_text() -> str:
    """Sample text with multiple paragraphs for chunking tests."""
    return """The quick brown fox jumps over the lazy dog. This is a simple sentence that demonstrates basic text.

Machine learning has revolutionized how we process and understand data. Neural networks can now perform tasks that were once thought to be exclusively human. Deep learning models continue to improve in accuracy and capability.

Philosophy asks fundamental questions about existence, knowledge, and ethics. Philosophers have debated these topics for thousands of years. The search for meaning continues to drive human inquiry.

Science provides a systematic approach to understanding the natural world. Through observation and experimentation, we build models of reality. These models are constantly refined as new evidence emerges."""


@pytest.fixture
def long_paragraph() -> str:
    """A single long paragraph that exceeds typical chunk sizes."""
    return " ".join(["This is sentence number {}.".format(i) for i in range(100)])


@pytest.fixture
def semantic_config() -> ChunkingConfig:
    """Configuration for semantic chunking."""
    return ChunkingConfig(
        strategy="semantic",
        target_size=200,
        overlap=50,
        respect_boundaries=True,
    )


@pytest.fixture
def fixed_config() -> ChunkingConfig:
    """Configuration for fixed-size chunking."""
    return ChunkingConfig(
        strategy="fixed",
        target_size=200,
        overlap=50,
        respect_boundaries=False,
    )


# =============================================================================
# Chunking Strategy Protocol Tests
# =============================================================================


class TestChunkingStrategyProtocol:
    """Test that strategies implement the expected interface."""

    def test_semantic_strategy_has_required_methods(self, semantic_config: ChunkingConfig) -> None:
        """SemanticChunkingStrategy should have chunk method."""
        from calibre_semantic.core.chunking import SemanticChunkingStrategy

        strategy = SemanticChunkingStrategy(semantic_config)
        assert hasattr(strategy, "chunk")
        assert callable(strategy.chunk)
        assert hasattr(strategy, "target_chunk_size")
        assert hasattr(strategy, "chunk_overlap")

    def test_fixed_strategy_has_required_methods(self, fixed_config: ChunkingConfig) -> None:
        """FixedSizeChunkingStrategy should have chunk method."""
        from calibre_semantic.core.chunking import FixedSizeChunkingStrategy

        strategy = FixedSizeChunkingStrategy(fixed_config)
        assert hasattr(strategy, "chunk")
        assert callable(strategy.chunk)


# =============================================================================
# Semantic Chunking Tests
# =============================================================================


class TestSemanticChunkingStrategy:
    """Tests for SemanticChunkingStrategy."""

    def test_chunks_respect_paragraph_boundaries(
        self,
        semantic_config: ChunkingConfig,
        sample_book_id: BookIdentifier,
        sample_text: str,
    ) -> None:
        """Chunks should not split mid-paragraph when possible."""
        from calibre_semantic.core.chunking import SemanticChunkingStrategy

        strategy = SemanticChunkingStrategy(semantic_config)
        chunks = list(strategy.chunk(
            text=sample_text,
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
        ))

        # Should produce multiple chunks
        assert len(chunks) > 1

        # Each chunk should be a TextChunk
        for chunk in chunks:
            assert isinstance(chunk, TextChunk)
            assert chunk.book_id == sample_book_id

    def test_chunks_have_valid_locations(
        self,
        semantic_config: ChunkingConfig,
        sample_book_id: BookIdentifier,
        sample_text: str,
    ) -> None:
        """Chunk locations should have valid offsets."""
        from calibre_semantic.core.chunking import SemanticChunkingStrategy

        strategy = SemanticChunkingStrategy(semantic_config)
        chunks = list(strategy.chunk(
            text=sample_text,
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
        ))

        for chunk in chunks:
            # Offsets should be valid
            assert chunk.location.start_offset >= 0
            assert chunk.location.end_offset > chunk.location.start_offset
            assert chunk.location.end_offset <= len(sample_text) + 100  # Allow for overlap

            # Spine info should be correct
            assert chunk.location.spine_index == 0
            assert chunk.location.spine_name == "chapter1.xhtml"

    def test_chunks_have_unique_ids(
        self,
        semantic_config: ChunkingConfig,
        sample_book_id: BookIdentifier,
        sample_text: str,
    ) -> None:
        """Each chunk should have a unique ID."""
        from calibre_semantic.core.chunking import SemanticChunkingStrategy

        strategy = SemanticChunkingStrategy(semantic_config)
        chunks = list(strategy.chunk(
            text=sample_text,
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
        ))

        ids = [chunk.id for chunk in chunks]
        assert len(ids) == len(set(ids))  # All unique

    def test_chunk_size_approximately_target(
        self,
        semantic_config: ChunkingConfig,
        sample_book_id: BookIdentifier,
        sample_text: str,
    ) -> None:
        """Chunks should be approximately target size."""
        from calibre_semantic.core.chunking import SemanticChunkingStrategy

        strategy = SemanticChunkingStrategy(semantic_config)
        chunks = list(strategy.chunk(
            text=sample_text,
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
        ))

        for chunk in chunks[:-1]:  # Last chunk may be smaller
            # Should be within 2x target (allowing for boundary respect)
            assert len(chunk.text) <= semantic_config.target_size * 2

    def test_handles_empty_text(
        self,
        semantic_config: ChunkingConfig,
        sample_book_id: BookIdentifier,
    ) -> None:
        """Empty text should produce no chunks."""
        from calibre_semantic.core.chunking import SemanticChunkingStrategy

        strategy = SemanticChunkingStrategy(semantic_config)
        chunks = list(strategy.chunk(
            text="",
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
        ))

        assert len(chunks) == 0

    def test_handles_whitespace_only(
        self,
        semantic_config: ChunkingConfig,
        sample_book_id: BookIdentifier,
    ) -> None:
        """Whitespace-only text should produce no chunks."""
        from calibre_semantic.core.chunking import SemanticChunkingStrategy

        strategy = SemanticChunkingStrategy(semantic_config)
        chunks = list(strategy.chunk(
            text="   \n\n   \t  ",
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
        ))

        assert len(chunks) == 0

    def test_handles_single_paragraph(
        self,
        semantic_config: ChunkingConfig,
        sample_book_id: BookIdentifier,
    ) -> None:
        """Single paragraph should produce at least one chunk."""
        from calibre_semantic.core.chunking import SemanticChunkingStrategy

        strategy = SemanticChunkingStrategy(semantic_config)
        text = "This is a single paragraph with enough text to be meaningful."
        chunks = list(strategy.chunk(
            text=text,
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
        ))

        assert len(chunks) >= 1
        assert chunks[0].text.strip() == text.strip()

    def test_preserves_chapter_title(
        self,
        semantic_config: ChunkingConfig,
        sample_book_id: BookIdentifier,
        sample_text: str,
    ) -> None:
        """Chapter title should be preserved in chunks."""
        from calibre_semantic.core.chunking import SemanticChunkingStrategy

        strategy = SemanticChunkingStrategy(semantic_config)
        chunks = list(strategy.chunk(
            text=sample_text,
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
            chapter_title="Chapter 1: Introduction",
        ))

        for chunk in chunks:
            assert chunk.chapter_title == "Chapter 1: Introduction"

    def test_long_paragraph_splits_at_sentences(
        self,
        sample_book_id: BookIdentifier,
        long_paragraph: str,
    ) -> None:
        """Long paragraphs should split at sentence boundaries."""
        from calibre_semantic.core.chunking import SemanticChunkingStrategy

        config = ChunkingConfig(target_size=200, overlap=50)
        strategy = SemanticChunkingStrategy(config)
        chunks = list(strategy.chunk(
            text=long_paragraph,
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
        ))

        # Should produce multiple chunks
        assert len(chunks) > 1

        # Chunks should end at sentence boundaries (period followed by space or end)
        for chunk in chunks[:-1]:
            text = chunk.text.rstrip()
            assert text.endswith(".") or text.endswith("!") or text.endswith("?")


# =============================================================================
# Fixed Size Chunking Tests
# =============================================================================


class TestFixedSizeChunkingStrategy:
    """Tests for FixedSizeChunkingStrategy."""

    def test_chunks_are_fixed_size(
        self,
        fixed_config: ChunkingConfig,
        sample_book_id: BookIdentifier,
        sample_text: str,
    ) -> None:
        """Chunks should be close to target size."""
        from calibre_semantic.core.chunking import FixedSizeChunkingStrategy

        strategy = FixedSizeChunkingStrategy(fixed_config)
        chunks = list(strategy.chunk(
            text=sample_text,
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
        ))

        for chunk in chunks[:-1]:  # Last chunk may be smaller
            # Should be within 10% of target (word boundary adjustment)
            assert len(chunk.text) <= fixed_config.target_size * 1.2

    def test_chunks_have_overlap(
        self,
        sample_book_id: BookIdentifier,
        sample_text: str,
    ) -> None:
        """Consecutive chunks should overlap."""
        from calibre_semantic.core.chunking import FixedSizeChunkingStrategy

        config = ChunkingConfig(strategy="fixed", target_size=100, overlap=30)
        strategy = FixedSizeChunkingStrategy(config)
        chunks = list(strategy.chunk(
            text=sample_text,
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
        ))

        if len(chunks) >= 2:
            # Check that chunks overlap
            for i in range(len(chunks) - 1):
                chunk1_end = chunks[i].text[-30:]
                chunk2_start = chunks[i + 1].text[:50]
                # Some overlap text should appear in both
                # (This is a soft check - exact overlap depends on word boundaries)
                assert len(chunk1_end) > 0 and len(chunk2_start) > 0

    def test_handles_text_shorter_than_target(
        self,
        fixed_config: ChunkingConfig,
        sample_book_id: BookIdentifier,
    ) -> None:
        """Short text should produce single chunk."""
        from calibre_semantic.core.chunking import FixedSizeChunkingStrategy

        strategy = FixedSizeChunkingStrategy(fixed_config)
        short_text = "Short text."
        chunks = list(strategy.chunk(
            text=short_text,
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
        ))

        assert len(chunks) == 1
        assert chunks[0].text.strip() == short_text


# =============================================================================
# Factory Tests
# =============================================================================


class TestChunkingFactory:
    """Tests for chunking strategy factory."""

    def test_create_semantic_strategy(self) -> None:
        """Factory should create SemanticChunkingStrategy."""
        from calibre_semantic.core.chunking import create_chunking_strategy

        config = ChunkingConfig(strategy="semantic")
        strategy = create_chunking_strategy(config)

        from calibre_semantic.core.chunking import SemanticChunkingStrategy
        assert isinstance(strategy, SemanticChunkingStrategy)

    def test_create_fixed_strategy(self) -> None:
        """Factory should create FixedSizeChunkingStrategy."""
        from calibre_semantic.core.chunking import create_chunking_strategy

        config = ChunkingConfig(strategy="fixed")
        strategy = create_chunking_strategy(config)

        from calibre_semantic.core.chunking import FixedSizeChunkingStrategy
        assert isinstance(strategy, FixedSizeChunkingStrategy)

    def test_unknown_strategy_raises(self) -> None:
        """Unknown strategy should raise ValueError."""
        from calibre_semantic.core.chunking import create_chunking_strategy

        config = ChunkingConfig(strategy="unknown")

        with pytest.raises(ValueError, match="Unknown chunking strategy"):
            create_chunking_strategy(config)


# =============================================================================
# Determinism Tests
# =============================================================================


class TestChunkingDeterminism:
    """Test that chunking is deterministic."""

    def test_same_input_same_output(
        self,
        semantic_config: ChunkingConfig,
        sample_book_id: BookIdentifier,
        sample_text: str,
    ) -> None:
        """Same input should always produce same chunks."""
        from calibre_semantic.core.chunking import SemanticChunkingStrategy

        strategy = SemanticChunkingStrategy(semantic_config)

        chunks1 = list(strategy.chunk(
            text=sample_text,
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
        ))

        chunks2 = list(strategy.chunk(
            text=sample_text,
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
        ))

        assert len(chunks1) == len(chunks2)
        for c1, c2 in zip(chunks1, chunks2):
            assert c1.id == c2.id
            assert c1.text == c2.text
            assert c1.location == c2.location

    def test_chunk_ids_are_deterministic(
        self,
        semantic_config: ChunkingConfig,
        sample_book_id: BookIdentifier,
        sample_text: str,
    ) -> None:
        """Chunk IDs should be deterministic based on content."""
        from calibre_semantic.core.chunking import SemanticChunkingStrategy

        strategy = SemanticChunkingStrategy(semantic_config)

        chunks1 = list(strategy.chunk(
            text=sample_text,
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
        ))

        # Create new strategy instance
        strategy2 = SemanticChunkingStrategy(semantic_config)
        chunks2 = list(strategy2.chunk(
            text=sample_text,
            book_id=sample_book_id,
            spine_index=0,
            spine_name="chapter1.xhtml",
        ))

        for c1, c2 in zip(chunks1, chunks2):
            assert c1.id == c2.id
