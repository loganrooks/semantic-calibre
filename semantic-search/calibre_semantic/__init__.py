"""
calibre-semantic: Semantic search library for Calibre e-book manager.

This library provides semantic search capabilities for e-book collections,
supporting cross-library search, within-book search, and MCP server integration.
"""

__version__ = "0.1.0"

from calibre_semantic.core.types import (
    BookIdentifier,
    BookMetadata,
    ChunkLocation,
    ChunkType,
    EmbeddedChunk,
    EmbeddingConfig,
    IndexingProgress,
    SearchResult,
    SearchResults,
    SemanticSearchConfig,
    TextChunk,
)
from calibre_semantic.search import SemanticSearchEngine

__all__ = [
    "__version__",
    "BookIdentifier",
    "BookMetadata",
    "ChunkLocation",
    "ChunkType",
    "EmbeddedChunk",
    "EmbeddingConfig",
    "IndexingProgress",
    "SearchResult",
    "SearchResults",
    "SemanticSearchConfig",
    "SemanticSearchEngine",
    "TextChunk",
]
