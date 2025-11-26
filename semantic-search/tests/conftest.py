"""Shared test fixtures for calibre-semantic tests."""

from __future__ import annotations

import pytest
import numpy as np

from calibre_semantic.core.types import (
    BookIdentifier,
    ChunkLocation,
    ChunkType,
    EmbeddingConfig,
    TextChunk,
)


@pytest.fixture
def sample_book_id() -> BookIdentifier:
    """Create a sample book identifier for testing."""
    return BookIdentifier(
        library_id="test-library-uuid",
        book_id=42,
        format="EPUB",
    )


@pytest.fixture
def sample_chunk_location() -> ChunkLocation:
    """Create a sample chunk location for testing."""
    return ChunkLocation(
        spine_index=0,
        spine_name="chapter1.xhtml",
        start_offset=100,
        end_offset=500,
        cfi="/4/2[chapter1]/2/1:0",
    )


@pytest.fixture
def sample_text_chunk(sample_book_id: BookIdentifier, sample_chunk_location: ChunkLocation) -> TextChunk:
    """Create a sample text chunk for testing."""
    return TextChunk(
        id="test-chunk-001",
        book_id=sample_book_id,
        text="The quick brown fox jumps over the lazy dog. This is a sample text chunk for testing semantic search functionality.",
        location=sample_chunk_location,
        chunk_type=ChunkType.PARAGRAPH,
        chapter_title="Chapter 1: Introduction",
    )


@pytest.fixture
def sample_texts() -> list[str]:
    """Sample texts for embedding tests."""
    return [
        "The quick brown fox jumps over the lazy dog.",
        "Machine learning is transforming how we process information.",
        "Semantic search finds results based on meaning, not just keywords.",
        "Books contain knowledge accumulated over centuries.",
        "Natural language processing enables computers to understand text.",
    ]


@pytest.fixture
def default_embedding_config() -> EmbeddingConfig:
    """Default embedding configuration for testing."""
    return EmbeddingConfig(
        provider="sentence-transformers",
        model="all-MiniLM-L6-v2",
        batch_size=32,
        device="cpu",  # Use CPU for tests
    )


@pytest.fixture
def mock_embeddings() -> list[np.ndarray]:
    """Create mock embedding vectors for testing."""
    # all-MiniLM-L6-v2 produces 384-dimensional vectors
    rng = np.random.default_rng(42)
    return [rng.random(384).astype(np.float32) for _ in range(5)]


class MockEmbeddingProvider:
    """Mock embedding provider for testing without real models.

    This mock implements the EmbeddingProvider protocol for testing
    code that depends on embeddings without requiring actual model loading.
    """

    def __init__(
        self,
        dimension: int = 384,
        model_id: str = "mock-model-v1",
        max_tokens: int = 512,
        deterministic: bool = True,
    ):
        self._dimension = dimension
        self._model_id = model_id
        self._max_tokens = max_tokens
        self._deterministic = deterministic
        self._rng = np.random.default_rng(42)
        self._call_count = 0

    @property
    def model_id(self) -> str:
        return self._model_id

    @property
    def dimension(self) -> int:
        return self._dimension

    @property
    def max_tokens(self) -> int:
        return self._max_tokens

    def embed(self, texts: list[str]) -> list[np.ndarray]:
        """Generate mock embeddings.

        If deterministic=True, same text produces same embedding.
        """
        self._call_count += 1
        embeddings = []

        for text in texts:
            if self._deterministic:
                # Create deterministic embedding based on text hash
                seed = hash(text) % (2**32)
                rng = np.random.default_rng(seed)
                vec = rng.random(self._dimension).astype(np.float32)
            else:
                vec = self._rng.random(self._dimension).astype(np.float32)

            # Normalize to unit length
            vec = vec / np.linalg.norm(vec)
            embeddings.append(vec)

        return embeddings

    async def embed_async(self, texts: list[str]) -> list[np.ndarray]:
        """Async mock embedding - just calls sync version."""
        return self.embed(texts)

    def embed_query(self, query: str) -> np.ndarray:
        """Generate mock query embedding."""
        return self.embed([query])[0]

    @property
    def call_count(self) -> int:
        """Number of times embed() was called."""
        return self._call_count


@pytest.fixture
def mock_embedding_provider() -> MockEmbeddingProvider:
    """Create a mock embedding provider for testing."""
    return MockEmbeddingProvider()
