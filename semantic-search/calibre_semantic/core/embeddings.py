"""Embedding provider abstractions and factory.

This module provides:
1. BaseEmbeddingProvider - Abstract base class with common functionality
2. create_embedding_provider() - Factory function to instantiate providers

The design follows the Strategy pattern, allowing different embedding
implementations to be swapped without changing client code.
"""

from __future__ import annotations

import asyncio
import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Sequence

import numpy as np

from calibre_semantic.core.types import EmbeddingConfig, Vector

if TYPE_CHECKING:
    from calibre_semantic.core.types import EmbeddingProvider

logger = logging.getLogger(__name__)


class BaseEmbeddingProvider(ABC):
    """Abstract base class for embedding providers.

    Provides common functionality for all embedding providers:
    - Batching with configurable batch size
    - L2 normalization of vectors
    - Async wrapper for sync implementations
    - Logging and error handling

    Subclasses must implement:
    - model_id property
    - dimension property
    - max_tokens property
    - _load_model() method
    - _embed_batch() method

    Example usage:
        class MyProvider(BaseEmbeddingProvider):
            @property
            def model_id(self) -> str:
                return f"my-provider:{self.config.model}"

            @property
            def dimension(self) -> int:
                return 768

            @property
            def max_tokens(self) -> int:
                return 512

            def _load_model(self) -> None:
                self._model = load_my_model(self.config.model)

            def _embed_batch(self, texts: Sequence[str]) -> list[Vector]:
                return self._model.encode(texts)
    """

    def __init__(self, config: EmbeddingConfig):
        """Initialize the embedding provider.

        Args:
            config: Configuration for the embedding provider
        """
        self.config = config
        self._model = None
        self._initialized = False

    def _ensure_initialized(self) -> None:
        """Ensure the model is loaded before use.

        This implements lazy initialization - the model is only loaded
        when first needed, not at construction time.
        """
        if not self._initialized:
            logger.info(f"Loading embedding model: {self.config.model}")
            self._load_model()
            self._initialized = True
            logger.info(
                f"Loaded model {self.model_id} "
                f"(dimension={self.dimension}, max_tokens={self.max_tokens})"
            )

    @property
    @abstractmethod
    def model_id(self) -> str:
        """Unique identifier for this model.

        Should include provider name and model name/version to enable
        cache invalidation when models change.

        Returns:
            String identifier like "sentence-transformers:all-MiniLM-L6-v2"
        """
        pass

    @property
    @abstractmethod
    def dimension(self) -> int:
        """Dimension of embedding vectors produced by this model.

        Returns:
            Integer dimension (e.g., 384, 768, 1536)
        """
        pass

    @property
    @abstractmethod
    def max_tokens(self) -> int:
        """Maximum tokens this model can process at once.

        Returns:
            Maximum token count
        """
        pass

    @abstractmethod
    def _load_model(self) -> None:
        """Load the embedding model.

        Called once on first use. Should set self._model to the loaded model.

        Raises:
            ImportError: If required dependencies are not installed
            RuntimeError: If model loading fails
        """
        pass

    @abstractmethod
    def _embed_batch(self, texts: Sequence[str]) -> list[Vector]:
        """Embed a batch of texts.

        This is the core implementation method that subclasses must provide.
        Called by embed() with pre-batched texts.

        Args:
            texts: Batch of texts to embed (size <= config.batch_size)

        Returns:
            List of embedding vectors, one per input text
        """
        pass

    def embed(self, texts: Sequence[str]) -> list[Vector]:
        """Generate embeddings for multiple texts.

        Handles batching, normalization, and error handling.

        Args:
            texts: Sequence of text strings to embed

        Returns:
            List of L2-normalized embedding vectors

        Example:
            >>> provider = SentenceTransformerProvider(config)
            >>> embeddings = provider.embed(["Hello", "World"])
            >>> len(embeddings)
            2
        """
        if not texts:
            return []

        self._ensure_initialized()

        results: list[Vector] = []
        batch_size = self.config.batch_size

        # Process in batches
        for i in range(0, len(texts), batch_size):
            batch = texts[i : i + batch_size]
            logger.debug(f"Embedding batch {i // batch_size + 1} ({len(batch)} texts)")

            batch_embeddings = self._embed_batch(batch)

            # Normalize embeddings
            normalized = self._normalize(batch_embeddings)
            results.extend(normalized)

        return results

    async def embed_async(self, texts: Sequence[str]) -> list[Vector]:
        """Generate embeddings asynchronously.

        Default implementation runs sync embed() in a thread pool.
        Subclasses can override for true async implementations.

        Args:
            texts: Sequence of text strings to embed

        Returns:
            List of embedding vectors
        """
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self.embed, list(texts))

    def embed_query(self, query: str) -> Vector:
        """Generate embedding for a search query.

        Some models use different embeddings for queries vs documents
        (asymmetric models). Override this method if your model
        requires different handling for queries.

        Args:
            query: The search query text

        Returns:
            Query embedding vector
        """
        return self.embed([query])[0]

    def _normalize(self, vectors: list[Vector]) -> list[Vector]:
        """L2-normalize vectors for cosine similarity.

        Normalized vectors enable cosine similarity via dot product,
        which is more efficient for vector databases.

        Args:
            vectors: List of vectors to normalize

        Returns:
            List of unit-length vectors
        """
        normalized = []
        for vec in vectors:
            norm = np.linalg.norm(vec)
            if norm > 0:
                normalized.append((vec / norm).astype(np.float32))
            else:
                # Handle zero vector edge case
                logger.warning("Encountered zero vector during normalization")
                normalized.append(vec.astype(np.float32))
        return normalized


# =============================================================================
# Provider Registry and Factory
# =============================================================================

# Registry of available providers
# Maps provider name to (module_path, class_name) tuple
_PROVIDER_REGISTRY: dict[str, tuple[str, str]] = {
    "sentence-transformers": (
        "calibre_semantic.providers.embeddings.sentence_transformers",
        "SentenceTransformerProvider",
    ),
    "openai": (
        "calibre_semantic.providers.embeddings.openai",
        "OpenAIProvider",
    ),
    "ollama": (
        "calibre_semantic.providers.embeddings.ollama",
        "OllamaProvider",
    ),
    "voyageai": (
        "calibre_semantic.providers.embeddings.voyageai",
        "VoyageAIProvider",
    ),
}


def register_provider(name: str, module_path: str, class_name: str) -> None:
    """Register a custom embedding provider.

    Allows extending the library with custom providers without
    modifying the core code.

    Args:
        name: Provider name to use in config
        module_path: Full module path (e.g., "mypackage.embeddings")
        class_name: Name of the provider class

    Example:
        >>> register_provider(
        ...     "custom",
        ...     "my_package.embeddings",
        ...     "CustomProvider"
        ... )
        >>> config = EmbeddingConfig(provider="custom")
        >>> provider = create_embedding_provider(config)
    """
    _PROVIDER_REGISTRY[name] = (module_path, class_name)
    logger.info(f"Registered embedding provider: {name}")


def get_available_providers() -> list[str]:
    """Get list of registered provider names.

    Returns:
        List of provider name strings
    """
    return list(_PROVIDER_REGISTRY.keys())


def create_embedding_provider(config: EmbeddingConfig) -> "EmbeddingProvider":
    """Factory function to create embedding provider from configuration.

    Uses dynamic import to only load dependencies when needed.

    Args:
        config: Embedding configuration specifying provider and model

    Returns:
        Configured EmbeddingProvider instance

    Raises:
        ValueError: If provider name is not registered
        ImportError: If provider dependencies are not installed

    Example:
        >>> config = EmbeddingConfig(
        ...     provider="sentence-transformers",
        ...     model="all-MiniLM-L6-v2"
        ... )
        >>> provider = create_embedding_provider(config)
        >>> embeddings = provider.embed(["Hello, world!"])
    """
    if config.provider not in _PROVIDER_REGISTRY:
        available = ", ".join(get_available_providers())
        raise ValueError(
            f"Unknown embedding provider: {config.provider}. "
            f"Available providers: {available}"
        )

    module_path, class_name = _PROVIDER_REGISTRY[config.provider]

    try:
        import importlib

        module = importlib.import_module(module_path)
        provider_class = getattr(module, class_name)
    except ImportError as e:
        raise ImportError(
            f"Failed to import provider '{config.provider}'. "
            f"Make sure the required dependencies are installed. "
            f"Try: pip install calibre-semantic[{config.provider}]\n"
            f"Original error: {e}"
        ) from e
    except AttributeError as e:
        raise ImportError(
            f"Provider class '{class_name}' not found in module '{module_path}'"
        ) from e

    logger.info(f"Creating embedding provider: {config.provider} ({config.model})")
    return provider_class(config)
