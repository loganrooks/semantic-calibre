"""Embedding provider implementations.

Available providers:
- sentence_transformers: Local embedding using sentence-transformers library
- openai: OpenAI API embeddings (requires API key)
- ollama: Local Ollama embeddings
- voyageai: Voyage AI embeddings (requires API key)
- calibre_ai: Adapter for Calibre's built-in AI module (when available)

Each provider implements the EmbeddingProvider protocol defined in
calibre_semantic.core.types.
"""

from calibre_semantic.core.embeddings import (
    create_embedding_provider,
    get_available_providers,
    register_provider,
)
from calibre_semantic.providers.embeddings.calibre_ai import (
    CalibreAIAdapter,
    create_calibre_ai_provider,
    is_calibre_ai_available,
)

__all__ = [
    "create_embedding_provider",
    "get_available_providers",
    "register_provider",
    "CalibreAIAdapter",
    "create_calibre_ai_provider",
    "is_calibre_ai_available",
]
