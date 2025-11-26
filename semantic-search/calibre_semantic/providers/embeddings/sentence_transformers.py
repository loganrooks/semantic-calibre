"""Sentence Transformers embedding provider.

This provider uses the sentence-transformers library for local embedding
generation. It supports a wide variety of models from HuggingFace.

Recommended models:
- all-MiniLM-L6-v2: Fast, good quality, 384 dimensions (default)
- all-mpnet-base-v2: Better quality, 768 dimensions, slower
- paraphrase-multilingual-MiniLM-L12-v2: Multilingual support

Installation:
    pip install calibre-semantic[sentence-transformers]

Usage:
    >>> from calibre_semantic.core.types import EmbeddingConfig
    >>> from calibre_semantic.providers.embeddings.sentence_transformers import (
    ...     SentenceTransformerProvider
    ... )
    >>> config = EmbeddingConfig(
    ...     provider="sentence-transformers",
    ...     model="all-MiniLM-L6-v2",
    ...     device="cpu"
    ... )
    >>> provider = SentenceTransformerProvider(config)
    >>> embeddings = provider.embed(["Hello, world!"])
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Sequence

import numpy as np

from calibre_semantic.core.embeddings import BaseEmbeddingProvider
from calibre_semantic.core.types import EmbeddingConfig, Vector

if TYPE_CHECKING:
    from sentence_transformers import SentenceTransformer

logger = logging.getLogger(__name__)

# Model metadata for common models
# Maps model name to (dimension, max_tokens)
_MODEL_METADATA: dict[str, tuple[int, int]] = {
    "all-MiniLM-L6-v2": (384, 256),
    "all-MiniLM-L12-v2": (384, 256),
    "all-mpnet-base-v2": (768, 384),
    "all-distilroberta-v1": (768, 512),
    "paraphrase-MiniLM-L6-v2": (384, 128),
    "paraphrase-multilingual-MiniLM-L12-v2": (384, 128),
    "multi-qa-MiniLM-L6-cos-v1": (384, 512),
    "multi-qa-mpnet-base-cos-v1": (768, 512),
}


class SentenceTransformerProvider(BaseEmbeddingProvider):
    """Embedding provider using sentence-transformers library.

    This provider runs models locally, requiring no API keys or internet
    connection after initial model download. Models are cached locally
    after first download.

    Attributes:
        config: The embedding configuration
        _model: The loaded SentenceTransformer model (lazy-loaded)

    Device selection:
        - "auto": Automatically select best available (CUDA > MPS > CPU)
        - "cpu": Force CPU usage
        - "cuda": Use NVIDIA GPU
        - "cuda:0", "cuda:1": Specific CUDA device
        - "mps": Use Apple Silicon GPU

    Example:
        >>> config = EmbeddingConfig(
        ...     model="all-MiniLM-L6-v2",
        ...     device="auto"
        ... )
        >>> provider = SentenceTransformerProvider(config)
        >>> emb = provider.embed(["test"])[0]
        >>> emb.shape
        (384,)
    """

    def __init__(self, config: EmbeddingConfig):
        """Initialize the SentenceTransformer provider.

        Args:
            config: Embedding configuration. The model field specifies
                   which sentence-transformers model to use.
        """
        super().__init__(config)
        self._model: "SentenceTransformer | None" = None
        self._dimension: int | None = None
        self._max_tokens: int | None = None

    @property
    def model_id(self) -> str:
        """Return unique model identifier.

        Includes provider name and model name for cache invalidation.
        """
        return f"sentence-transformers:{self.config.model}"

    @property
    def dimension(self) -> int:
        """Return embedding dimension.

        Queries model metadata or loads model to determine dimension.
        """
        if self._dimension is not None:
            return self._dimension

        # Try to get from known metadata
        if self.config.model in _MODEL_METADATA:
            self._dimension = _MODEL_METADATA[self.config.model][0]
            return self._dimension

        # Need to load model to determine
        self._ensure_initialized()
        return self._dimension  # type: ignore

    @property
    def max_tokens(self) -> int:
        """Return maximum tokens.

        Queries model metadata or loads model to determine max tokens.
        """
        if self._max_tokens is not None:
            return self._max_tokens

        # Try to get from known metadata
        if self.config.model in _MODEL_METADATA:
            self._max_tokens = _MODEL_METADATA[self.config.model][1]
            return self._max_tokens

        # Need to load model to determine
        self._ensure_initialized()
        return self._max_tokens  # type: ignore

    def _load_model(self) -> None:
        """Load the SentenceTransformer model.

        Handles device selection and model configuration.

        Raises:
            ImportError: If sentence-transformers is not installed
            OSError: If model cannot be loaded/downloaded
        """
        try:
            from sentence_transformers import SentenceTransformer
        except ImportError as e:
            raise ImportError(
                "sentence-transformers is required for this provider. "
                "Install it with: pip install calibre-semantic[sentence-transformers]"
            ) from e

        device = self._resolve_device()
        logger.info(f"Loading SentenceTransformer model '{self.config.model}' on {device}")

        try:
            self._model = SentenceTransformer(
                self.config.model,
                device=device,
            )
        except Exception as e:
            raise RuntimeError(
                f"Failed to load model '{self.config.model}': {e}"
            ) from e

        # Get actual dimension from model
        self._dimension = self._model.get_sentence_embedding_dimension()

        # Get max sequence length
        self._max_tokens = self._model.max_seq_length

        logger.info(
            f"Model loaded: dimension={self._dimension}, "
            f"max_tokens={self._max_tokens}, device={device}"
        )

    def _resolve_device(self) -> str:
        """Resolve device setting to actual device string.

        Returns:
            Device string for PyTorch ("cpu", "cuda", "mps", etc.)
        """
        device = self.config.device

        if device != "auto":
            return device

        # Auto-detect best device
        try:
            import torch

            if torch.cuda.is_available():
                logger.info("Auto-detected CUDA device")
                return "cuda"
            elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
                logger.info("Auto-detected MPS device (Apple Silicon)")
                return "mps"
        except ImportError:
            pass

        logger.info("Using CPU device")
        return "cpu"

    def _embed_batch(self, texts: Sequence[str]) -> list[Vector]:
        """Embed a batch of texts using the model.

        Args:
            texts: Batch of texts to embed

        Returns:
            List of embedding vectors (not yet normalized)
        """
        if self._model is None:
            raise RuntimeError("Model not loaded. Call _ensure_initialized() first.")

        # sentence-transformers handles conversion to numpy
        embeddings = self._model.encode(
            list(texts),
            convert_to_numpy=True,
            show_progress_bar=False,
            normalize_embeddings=False,  # We normalize in base class
        )

        # Ensure float32 and return as list
        if isinstance(embeddings, np.ndarray):
            embeddings = embeddings.astype(np.float32)
            return [embeddings[i] for i in range(len(embeddings))]

        return [np.array(emb, dtype=np.float32) for emb in embeddings]

    def embed_query(self, query: str) -> Vector:
        """Generate embedding for a search query.

        SentenceTransformers uses symmetric embeddings by default,
        so queries and documents use the same embedding function.
        Some models (e.g., multi-qa-*) are asymmetric and handle
        this internally.

        Args:
            query: The search query text

        Returns:
            Query embedding vector
        """
        # For most sentence-transformers models, query = document embedding
        # Asymmetric models handle the distinction internally
        return self.embed([query])[0]


def get_recommended_models() -> dict[str, dict[str, Any]]:
    """Get information about recommended models.

    Returns:
        Dict mapping model names to metadata including dimension,
        description, and use case recommendations.
    """
    return {
        "all-MiniLM-L6-v2": {
            "dimension": 384,
            "max_tokens": 256,
            "size_mb": 80,
            "description": "Good balance of speed and quality. Recommended default.",
            "use_cases": ["general", "semantic-search"],
        },
        "all-mpnet-base-v2": {
            "dimension": 768,
            "max_tokens": 384,
            "size_mb": 420,
            "description": "Higher quality but slower. Good for accuracy-critical use.",
            "use_cases": ["semantic-search", "clustering"],
        },
        "paraphrase-multilingual-MiniLM-L12-v2": {
            "dimension": 384,
            "max_tokens": 128,
            "size_mb": 420,
            "description": "Supports 50+ languages. Good for multilingual libraries.",
            "use_cases": ["multilingual", "semantic-search"],
        },
        "multi-qa-MiniLM-L6-cos-v1": {
            "dimension": 384,
            "max_tokens": 512,
            "size_mb": 80,
            "description": "Optimized for question-answering style queries.",
            "use_cases": ["question-answering", "semantic-search"],
        },
    }
