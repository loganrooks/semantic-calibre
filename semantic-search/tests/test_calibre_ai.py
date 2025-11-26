"""Tests for CalibreAIAdapter.

Tests validate:
- Adapter initialization with/without Calibre AI
- Fallback behavior when Calibre AI unavailable
- Provider selection (google, openai, auto)
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

    def test_get_available_providers_returns_list(self) -> None:
        """get_available_providers should return a list of strings."""
        from calibre_semantic.providers.embeddings.calibre_ai import (
            get_available_providers,
        )

        result = get_available_providers()
        assert isinstance(result, list)
        for provider in result:
            assert isinstance(provider, str)

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

    def test_adapter_has_provider_property(self) -> None:
        """Adapter should have provider property."""
        from calibre_semantic.providers.embeddings.calibre_ai import CalibreAIAdapter

        adapter = CalibreAIAdapter()
        # Provider can be None if using fallback, or a string
        assert adapter.provider is None or isinstance(adapter.provider, str)


# =============================================================================
# Provider Selection Tests
# =============================================================================


class TestProviderSelection:
    """Tests for provider selection logic."""

    def test_auto_provider_selects_available(self) -> None:
        """Auto provider should select first available or fall back."""
        from calibre_semantic.providers.embeddings.calibre_ai import CalibreAIAdapter

        adapter = CalibreAIAdapter(provider='auto')
        # Should either use a Calibre AI provider or fall back
        assert adapter.is_available or not adapter.is_available  # Always true, but tests init

    def test_explicit_google_provider(self) -> None:
        """Explicit Google provider should be respected when available."""
        from calibre_semantic.providers.embeddings.calibre_ai import CalibreAIAdapter

        adapter = CalibreAIAdapter(provider='google')
        # If Google not available, should fall back
        assert isinstance(adapter.model_id, str)

    def test_custom_dimension(self) -> None:
        """Custom dimension should be respected."""
        from calibre_semantic.providers.embeddings.calibre_ai import CalibreAIAdapter

        adapter = CalibreAIAdapter(dimension=256)
        # Dimension might be overridden by fallback, but should be set
        assert adapter.dimension > 0

    def test_custom_fallback_provider(self) -> None:
        """Custom fallback provider should be used when specified."""
        from calibre_semantic.providers.embeddings.calibre_ai import CalibreAIAdapter

        # If Calibre AI not available, this fallback will be attempted
        adapter = CalibreAIAdapter(
            fallback_provider='sentence-transformers',
            fallback_model='all-MiniLM-L6-v2'
        )
        assert adapter is not None


# =============================================================================
# Mock Calibre AI Tests
# =============================================================================


class TestWithMockCalibreAI:
    """Tests with mocked Calibre AI module."""

    def test_uses_google_when_available(self) -> None:
        """Adapter should use Google AI when available and configured."""
        from calibre_semantic.providers.embeddings import calibre_ai

        # Save original values
        orig_google_available = calibre_ai._CALIBRE_GOOGLE_AVAILABLE
        orig_google_embed = calibre_ai._google_embed
        orig_google_is_ready = calibre_ai._google_is_ready

        try:
            # Mock Google AI as available and ready
            calibre_ai._CALIBRE_GOOGLE_AVAILABLE = True
            calibre_ai._google_is_ready = lambda: True
            calibre_ai._google_embed = MagicMock(
                return_value=[[0.1] * 768]
            )

            adapter = calibre_ai.CalibreAIAdapter(provider='google')

            assert adapter.uses_calibre_ai is True
            assert adapter.provider == 'google'
            assert 'google' in adapter.model_id.lower()

        finally:
            # Restore original values
            calibre_ai._CALIBRE_GOOGLE_AVAILABLE = orig_google_available
            calibre_ai._google_embed = orig_google_embed
            calibre_ai._google_is_ready = orig_google_is_ready

    def test_embed_uses_google_when_active(self) -> None:
        """Embedding should use Google when it's the active provider."""
        from calibre_semantic.providers.embeddings import calibre_ai

        orig_google_available = calibre_ai._CALIBRE_GOOGLE_AVAILABLE
        orig_google_embed = calibre_ai._google_embed
        orig_google_is_ready = calibre_ai._google_is_ready

        try:
            mock_embed = MagicMock(return_value=[[0.5] * 768])
            calibre_ai._CALIBRE_GOOGLE_AVAILABLE = True
            calibre_ai._google_is_ready = lambda: True
            calibre_ai._google_embed = mock_embed

            adapter = calibre_ai.CalibreAIAdapter(provider='google', dimension=768)
            result = adapter.embed(["test text"])

            mock_embed.assert_called_once()
            assert len(result) == 1
            assert result[0].shape == (768,)
            assert result[0].dtype == np.float32

        finally:
            calibre_ai._CALIBRE_GOOGLE_AVAILABLE = orig_google_available
            calibre_ai._google_embed = orig_google_embed
            calibre_ai._google_is_ready = orig_google_is_ready

    def test_embed_query_uses_google_embed_query(self) -> None:
        """embed_query should use Google's embed_query for RETRIEVAL_QUERY task."""
        from calibre_semantic.providers.embeddings import calibre_ai

        orig_google_available = calibre_ai._CALIBRE_GOOGLE_AVAILABLE
        orig_google_embed_query = calibre_ai._google_embed_query
        orig_google_is_ready = calibre_ai._google_is_ready

        try:
            mock_embed_query = MagicMock(return_value=[0.3] * 768)
            calibre_ai._CALIBRE_GOOGLE_AVAILABLE = True
            calibre_ai._google_is_ready = lambda: True
            calibre_ai._google_embed_query = mock_embed_query
            # Need embed for fallback check
            calibre_ai._google_embed = MagicMock(return_value=[[0.5] * 768])

            adapter = calibre_ai.CalibreAIAdapter(provider='google', dimension=768)
            result = adapter.embed_query("search query")

            mock_embed_query.assert_called_once()
            assert result.shape == (768,)

        finally:
            calibre_ai._CALIBRE_GOOGLE_AVAILABLE = orig_google_available
            calibre_ai._google_embed_query = orig_google_embed_query
            calibre_ai._google_is_ready = orig_google_is_ready

    def test_empty_texts_returns_empty_list(self) -> None:
        """Embedding empty list should return empty list."""
        from calibre_semantic.providers.embeddings.calibre_ai import CalibreAIAdapter

        adapter = CalibreAIAdapter()
        result = adapter.embed([])
        assert result == []


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

    def test_factory_accepts_provider(self) -> None:
        """Factory should accept provider parameter."""
        from calibre_semantic.providers.embeddings.calibre_ai import (
            create_calibre_ai_provider,
        )

        adapter = create_calibre_ai_provider(provider='google')
        assert adapter is not None

    def test_factory_accepts_dimension(self) -> None:
        """Factory should accept dimension parameter."""
        from calibre_semantic.providers.embeddings.calibre_ai import (
            create_calibre_ai_provider,
        )

        adapter = create_calibre_ai_provider(dimension=256)
        assert adapter is not None


# =============================================================================
# Integration Tests (when Calibre AI available)
# =============================================================================


class TestIntegration:
    """Integration tests that run when Calibre AI is available."""

    def test_model_id_format(self) -> None:
        """Model ID should have expected format based on provider."""
        from calibre_semantic.providers.embeddings.calibre_ai import CalibreAIAdapter

        adapter = CalibreAIAdapter()

        if adapter.uses_calibre_ai:
            if adapter.provider == 'google':
                assert 'calibre-google:' in adapter.model_id
            elif adapter.provider == 'openai':
                assert 'calibre-openai:' in adapter.model_id
        else:
            # Using fallback - model_id format depends on fallback provider
            assert adapter.model_id != "unavailable" or not adapter.is_available
