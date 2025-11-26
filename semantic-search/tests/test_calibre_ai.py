"""Tests for CalibreAIAdapter.

Tests validate:
- Adapter initialization with/without Calibre AI
- Fallback behavior when Calibre AI unavailable
- Embedding generation through adapter
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch
import numpy as np
import pytest

from calibre_semantic.core.types import EmbeddingConfig


# =============================================================================
# Availability Tests
# =============================================================================


class TestCalibreAIAvailability:
    """Tests for Calibre AI availability detection."""

    def test_is_calibre_ai_available_returns_boolean(self) -> None:
        """is_calibre_ai_available should return a boolean."""
        from calibre_semantic.providers.embeddings.calibre_ai import (
            is_calibre_ai_available,
        )

        result = is_calibre_ai_available()
        assert isinstance(result, bool)

    def test_adapter_reports_availability(self) -> None:
        """Adapter should report whether it's available."""
        from calibre_semantic.providers.embeddings.calibre_ai import CalibreAIAdapter

        adapter = CalibreAIAdapter()
        assert isinstance(adapter.is_available, bool)

    def test_adapter_reports_calibre_ai_usage(self) -> None:
        """Adapter should report whether using Calibre AI."""
        from calibre_semantic.providers.embeddings.calibre_ai import CalibreAIAdapter

        adapter = CalibreAIAdapter()
        assert isinstance(adapter.uses_calibre_ai, bool)


# =============================================================================
# Fallback Behavior Tests
# =============================================================================


class TestFallbackBehavior:
    """Tests for fallback behavior when Calibre AI unavailable."""

    def test_adapter_initializes_without_calibre_ai(self) -> None:
        """Adapter should initialize even without Calibre AI."""
        from calibre_semantic.providers.embeddings.calibre_ai import CalibreAIAdapter

        # This should not raise
        adapter = CalibreAIAdapter()
        assert adapter is not None

    def test_adapter_has_model_id(self) -> None:
        """Adapter should have a model ID."""
        from calibre_semantic.providers.embeddings.calibre_ai import CalibreAIAdapter

        adapter = CalibreAIAdapter()
        assert isinstance(adapter.model_id, str)
        assert len(adapter.model_id) > 0

    def test_adapter_has_dimension(self) -> None:
        """Adapter should have an embedding dimension."""
        from calibre_semantic.providers.embeddings.calibre_ai import CalibreAIAdapter

        adapter = CalibreAIAdapter()
        assert isinstance(adapter.dimension, int)
        assert adapter.dimension > 0

    def test_adapter_has_max_tokens(self) -> None:
        """Adapter should have max_tokens property."""
        from calibre_semantic.providers.embeddings.calibre_ai import CalibreAIAdapter

        adapter = CalibreAIAdapter()
        assert isinstance(adapter.max_tokens, int)
        assert adapter.max_tokens > 0


# =============================================================================
# Mock Calibre AI Tests
# =============================================================================


class TestWithMockCalibreAI:
    """Tests with mocked Calibre AI module."""

    def test_uses_calibre_ai_when_available(self) -> None:
        """Adapter should use Calibre AI when available."""
        from calibre_semantic.providers.embeddings.calibre_ai import CalibreAIAdapter

        # Create mock Calibre AI module
        mock_model = MagicMock()
        mock_model.model_id = "calibre-test-model"
        mock_model.dimension = 768
        mock_model.max_tokens = 1024
        mock_model.embed.return_value = [np.zeros(768, dtype=np.float32)]

        # Create adapter with manually set calibre model (simulating Calibre AI)
        adapter = CalibreAIAdapter.__new__(CalibreAIAdapter)
        adapter._config = EmbeddingConfig()
        adapter._fallback_provider_name = "sentence-transformers"
        adapter._fallback_model = "all-MiniLM-L6-v2"
        adapter._calibre_model = mock_model
        adapter._fallback = None
        adapter._dimension_value = 768
        adapter._model_id_value = "calibre-test-model"
        adapter._max_tokens_value = 1024

        assert adapter.uses_calibre_ai is True
        assert adapter.model_id == "calibre-test-model"
        assert adapter.dimension == 768
        assert adapter.max_tokens == 1024

    def test_embed_uses_calibre_model(self) -> None:
        """Embedding should use Calibre model when available."""
        from calibre_semantic.providers.embeddings.calibre_ai import CalibreAIAdapter

        mock_model = MagicMock()
        mock_model.embed.return_value = [np.ones(384, dtype=np.float32)]

        adapter = CalibreAIAdapter.__new__(CalibreAIAdapter)
        adapter._config = EmbeddingConfig()
        adapter._calibre_model = mock_model
        adapter._fallback = None
        adapter._dimension_value = 384
        adapter._model_id_value = "test"
        adapter._max_tokens_value = 512

        result = adapter.embed(["test text"])

        mock_model.embed.assert_called_once_with(["test text"])
        assert len(result) == 1
        assert result[0].shape == (384,)


# =============================================================================
# Factory Function Tests
# =============================================================================


class TestFactory:
    """Tests for factory function."""

    def test_create_calibre_ai_provider(self) -> None:
        """Factory should create CalibreAIAdapter."""
        from calibre_semantic.providers.embeddings.calibre_ai import (
            CalibreAIAdapter,
            create_calibre_ai_provider,
        )

        adapter = create_calibre_ai_provider()
        assert isinstance(adapter, CalibreAIAdapter)

    def test_factory_accepts_config(self) -> None:
        """Factory should accept configuration."""
        from calibre_semantic.providers.embeddings.calibre_ai import (
            create_calibre_ai_provider,
        )

        config = EmbeddingConfig(device="cpu", batch_size=16)
        adapter = create_calibre_ai_provider(config=config)
        assert adapter is not None
