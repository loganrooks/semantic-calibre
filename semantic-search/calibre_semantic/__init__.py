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

# Viewer integration (lazy import to avoid dependency issues)
def search_viewer_book(*args, **kwargs):
    """Search a book semantically - see viewer module for details."""
    from calibre_semantic.viewer import search_viewer_book as _search
    return _search(*args, **kwargs)


def is_book_indexed(*args, **kwargs):
    """Check if a book is indexed - see viewer module for details."""
    from calibre_semantic.viewer import is_book_indexed as _check
    return _check(*args, **kwargs)


def index_book_for_viewer(*args, **kwargs):
    """Index a book for the viewer - see viewer module for details."""
    from calibre_semantic.viewer import index_book_for_viewer as _index
    return _index(*args, **kwargs)


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
    # Viewer integration
    "search_viewer_book",
    "is_book_indexed",
    "index_book_for_viewer",
]
