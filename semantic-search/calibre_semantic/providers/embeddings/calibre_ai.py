"""Calibre AI Adapter for embedding generation.

This module provides an adapter that uses Calibre's built-in AI module
for embedding generation when available. This allows calibre-semantic
to leverage Calibre's AI configuration without duplication.

When Calibre's AI module is not available, this adapter falls back to
using the configured embedding provider from calibre-semantic's own
provider system.

Supported Calibre AI providers:
- Google (Gemini text-embedding-004)
- OpenAI (text-embedding-3-small/large) - when implemented

Usage:
    >>> from calibre_semantic.providers.embeddings.calibre_ai import CalibreAIAdapter
    >>> # Will use Calibre AI if available, otherwise falls back
    >>> adapter = CalibreAIAdapter()
    >>> if adapter.is_available:
    ...     embeddings = adapter.embed(["text1", "text2"])
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Callable, Sequence

import numpy as np

from calibre_semantic.core.types import EmbeddingConfig, Vector

if TYPE_CHECKING:
    from calibre_semantic.core.embeddings import BaseEmbeddingProvider

logger = logging.getLogger(__name__)

# =============================================================================
# Calibre AI Module Detection
# =============================================================================

_CALIBRE_GOOGLE_AVAILABLE = False
_CALIBRE_OPENAI_AVAILABLE = False
_google_embed: Callable[..., list[list[float]]] | None = None
_google_embed_query: Callable[..., list[float]] | None = None
_google_is_ready: Callable[[], bool] | None = None
_openai_embed: Callable[..., list[list[float]]] | None = None
_openai_is_ready: Callable[[], bool] | None = None

# Try to import Google AI embedding
try:
    from calibre.ai.google.backend import (
        DEFAULT_EMBEDDING_DIMENSION,
        DEFAULT_EMBEDDING_MODEL,
        embed as google_embed,
        embed_query as google_embed_query,
        is_ready_for_use as google_is_ready,
    )
    _CALIBRE_GOOGLE_AVAILABLE = True
    _google_embed = google_embed
    _google_embed_query = google_embed_query
    _google_is_ready = google_is_ready
    logger.debug("Calibre Google AI embedding available")
except ImportError:
    DEFAULT_EMBEDDING_MODEL = 'models/text-embedding-004'
    DEFAULT_EMBEDDING_DIMENSION = 768
    logger.debug("Calibre Google AI not available")

# Try to import OpenAI embedding (when implemented)
try:
    from calibre.ai.openai.backend import (
        embed as openai_embed,
        is_ready_for_use as openai_is_ready,
    )
    _CALIBRE_OPENAI_AVAILABLE = True
    _openai_embed = openai_embed
    _openai_is_ready = openai_is_ready
    logger.debug("Calibre OpenAI embedding available")
except ImportError:
    logger.debug("Calibre OpenAI embedding not available")


def is_calibre_ai_available() -> bool:
    """Check if any Calibre AI embedding provider is available and configured.

    Returns:
        True if at least one Calibre AI provider is ready for use
    """
    if _CALIBRE_GOOGLE_AVAILABLE and _google_is_ready and _google_is_ready():
        return True
    if _CALIBRE_OPENAI_AVAILABLE and _openai_is_ready and _openai_is_ready():
        return True
    return False


def get_available_providers() -> list[str]:
    """Get list of available Calibre AI embedding providers.

    Returns:
        List of provider names that are available and configured
    """
    providers = []
    if _CALIBRE_GOOGLE_AVAILABLE and _google_is_ready and _google_is_ready():
        providers.append('google')
    if _CALIBRE_OPENAI_AVAILABLE and _openai_is_ready and _openai_is_ready():
        providers.append('openai')
    return providers


class CalibreAIAdapter:
    """Adapter to use Calibre's built-in AI embedding capabilities.

    This adapter bridges between calibre-semantic's EmbeddingProvider
    protocol and Calibre's AI module. When Calibre AI is not available,
    it falls back to a specified fallback provider.

    Attributes:
        provider: The Calibre AI provider being used ('google', 'openai', or None)
        dimension: Embedding vector dimension
        model: The model being used

    Example:
        >>> adapter = CalibreAIAdapter(provider='google', dimension=768)
        >>> if adapter.is_available:
        ...     embeddings = adapter.embed(["Hello world"])
    """

    def __init__(
        self,
        config: EmbeddingConfig | None = None,
        provider: str = 'auto',
        model: str = '',
        dimension: int = 768,
        fallback_provider: str = "sentence-transformers",
        fallback_model: str = "all-MiniLM-L6-v2",
    ):
        """Initialize the Calibre AI adapter.

        Args:
            config: Optional embedding configuration (overrides other params)
            provider: Calibre AI provider to use ('google', 'openai', 'auto')
            model: Model name (provider-specific, uses default if empty)
            dimension: Embedding dimension (256, 768, 3072 for Gemini)
            fallback_provider: Provider to use if Calibre AI unavailable
            fallback_model: Model to use with fallback provider
        """
        self._config = config or EmbeddingConfig()
        self._requested_provider = provider
        self._model = model
        self._dimension = dimension
        self._fallback_provider_name = fallback_provider
        self._fallback_model = fallback_model

        self._active_provider: str | None = None
        self._fallback: "BaseEmbeddingProvider | None" = None

        # Try to initialize Calibre AI
        self._init_calibre_ai()

        # Fall back if Calibre AI not available
        if self._active_provider is None:
            self._init_fallback()

    def _init_calibre_ai(self) -> None:
        """Initialize using Calibre's AI module."""
        provider = self._requested_provider

        # Auto-select provider
        if provider == 'auto':
            available = get_available_providers()
            if available:
                provider = available[0]  # Prefer first available
                logger.info(f"Auto-selected Calibre AI provider: {provider}")
            else:
                logger.info("No Calibre AI providers available")
                return

        # Initialize specific provider
        if provider == 'google':
            if _CALIBRE_GOOGLE_AVAILABLE and _google_is_ready and _google_is_ready():
                self._active_provider = 'google'
                self._model = self._model or DEFAULT_EMBEDDING_MODEL
                logger.info(
                    f"Initialized Calibre Google AI: model={self._model}, "
                    f"dimension={self._dimension}"
                )
            else:
                logger.warning("Google AI requested but not available/configured")

        elif provider == 'openai':
            if _CALIBRE_OPENAI_AVAILABLE and _openai_is_ready and _openai_is_ready():
                self._active_provider = 'openai'
                self._model = self._model or 'text-embedding-3-small'
                logger.info(f"Initialized Calibre OpenAI: model={self._model}")
            else:
                logger.warning("OpenAI requested but not available/configured")

    def _init_fallback(self) -> None:
        """Initialize the fallback provider."""
        from calibre_semantic.core.embeddings import create_embedding_provider

        fallback_config = EmbeddingConfig(
            provider=self._fallback_provider_name,
            model=self._fallback_model,
            device=self._config.device,
            batch_size=self._config.batch_size,
        )

        try:
            self._fallback = create_embedding_provider(fallback_config)
            self._dimension = self._fallback.dimension
            logger.info(
                f"Using fallback provider: {self._fallback_provider_name}/"
                f"{self._fallback_model}"
            )
        except ImportError as e:
            logger.warning(f"Fallback provider not available: {e}")

    @property
    def is_available(self) -> bool:
        """Check if any embedding capability is available."""
        return self._active_provider is not None or self._fallback is not None

    @property
    def uses_calibre_ai(self) -> bool:
        """Check if using Calibre's AI module."""
        return self._active_provider is not None

    @property
    def provider(self) -> str | None:
        """Get the active Calibre AI provider name."""
        return self._active_provider

    @property
    def model_id(self) -> str:
        """Get the model identifier."""
        if self._active_provider == 'google':
            return f"calibre-google:{self._model}:{self._dimension}"
        elif self._active_provider == 'openai':
            return f"calibre-openai:{self._model}"
        elif self._fallback:
            return self._fallback.model_id
        return "unavailable"

    @property
    def dimension(self) -> int:
        """Get the embedding dimension."""
        if self._fallback and not self._active_provider:
            return self._fallback.dimension
        return self._dimension

    @property
    def max_tokens(self) -> int:
        """Get max tokens supported."""
        if self._active_provider == 'google':
            return 2048  # Gemini embedding models
        elif self._active_provider == 'openai':
            return 8191  # OpenAI embedding models
        elif self._fallback:
            return self._fallback.max_tokens
        return 512

    def embed(self, texts: Sequence[str]) -> list[Vector]:
        """Generate embeddings for texts.

        Uses Calibre AI if available, otherwise falls back.

        Args:
            texts: Sequence of texts to embed

        Returns:
            List of embedding vectors

        Raises:
            RuntimeError: If no embedding capability is available
        """
        if not texts:
            return []

        texts_list = list(texts)

        if self._active_provider == 'google' and _google_embed:
            return self._embed_with_google(texts_list)
        elif self._active_provider == 'openai' and _openai_embed:
            return self._embed_with_openai(texts_list)
        elif self._fallback is not None:
            return self._fallback.embed(texts_list)
        else:
            raise RuntimeError(
                "No embedding capability available. Configure Calibre AI "
                "(Preferences → Ask AI) or install sentence-transformers."
            )

    def _embed_with_google(self, texts: list[str]) -> list[Vector]:
        """Generate embeddings using Calibre's Google AI.

        Args:
            texts: Texts to embed

        Returns:
            List of embedding vectors
        """
        if not _google_embed:
            raise RuntimeError("Google embed function not available")

        embeddings = _google_embed(
            texts,
            model=self._model,
            dimensions=self._dimension,
            task_type='RETRIEVAL_DOCUMENT',
        )

        return [np.array(emb, dtype=np.float32) for emb in embeddings]

    def _embed_with_openai(self, texts: list[str]) -> list[Vector]:
        """Generate embeddings using Calibre's OpenAI.

        Args:
            texts: Texts to embed

        Returns:
            List of embedding vectors
        """
        if not _openai_embed:
            raise RuntimeError("OpenAI embed function not available")

        embeddings = _openai_embed(texts, model=self._model)
        return [np.array(emb, dtype=np.float32) for emb in embeddings]

    async def embed_async(self, texts: Sequence[str]) -> list[Vector]:
        """Generate embeddings asynchronously.

        Currently runs synchronously - async support may be added later.

        Args:
            texts: Texts to embed

        Returns:
            List of embedding vectors
        """
        # TODO: Implement true async when Calibre AI supports it
        return self.embed(texts)

    def embed_query(self, query: str) -> Vector:
        """Generate embedding for a search query.

        Uses RETRIEVAL_QUERY task type for Google, which is optimized
        for search queries.

        Args:
            query: The search query

        Returns:
            Query embedding vector
        """
        if self._active_provider == 'google' and _google_embed_query:
            result = _google_embed_query(
                query,
                model=self._model,
                dimensions=self._dimension,
            )
            return np.array(result, dtype=np.float32)

        # For OpenAI and fallback, use regular embed
        embeddings = self.embed([query])
        return embeddings[0]


def create_calibre_ai_provider(
    config: EmbeddingConfig | None = None,
    provider: str = 'auto',
    dimension: int = 768,
) -> CalibreAIAdapter:
    """Factory function to create a Calibre AI adapter.

    Args:
        config: Optional embedding configuration
        provider: Provider to use ('google', 'openai', 'auto')
        dimension: Embedding dimension

    Returns:
        CalibreAIAdapter instance
    """
    return CalibreAIAdapter(config=config, provider=provider, dimension=dimension)
