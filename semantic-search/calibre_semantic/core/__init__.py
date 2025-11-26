"""Core modules for calibre-semantic."""

from calibre_semantic.core.types import (
    BookIdentifier,
    BookMetadata,
    ChunkLocation,
    ChunkType,
    ChunkingConfig,
    EmbeddedChunk,
    EmbeddingConfig,
    EmbeddingProvider,
    IndexingProgress,
    SearchResult,
    SearchResults,
    SemanticSearchConfig,
    TextChunk,
    Vector,
    VectorStore,
    VectorStoreConfig,
)
from calibre_semantic.core.embeddings import create_embedding_provider
from calibre_semantic.core.vectordb import create_vector_store

__all__ = [
    # Types
    "BookIdentifier",
    "BookMetadata",
    "ChunkLocation",
    "ChunkType",
    "ChunkingConfig",
    "EmbeddedChunk",
    "EmbeddingConfig",
    "EmbeddingProvider",
    "IndexingProgress",
    "SearchResult",
    "SearchResults",
    "SemanticSearchConfig",
    "TextChunk",
    "Vector",
    "VectorStore",
    "VectorStoreConfig",
    # Factories
    "create_embedding_provider",
    "create_vector_store",
]
