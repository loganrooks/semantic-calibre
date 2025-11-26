"""Tests for embedding providers.

This module tests:
1. The EmbeddingProvider protocol contract
2. The BaseEmbeddingProvider common functionality
3. The SentenceTransformerProvider implementation

Tests are structured to validate:
- Interface compliance
- Embedding properties (dimension, normalization)
- Batching behavior
- Error handling
- Query vs document embedding distinction
"""

from __future__ import annotations

import pytest
import numpy as np
from typing import TYPE_CHECKING

from calibre_semantic.core.types import EmbeddingConfig, EmbeddingProvider

if TYPE_CHECKING:
    from conftest import MockEmbeddingProvider


class TestEmbeddingProviderProtocol:
    """Test that providers implement the EmbeddingProvider protocol correctly."""

    def test_mock_provider_implements_protocol(
        self, mock_embedding_provider: "MockEmbeddingProvider"
    ) -> None:
        """Mock provider should implement EmbeddingProvider protocol."""
        assert isinstance(mock_embedding_provider, EmbeddingProvider)

    def test_protocol_requires_model_id(
        self, mock_embedding_provider: "MockEmbeddingProvider"
    ) -> None:
        """Provider must have model_id property."""
        assert hasattr(mock_embedding_provider, "model_id")
        assert isinstance(mock_embedding_provider.model_id, str)
        assert len(mock_embedding_provider.model_id) > 0

    def test_protocol_requires_dimension(
        self, mock_embedding_provider: "MockEmbeddingProvider"
    ) -> None:
        """Provider must have dimension property."""
        assert hasattr(mock_embedding_provider, "dimension")
        assert isinstance(mock_embedding_provider.dimension, int)
        assert mock_embedding_provider.dimension > 0

    def test_protocol_requires_max_tokens(
        self, mock_embedding_provider: "MockEmbeddingProvider"
    ) -> None:
        """Provider must have max_tokens property."""
        assert hasattr(mock_embedding_provider, "max_tokens")
        assert isinstance(mock_embedding_provider.max_tokens, int)
        assert mock_embedding_provider.max_tokens > 0

    def test_protocol_requires_embed_method(
        self, mock_embedding_provider: "MockEmbeddingProvider", sample_texts: list[str]
    ) -> None:
        """Provider must have embed method that returns list of vectors."""
        assert hasattr(mock_embedding_provider, "embed")
        assert callable(mock_embedding_provider.embed)

        embeddings = mock_embedding_provider.embed(sample_texts)
        assert isinstance(embeddings, list)
        assert len(embeddings) == len(sample_texts)

    def test_protocol_requires_embed_query_method(
        self, mock_embedding_provider: "MockEmbeddingProvider"
    ) -> None:
        """Provider must have embed_query method that returns single vector."""
        assert hasattr(mock_embedding_provider, "embed_query")
        assert callable(mock_embedding_provider.embed_query)

        query = "test query"
        embedding = mock_embedding_provider.embed_query(query)
        assert isinstance(embedding, np.ndarray)


class TestMockEmbeddingProvider:
    """Test the MockEmbeddingProvider implementation."""

    def test_embed_returns_correct_dimension(
        self, mock_embedding_provider: "MockEmbeddingProvider", sample_texts: list[str]
    ) -> None:
        """Embeddings should have the configured dimension."""
        embeddings = mock_embedding_provider.embed(sample_texts)

        for embedding in embeddings:
            assert embedding.shape == (mock_embedding_provider.dimension,)
            assert embedding.dtype == np.float32

    def test_embed_returns_normalized_vectors(
        self, mock_embedding_provider: "MockEmbeddingProvider", sample_texts: list[str]
    ) -> None:
        """Embeddings should be L2-normalized (unit length)."""
        embeddings = mock_embedding_provider.embed(sample_texts)

        for embedding in embeddings:
            norm = np.linalg.norm(embedding)
            assert np.isclose(norm, 1.0, atol=1e-6)

    def test_embed_is_deterministic_for_same_text(
        self, mock_embedding_provider: "MockEmbeddingProvider"
    ) -> None:
        """Same text should produce same embedding (when deterministic=True)."""
        text = "This is a test sentence."

        embedding1 = mock_embedding_provider.embed([text])[0]
        embedding2 = mock_embedding_provider.embed([text])[0]

        np.testing.assert_array_equal(embedding1, embedding2)

    def test_embed_produces_different_embeddings_for_different_texts(
        self, mock_embedding_provider: "MockEmbeddingProvider"
    ) -> None:
        """Different texts should produce different embeddings."""
        texts = ["First sentence.", "Second sentence."]
        embeddings = mock_embedding_provider.embed(texts)

        # Embeddings should not be equal
        assert not np.allclose(embeddings[0], embeddings[1])

    def test_embed_empty_list(
        self, mock_embedding_provider: "MockEmbeddingProvider"
    ) -> None:
        """Embedding empty list should return empty list."""
        embeddings = mock_embedding_provider.embed([])
        assert embeddings == []

    def test_embed_query_returns_same_as_embed_single(
        self, mock_embedding_provider: "MockEmbeddingProvider"
    ) -> None:
        """embed_query should be consistent with embed for single text."""
        query = "test query"

        query_embedding = mock_embedding_provider.embed_query(query)
        batch_embedding = mock_embedding_provider.embed([query])[0]

        np.testing.assert_array_equal(query_embedding, batch_embedding)

    def test_call_count_tracking(
        self, mock_embedding_provider: "MockEmbeddingProvider", sample_texts: list[str]
    ) -> None:
        """Provider should track number of embed calls."""
        assert mock_embedding_provider.call_count == 0

        mock_embedding_provider.embed(sample_texts)
        assert mock_embedding_provider.call_count == 1

        mock_embedding_provider.embed(sample_texts[:2])
        assert mock_embedding_provider.call_count == 2

    @pytest.mark.asyncio
    async def test_embed_async(
        self, mock_embedding_provider: "MockEmbeddingProvider", sample_texts: list[str]
    ) -> None:
        """Async embed should return same results as sync."""
        sync_embeddings = mock_embedding_provider.embed(sample_texts)
        async_embeddings = await mock_embedding_provider.embed_async(sample_texts)

        assert len(async_embeddings) == len(sync_embeddings)
        for sync_emb, async_emb in zip(sync_embeddings, async_embeddings):
            np.testing.assert_array_equal(sync_emb, async_emb)


class TestSentenceTransformerProvider:
    """Tests for SentenceTransformerProvider.

    These tests require sentence-transformers to be installed.
    They are skipped if the dependency is not available.
    """

    @pytest.fixture
    def sentence_transformer_provider(self, default_embedding_config: EmbeddingConfig):
        """Create a SentenceTransformerProvider for testing."""
        # Check if sentence-transformers is available first
        try:
            import sentence_transformers  # noqa: F401
        except ImportError:
            pytest.skip("sentence-transformers not installed")

        from calibre_semantic.providers.embeddings.sentence_transformers import (
            SentenceTransformerProvider,
        )
        return SentenceTransformerProvider(default_embedding_config)

    def test_implements_protocol(self, sentence_transformer_provider) -> None:
        """SentenceTransformerProvider should implement EmbeddingProvider protocol."""
        assert isinstance(sentence_transformer_provider, EmbeddingProvider)

    def test_model_id_includes_model_name(
        self, sentence_transformer_provider, default_embedding_config: EmbeddingConfig
    ) -> None:
        """Model ID should include the model name."""
        assert default_embedding_config.model in sentence_transformer_provider.model_id

    def test_dimension_matches_model(self, sentence_transformer_provider) -> None:
        """Dimension should match the actual model dimension."""
        # all-MiniLM-L6-v2 produces 384-dimensional vectors
        assert sentence_transformer_provider.dimension == 384

    def test_embed_single_text(self, sentence_transformer_provider) -> None:
        """Should embed a single text correctly."""
        texts = ["This is a test sentence."]
        embeddings = sentence_transformer_provider.embed(texts)

        assert len(embeddings) == 1
        assert embeddings[0].shape == (384,)
        assert embeddings[0].dtype == np.float32

    def test_embed_multiple_texts(
        self, sentence_transformer_provider, sample_texts: list[str]
    ) -> None:
        """Should embed multiple texts correctly."""
        embeddings = sentence_transformer_provider.embed(sample_texts)

        assert len(embeddings) == len(sample_texts)
        for emb in embeddings:
            assert emb.shape == (384,)
            assert emb.dtype == np.float32

    def test_embeddings_are_normalized(self, sentence_transformer_provider) -> None:
        """Embeddings should be L2-normalized."""
        texts = ["Test sentence for normalization check."]
        embeddings = sentence_transformer_provider.embed(texts)

        norm = np.linalg.norm(embeddings[0])
        assert np.isclose(norm, 1.0, atol=1e-5)

    def test_similar_texts_have_high_similarity(
        self, sentence_transformer_provider
    ) -> None:
        """Semantically similar texts should have high cosine similarity."""
        texts = [
            "The cat sat on the mat.",
            "A cat is sitting on a rug.",
            "The stock market crashed yesterday.",
        ]
        embeddings = sentence_transformer_provider.embed(texts)

        # Cosine similarity (embeddings are normalized, so dot product = cosine sim)
        sim_0_1 = np.dot(embeddings[0], embeddings[1])
        sim_0_2 = np.dot(embeddings[0], embeddings[2])

        # Similar sentences should have higher similarity
        assert sim_0_1 > sim_0_2
        assert sim_0_1 > 0.5  # Should be fairly high

    def test_embed_empty_list(self, sentence_transformer_provider) -> None:
        """Embedding empty list should return empty list."""
        embeddings = sentence_transformer_provider.embed([])
        assert embeddings == []

    def test_embed_query(self, sentence_transformer_provider) -> None:
        """embed_query should return valid embedding."""
        query = "What is semantic search?"
        embedding = sentence_transformer_provider.embed_query(query)

        assert embedding.shape == (384,)
        assert embedding.dtype == np.float32
        norm = np.linalg.norm(embedding)
        assert np.isclose(norm, 1.0, atol=1e-5)

    @pytest.mark.asyncio
    async def test_embed_async(
        self, sentence_transformer_provider, sample_texts: list[str]
    ) -> None:
        """Async embed should work correctly."""
        embeddings = await sentence_transformer_provider.embed_async(sample_texts)

        assert len(embeddings) == len(sample_texts)
        for emb in embeddings:
            assert emb.shape == (384,)

    def test_batching_produces_same_results(
        self, sentence_transformer_provider, sample_texts: list[str]
    ) -> None:
        """Batching should not affect embedding results."""
        # Get embeddings in one batch
        all_at_once = sentence_transformer_provider.embed(sample_texts)

        # Get embeddings one at a time
        one_at_a_time = [
            sentence_transformer_provider.embed([text])[0]
            for text in sample_texts
        ]

        for all_emb, single_emb in zip(all_at_once, one_at_a_time):
            np.testing.assert_array_almost_equal(all_emb, single_emb, decimal=5)

    def test_handles_long_text(self, sentence_transformer_provider) -> None:
        """Should handle text longer than max_tokens by truncating."""
        # Create a very long text
        long_text = "word " * 1000  # Way more than 512 tokens

        # Should not raise an error
        embeddings = sentence_transformer_provider.embed([long_text])
        assert len(embeddings) == 1
        assert embeddings[0].shape == (384,)

    def test_handles_unicode(self, sentence_transformer_provider) -> None:
        """Should handle Unicode text correctly."""
        texts = [
            "日本語のテスト",  # Japanese
            "Тест на русском",  # Russian
            "Test with émojis 🎉📚",  # Emojis
        ]
        embeddings = sentence_transformer_provider.embed(texts)

        assert len(embeddings) == 3
        for emb in embeddings:
            assert emb.shape == (384,)


class TestEmbeddingProviderFactory:
    """Tests for the embedding provider factory function."""

    def test_create_sentence_transformer_provider(
        self, default_embedding_config: EmbeddingConfig
    ) -> None:
        """Factory should create SentenceTransformerProvider for correct config."""
        # Check if sentence-transformers is available first
        try:
            import sentence_transformers  # noqa: F401
        except ImportError:
            pytest.skip("sentence-transformers not installed")

        from calibre_semantic.core.embeddings import create_embedding_provider

        provider = create_embedding_provider(default_embedding_config)
        assert isinstance(provider, EmbeddingProvider)
        assert "all-MiniLM-L6-v2" in provider.model_id

    def test_create_unknown_provider_raises(self) -> None:
        """Factory should raise ValueError for unknown provider."""
        from calibre_semantic.core.embeddings import create_embedding_provider

        config = EmbeddingConfig(provider="unknown-provider")

        with pytest.raises(ValueError, match="Unknown embedding provider"):
            create_embedding_provider(config)
