"""Viewer integration for semantic search.

This module provides the convenience API for integrating semantic search
into Calibre's e-book viewer. It handles:

- Book indexing on-demand
- Converting semantic search results to viewer-compatible format
- Profile management for the viewer context

Usage in Calibre viewer (search.py):

    from calibre_semantic.viewer import search_viewer_book, is_book_indexed

    # Check if book needs indexing
    if not is_book_indexed(book_path):
        # Prompt user to index first
        ...

    # Search
    results = search_viewer_book(
        query="meaning of life",
        book_path=book_path,
        spine_items=spine_items,
    )

    # Convert to Calibre SearchResult format
    for result in results:
        yield result.before, result.text, result.after, result.offset
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Iterator, Sequence

if TYPE_CHECKING:
    from calibre_semantic.core.types import BookIdentifier, TextChunk

logger = logging.getLogger(__name__)

# Default profile for viewer (can be overridden)
DEFAULT_VIEWER_PROFILE = "viewer-default"


@dataclass
class ViewerSearchResult:
    """Search result formatted for Calibre viewer integration.

    Attributes:
        before: Context text before the match
        text: The matched text
        after: Context text after the match
        offset: Character offset in the spine item's text
        spine_idx: Index into the book's spine
        spine_name: Name of the spine item (file name)
        score: Similarity score (0-1)
        chunk_text: Full chunk text that matched
    """

    before: str
    text: str
    after: str
    offset: int
    spine_idx: int
    spine_name: str
    score: float
    chunk_text: str


def _get_default_engine():
    """Get or create the default semantic search engine for the viewer.

    Returns a lazily-initialized engine with sensible defaults for
    viewer-based search (in-memory store, default embedding provider).
    """
    from calibre_semantic import SemanticSearchEngine
    from calibre_semantic.core.types import (
        ChunkingConfig,
        EmbeddingConfig,
        SemanticSearchConfig,
        VectorStoreConfig,
    )

    # Use a shared engine instance
    if not hasattr(_get_default_engine, "_instance"):
        config = SemanticSearchConfig(
            embedding=EmbeddingConfig(
                provider="sentence-transformers",
                model="all-MiniLM-L6-v2",
            ),
            vector_store=VectorStoreConfig(
                backend="memory",  # In-memory for viewer (per-book)
            ),
            chunking=ChunkingConfig(
                strategy="semantic",
                target_size=512,
                overlap=50,
            ),
        )

        try:
            _get_default_engine._instance = SemanticSearchEngine(config)
        except ImportError as e:
            logger.warning(
                f"Could not create semantic search engine: {e}. "
                "Make sure sentence-transformers is installed."
            )
            raise

    return _get_default_engine._instance


def _create_book_id(book_path: str | Path, library_id: str = "viewer") -> "BookIdentifier":
    """Create a BookIdentifier for a viewer book.

    Args:
        book_path: Path to the book file
        library_id: Library identifier (default: "viewer")

    Returns:
        BookIdentifier suitable for indexing
    """
    from calibre_semantic.core.types import BookIdentifier

    path = Path(book_path)

    # Use hash of path as book_id for uniqueness
    book_id = hash(str(path.resolve())) % (10**9)

    # Get format from extension
    format_type = path.suffix.upper().lstrip(".")

    return BookIdentifier(
        library_id=library_id,
        book_id=book_id,
        format=format_type,
    )


def is_book_indexed(
    book_path: str | Path,
    profile_id: str | None = None,
    engine: "SemanticSearchEngine | None" = None,
) -> bool:
    """Check if a book is already indexed for semantic search.

    Args:
        book_path: Path to the book file
        profile_id: Profile to check (default: viewer-default)
        engine: Optional engine instance (uses default if not provided)

    Returns:
        True if the book has been indexed
    """
    if engine is None:
        try:
            engine = _get_default_engine()
        except ImportError:
            return False

    book_id = _create_book_id(book_path)
    profile = profile_id or DEFAULT_VIEWER_PROFILE

    return engine.is_indexed(book_id, profile_id=profile)


def index_book_for_viewer(
    book_path: str | Path,
    spine_items: Sequence[tuple[str, str]],
    profile_id: str | None = None,
    engine: "SemanticSearchEngine | None" = None,
    on_progress: "callable | None" = None,
) -> int:
    """Index a book for semantic search in the viewer.

    Args:
        book_path: Path to the book file
        spine_items: List of (spine_name, text_content) tuples
        profile_id: Profile to use (default: viewer-default)
        engine: Optional engine instance (uses default if not provided)
        on_progress: Optional callback(current, total) for progress updates

    Returns:
        Number of chunks indexed

    Raises:
        ImportError: If required dependencies are not available
    """
    if engine is None:
        engine = _get_default_engine()

    book_id = _create_book_id(book_path)
    profile = profile_id or DEFAULT_VIEWER_PROFILE

    # Convert spine_items to the format expected by index_book_content
    # Each item is (spine_name, text_content)
    formatted_items = [
        (name, content) for name, content in spine_items
    ]

    total_chunks = engine.index_book_content(
        book_id=book_id,
        spine_items=formatted_items,
        profile_id=profile,
        force_reindex=False,
    )

    logger.info(f"Indexed {total_chunks} chunks for {book_path}")
    return total_chunks


def search_viewer_book(
    query: str,
    book_path: str | Path,
    spine_items: Sequence[tuple[str, str]] | None = None,
    profile_id: str | None = None,
    engine: "SemanticSearchEngine | None" = None,
    limit: int = 20,
    min_score: float = 0.3,
    ctx_size: int = 75,
    auto_index: bool = True,
) -> list[ViewerSearchResult]:
    """Search a book semantically and return results for the viewer.

    This is the main entry point for semantic search in the Calibre viewer.
    It handles indexing (if needed) and returns results in a format that
    can be easily converted to Calibre's SearchResult.

    Args:
        query: The search query (semantic/meaning-based)
        book_path: Path to the book file
        spine_items: List of (spine_name, text_content) tuples for indexing
                    Required if auto_index is True and book is not indexed
        profile_id: Profile to use (default: viewer-default)
        engine: Optional engine instance (uses default if not provided)
        limit: Maximum number of results to return
        min_score: Minimum similarity score (0-1)
        ctx_size: Size of before/after context in characters
        auto_index: If True and book not indexed, index it first

    Returns:
        List of ViewerSearchResult objects

    Raises:
        ImportError: If required dependencies are not available
        ValueError: If book needs indexing but spine_items not provided
    """
    if engine is None:
        engine = _get_default_engine()

    book_id = _create_book_id(book_path)
    profile = profile_id or DEFAULT_VIEWER_PROFILE

    # Check if book needs indexing
    if not engine.is_indexed(book_id, profile_id=profile):
        if not auto_index:
            logger.warning(f"Book {book_path} is not indexed and auto_index is False")
            return []

        if spine_items is None:
            raise ValueError(
                f"Book {book_path} is not indexed and spine_items not provided. "
                "Either provide spine_items or index the book first."
            )

        logger.info(f"Auto-indexing book: {book_path}")
        index_book_for_viewer(
            book_path=book_path,
            spine_items=spine_items,
            profile_id=profile,
            engine=engine,
        )

    # Perform semantic search
    search_results = engine.search(
        query=query,
        limit=limit,
        min_score=min_score,
        filter_book_ids=[book_id],
        profile_id=profile,
    )

    # Convert to viewer format
    viewer_results = []
    for chunk, score in search_results.results:
        # Extract context around the chunk
        text = chunk.text
        before = ""
        after = ""

        # The chunk IS the matched text for semantic search
        # We use the beginning and end as context
        if len(text) > ctx_size * 2:
            # Long chunk - show beginning and end
            middle_start = ctx_size
            middle_end = len(text) - ctx_size
            before = text[:middle_start]
            matched_text = text[middle_start:middle_end]
            after = text[middle_end:]
        else:
            # Short chunk - show the whole thing
            matched_text = text

        # Get spine index from chunk location
        spine_idx = 0
        spine_name = ""
        offset = 0

        if chunk.location:
            spine_name = chunk.location.spine_index or ""
            # Try to parse spine_idx from location
            if chunk.location.spine_index and chunk.location.spine_index.isdigit():
                spine_idx = int(chunk.location.spine_index)
            offset = chunk.location.char_offset or 0

        viewer_results.append(
            ViewerSearchResult(
                before=before,
                text=matched_text,
                after=after,
                offset=offset,
                spine_idx=spine_idx,
                spine_name=spine_name,
                score=score,
                chunk_text=text,
            )
        )

    return viewer_results


def clear_book_index(
    book_path: str | Path,
    profile_id: str | None = None,
    engine: "SemanticSearchEngine | None" = None,
) -> int:
    """Remove a book's index from semantic search.

    Args:
        book_path: Path to the book file
        profile_id: Profile to clear (default: viewer-default)
        engine: Optional engine instance (uses default if not provided)

    Returns:
        Number of chunks removed
    """
    if engine is None:
        try:
            engine = _get_default_engine()
        except ImportError:
            return 0

    book_id = _create_book_id(book_path)
    profile = profile_id or DEFAULT_VIEWER_PROFILE

    return engine.remove_book(book_id, profile_id=profile)
