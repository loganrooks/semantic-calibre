"""Embedding provider implementations.

Available providers:
- sentence_transformers: Local embedding using sentence-transformers library
- openai: OpenAI API embeddings (requires API key)
- ollama: Local Ollama embeddings
- voyageai: Voyage AI embeddings (requires API key)

Each provider implements the EmbeddingProvider protocol defined in
calibre_semantic.core.types.
"""

from calibre_semantic.core.embeddings import (
    create_embedding_provider,
    get_available_providers,
    register_provider,
)

__all__ = [
    "create_embedding_provider",
    "get_available_providers",
    "register_provider",
]
