"""Calibre AI Adapter for embedding generation.

This module provides an adapter that uses Calibre's built-in AI module
for embedding generation when available. This allows calibre-semantic
to leverage Calibre's AI configuration without duplication.

When Calibre's AI module is not available, this adapter falls back to
using the configured embedding provider from calibre-semantic's own
provider system.

Usage:
    >>> from calibre_semantic.providers.embeddings.calibre_ai import CalibreAIAdapter
    >>> # Will use Calibre AI if available, otherwise falls back
    >>> adapter = CalibreAIAdapter()
    >>> if adapter.is_available:
    ...     embeddings = adapter.embed(["text1", "text2"])
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Sequence

import numpy as np

from calibre_semantic.core.types import EmbeddingConfig, Vector

if TYPE_CHECKING:
    from calibre_semantic.core.embeddings import BaseEmbeddingProvider

logger = logging.getLogger(__name__)

# Try to import Calibre's AI module
_CALIBRE_AI_AVAILABLE = False
_calibre_ai: dict[str, Any] | None = None

try:
    # This import path may change as Calibre's AI module evolves
    # Currently checking for potential locations
    from calibre.gui2.ai import get_embedding_model  # type: ignore
    _CALIBRE_AI_AVAILABLE = True
    _calibre_ai = {"get_embedding_model": get_embedding_model}
except ImportError:
    pass

if not _CALIBRE_AI_AVAILABLE:
    try:
        # Alternative import path
        from calibre.ai import EmbeddingProvider as CalibreEmbedding  # type: ignore
        _CALIBRE_AI_AVAILABLE = True
        _calibre_ai = {"EmbeddingProvider": CalibreEmbedding}
    except ImportError:
        pass


def is_calibre_ai_available() -> bool:
    """Check if Calibre's AI module is available.

    Returns:
        True if Calibre AI embedding support is available
    """
    return _CALIBRE_AI_AVAILABLE


class CalibreAIAdapter:
    """Adapter to use Calibre's built-in AI embedding capabilities.

    This adapter bridges between calibre-semantic's EmbeddingProvider
    protocol and Calibre's AI module. When Calibre AI is not available,
    it falls back to a specified fallback provider.

    Note: This class implements the EmbeddingProvider protocol but does NOT
    inherit from BaseEmbeddingProvider because it delegates to either
    Calibre AI or a fallback provider, rather than implementing embedding
    directly.

    Attributes:
        _calibre_model: The Calibre AI embedding model (if available)
        _fallback: Fallback embedding provider
        _model_id_value: Identifier for the embedding model
        _dimension_value: Embedding vector dimension
    """

    def __init__(
        self,
        config: EmbeddingConfig | None = None,
        fallback_provider: str = "sentence-transformers",
        fallback_model: str = "all-MiniLM-L6-v2",
    ):
        """Initialize the Calibre AI adapter.

        Args:
            config: Optional embedding configuration
            fallback_provider: Provider to use if Calibre AI unavailable
            fallback_model: Model to use with fallback provider
        """
        self._config = config or EmbeddingConfig()
        self._fallback_provider_name = fallback_provider
        self._fallback_model = fallback_model
        self._calibre_model: Any = None
        self._fallback: "BaseEmbeddingProvider | None" = None
        self._dimension_value: int = 384
        self._model_id_value: str = "unavailable"
        self._max_tokens_value: int = 512

        if _CALIBRE_AI_AVAILABLE and _calibre_ai is not None:
            try:
                self._init_calibre_ai()
            except Exception as e:
                logger.warning(f"Failed to initialize Calibre AI: {e}")
                self._init_fallback()
        else:
            logger.info(
                "Calibre AI not available, using fallback provider: "
                f"{fallback_provider}/{fallback_model}"
            )
            self._init_fallback()

    def _init_calibre_ai(self) -> None:
        """Initialize using Calibre's AI module."""
        if _calibre_ai is None:
            return

        if "get_embedding_model" in _calibre_ai:
            self._calibre_model = _calibre_ai["get_embedding_model"]()
            self._model_id_value = getattr(
                self._calibre_model, "model_id", "calibre-ai-default"
            )
            self._dimension_value = getattr(self._calibre_model, "dimension", 384)
            self._max_tokens_value = getattr(self._calibre_model, "max_tokens", 512)
        elif "EmbeddingProvider" in _calibre_ai:
            self._calibre_model = _calibre_ai["EmbeddingProvider"]()
            self._model_id_value = getattr(
                self._calibre_model, "model_id", "calibre-ai-default"
            )
            self._dimension_value = getattr(self._calibre_model, "dimension", 384)
            self._max_tokens_value = getattr(self._calibre_model, "max_tokens", 512)

        logger.info(f"Initialized Calibre AI adapter with model: {self._model_id_value}")

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
            self._model_id_value = self._fallback.model_id
            self._dimension_value = self._fallback.dimension
            self._max_tokens_value = self._fallback.max_tokens
        except ImportError as e:
            # If fallback also fails, we need to provide sensible defaults
            logger.warning(f"Fallback provider not available: {e}")
            self._model_id_value = "unavailable"
            self._dimension_value = 384
            self._max_tokens_value = 512

    @property
    def is_available(self) -> bool:
        """Check if any embedding capability is available."""
        return self._calibre_model is not None or self._fallback is not None

    @property
    def uses_calibre_ai(self) -> bool:
        """Check if using Calibre's AI module."""
        return self._calibre_model is not None

    @property
    def model_id(self) -> str:
        """Get the model identifier."""
        return self._model_id_value

    @property
    def dimension(self) -> int:
        """Get the embedding dimension."""
        return self._dimension_value

    @property
    def max_tokens(self) -> int:
        """Get max tokens supported."""
        return self._max_tokens_value

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

        if self._calibre_model is not None:
            return self._embed_with_calibre(texts)
        elif self._fallback is not None:
            return self._fallback.embed(texts)
        else:
            raise RuntimeError(
                "No embedding capability available. Install sentence-transformers "
                "or configure a cloud provider."
            )

    def _embed_with_calibre(self, texts: Sequence[str]) -> list[Vector]:
        """Generate embeddings using Calibre AI.

        Args:
            texts: Texts to embed

        Returns:
            List of embedding vectors
        """
        # Calibre AI should have an embed method
        # The exact API depends on how Calibre implements it
        if hasattr(self._calibre_model, "embed"):
            embeddings = self._calibre_model.embed(texts)
        elif hasattr(self._calibre_model, "encode"):
            embeddings = self._calibre_model.encode(texts)
        elif hasattr(self._calibre_model, "get_embeddings"):
            embeddings = self._calibre_model.get_embeddings(texts)
        else:
            raise RuntimeError(
                "Calibre AI model does not have a recognized embedding method"
            )

        # Ensure correct format
        result = []
        for emb in embeddings:
            if isinstance(emb, np.ndarray):
                result.append(emb.astype(np.float32))
            else:
                result.append(np.array(emb, dtype=np.float32))

        return result

    async def embed_async(self, texts: Sequence[str]) -> list[Vector]:
        """Generate embeddings asynchronously.

        Args:
            texts: Texts to embed

        Returns:
            List of embedding vectors
        """
        # Check if Calibre AI has async support
        if self._calibre_model is not None:
            if hasattr(self._calibre_model, "embed_async"):
                return await self._calibre_model.embed_async(texts)

        # Fall back to sync
        return self.embed(texts)

    def embed_query(self, query: str) -> Vector:
        """Generate embedding for a search query.

        Args:
            query: The search query

        Returns:
            Query embedding vector
        """
        if self._calibre_model is not None:
            if hasattr(self._calibre_model, "embed_query"):
                result = self._calibre_model.embed_query(query)
                if isinstance(result, np.ndarray):
                    return result.astype(np.float32)
                return np.array(result, dtype=np.float32)

        # Default: use regular embed
        embeddings = self.embed([query])
        return embeddings[0]


def create_calibre_ai_provider(
    config: EmbeddingConfig | None = None,
) -> CalibreAIAdapter:
    """Factory function to create a Calibre AI adapter.

    Args:
        config: Optional embedding configuration

    Returns:
        CalibreAIAdapter instance
    """
    return CalibreAIAdapter(config=config)
