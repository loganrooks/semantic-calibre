"""Library integration for semantic search.

This module provides the API for integrating semantic search into Calibre's
main library interface. It handles:

- Hybrid queries: metadata filtering in Calibre DB + semantic search in ChromaDB
- Metadata filter building from UI to Calibre query syntax
- Background indexing for bulk operations
- Profile management for library-wide search

Key ADRs:
- ADR-006: Hybrid Metadata Filtering
- ADR-007: Library UI Integration
- ADR-008: Background Indexing Architecture

Usage in Calibre library:

    from calibre_semantic.library import (
        LibrarySearchEngine,
        MetadataFilterBuilder,
        IndexingJob,
    )

    # Build a hybrid search
    engine = LibrarySearchEngine(db=calibre_db)

    # Create metadata filter
    filter_builder = MetadataFilterBuilder()
    filter_builder.add_authors(["John Smith"])
    filter_builder.add_tags(["philosophy", "ethics"])

    # Search with both metadata and semantic filtering
    results = engine.search(
        query="meaning of consciousness",
        metadata_filter=filter_builder,
        profile_id="default",
    )
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable, Iterator, Protocol, Sequence

if TYPE_CHECKING:
    from calibre_semantic.core.types import BookIdentifier, EmbeddingProfile, TextChunk
    from calibre_semantic.search import SemanticSearchEngine

logger = logging.getLogger(__name__)


# =============================================================================
# Enums and Constants
# =============================================================================

class IndexStatus(Enum):
    """Status of a book's semantic index."""
    NOT_INDEXED = "not_indexed"
    INDEXING = "indexing"
    COMPLETE = "complete"
    FAILED = "failed"


DEFAULT_LIBRARY_PROFILE = "library-default"


# =============================================================================
# Metadata Filter Building (ADR-006)
# =============================================================================

@dataclass
class MetadataFilter:
    """A single metadata filter condition.

    Attributes:
        field: The Calibre field name (e.g., "authors", "tags", "#tradition")
        operator: The comparison operator (":", "=", ">", "<", etc.)
        values: The values to match
        negate: If True, negate the condition with NOT
    """
    field: str
    operator: str = ":"  # Calibre default is contains
    values: list[str] = field(default_factory=list)
    negate: bool = False

    def to_query(self) -> str:
        """Convert to Calibre search query syntax.

        Examples:
            authors:"John Smith"
            tags:philosophy
            NOT #tradition:continental
        """
        if not self.values:
            return ""

        # Build the query parts
        parts = []
        for value in self.values:
            # Quote values with spaces
            if " " in value:
                value = f'"{value}"'
            parts.append(f"{self.field}{self.operator}{value}")

        # Join with OR for multiple values
        if len(parts) > 1:
            query = "(" + " OR ".join(parts) + ")"
        else:
            query = parts[0]

        # Apply negation
        if self.negate:
            query = f"NOT {query}"

        return query


class MetadataFilterBuilder:
    """Builder for constructing Calibre metadata search queries.

    This class helps build complex metadata filters that can be combined
    with semantic search per ADR-006 (Hybrid Metadata Filtering).

    Example:
        builder = MetadataFilterBuilder()
        builder.add_authors(["John Smith", "Jane Doe"])
        builder.add_tags(["philosophy"])
        builder.add_custom("#tradition", ["continental"])

        query = builder.build()
        # Result: '(authors:"John Smith" OR authors:"Jane Doe") AND tags:philosophy AND #tradition:continental'
    """

    def __init__(self) -> None:
        self._filters: list[MetadataFilter] = []

    def add_filter(self, filter: MetadataFilter) -> "MetadataFilterBuilder":
        """Add a raw metadata filter."""
        self._filters.append(filter)
        return self

    def add_authors(
        self,
        authors: list[str],
        operator: str = ":",
        negate: bool = False,
    ) -> "MetadataFilterBuilder":
        """Add an author filter.

        Args:
            authors: List of author names to match
            operator: ":" for contains, "=" for exact match
            negate: If True, exclude these authors
        """
        if authors:
            self._filters.append(MetadataFilter(
                field="authors",
                operator=operator,
                values=authors,
                negate=negate,
            ))
        return self

    def add_tags(
        self,
        tags: list[str],
        operator: str = ":",
        negate: bool = False,
    ) -> "MetadataFilterBuilder":
        """Add a tag filter."""
        if tags:
            self._filters.append(MetadataFilter(
                field="tags",
                operator=operator,
                values=tags,
                negate=negate,
            ))
        return self

    def add_series(
        self,
        series: list[str],
        operator: str = ":",
        negate: bool = False,
    ) -> "MetadataFilterBuilder":
        """Add a series filter."""
        if series:
            self._filters.append(MetadataFilter(
                field="series",
                operator=operator,
                values=series,
                negate=negate,
            ))
        return self

    def add_publisher(
        self,
        publishers: list[str],
        operator: str = ":",
        negate: bool = False,
    ) -> "MetadataFilterBuilder":
        """Add a publisher filter."""
        if publishers:
            self._filters.append(MetadataFilter(
                field="publisher",
                operator=operator,
                values=publishers,
                negate=negate,
            ))
        return self

    def add_languages(
        self,
        languages: list[str],
        operator: str = ":",
        negate: bool = False,
    ) -> "MetadataFilterBuilder":
        """Add a language filter."""
        if languages:
            self._filters.append(MetadataFilter(
                field="languages",
                operator=operator,
                values=languages,
                negate=negate,
            ))
        return self

    def add_rating(
        self,
        min_rating: int | None = None,
        max_rating: int | None = None,
    ) -> "MetadataFilterBuilder":
        """Add a rating filter.

        Args:
            min_rating: Minimum rating (1-5)
            max_rating: Maximum rating (1-5)
        """
        if min_rating is not None:
            self._filters.append(MetadataFilter(
                field="rating",
                operator=">=",
                values=[str(min_rating)],
            ))
        if max_rating is not None:
            self._filters.append(MetadataFilter(
                field="rating",
                operator="<=",
                values=[str(max_rating)],
            ))
        return self

    def add_custom(
        self,
        column: str,
        values: list[str],
        operator: str = ":",
        negate: bool = False,
    ) -> "MetadataFilterBuilder":
        """Add a custom column filter.

        Args:
            column: Custom column name (with or without # prefix)
            values: Values to match
            operator: ":" for contains, "=" for exact match
            negate: If True, exclude these values
        """
        if not column.startswith("#"):
            column = f"#{column}"

        if values:
            self._filters.append(MetadataFilter(
                field=column,
                operator=operator,
                values=values,
                negate=negate,
            ))
        return self

    def add_formats(
        self,
        formats: list[str],
        negate: bool = False,
    ) -> "MetadataFilterBuilder":
        """Add a format filter (e.g., EPUB, PDF)."""
        if formats:
            self._filters.append(MetadataFilter(
                field="formats",
                operator=":",
                values=[f.upper() for f in formats],
                negate=negate,
            ))
        return self

    def add_date_range(
        self,
        field: str,
        start: str | None = None,
        end: str | None = None,
    ) -> "MetadataFilterBuilder":
        """Add a date range filter.

        Args:
            field: Date field ("pubdate", "timestamp", "last_modified")
            start: Start date in Calibre format (e.g., "2020-01-01")
            end: End date in Calibre format
        """
        if start:
            self._filters.append(MetadataFilter(
                field=field,
                operator=">",
                values=[start],
            ))
        if end:
            self._filters.append(MetadataFilter(
                field=field,
                operator="<",
                values=[end],
            ))
        return self

    def build(self, join_with: str = " AND ") -> str:
        """Build the final Calibre search query.

        Args:
            join_with: How to join multiple filters (default: " AND ")

        Returns:
            Complete Calibre search query string
        """
        queries = []
        for f in self._filters:
            q = f.to_query()
            if q:
                queries.append(q)

        return join_with.join(queries)

    def is_empty(self) -> bool:
        """Check if no filters have been added."""
        return len(self._filters) == 0

    def clear(self) -> "MetadataFilterBuilder":
        """Remove all filters."""
        self._filters.clear()
        return self


# =============================================================================
# Search Results
# =============================================================================

@dataclass
class LibrarySearchResult:
    """A single result from library semantic search.

    Attributes:
        book_id: Calibre book ID
        title: Book title
        authors: List of author names
        score: Similarity score (0-1)
        chunk_text: The matched text chunk
        chunk_location: Location info (spine_name, offset, etc.)
        metadata: Additional book metadata
    """
    book_id: int
    title: str
    authors: list[str]
    score: float
    chunk_text: str
    chunk_location: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class LibrarySearchResults:
    """Collection of library search results.

    Attributes:
        results: List of search results
        total_matches: Total number of matches before limiting
        query: The semantic query used
        metadata_filter: The metadata filter applied
        profile_id: The embedding profile used
        search_time_ms: Time taken to search in milliseconds
    """
    results: list[LibrarySearchResult]
    total_matches: int
    query: str
    metadata_filter: str
    profile_id: str
    search_time_ms: float = 0.0


# =============================================================================
# Indexing (ADR-008)
# =============================================================================

@dataclass
class IndexingResults:
    """Results from a batch indexing operation.

    Attributes:
        succeeded: List of book IDs successfully indexed
        failed: List of (book_id, error_message) tuples for failures
        skipped: List of book IDs skipped (already indexed)
        total_chunks: Total number of chunks indexed
        duration_seconds: Time taken in seconds
    """
    succeeded: list[int] = field(default_factory=list)
    failed: list[tuple[int, str]] = field(default_factory=list)
    skipped: list[int] = field(default_factory=list)
    total_chunks: int = 0
    duration_seconds: float = 0.0

    @property
    def total_processed(self) -> int:
        """Total number of books processed."""
        return len(self.succeeded) + len(self.failed) + len(self.skipped)

    @property
    def success_rate(self) -> float:
        """Percentage of books successfully indexed."""
        total = len(self.succeeded) + len(self.failed)
        if total == 0:
            return 1.0
        return len(self.succeeded) / total


class CalibreDBProtocol(Protocol):
    """Protocol for Calibre database access.

    This defines the minimum interface needed from Calibre's database
    for semantic search integration.
    """

    def search(
        self,
        query: str,
        restriction: str = "",
        book_ids: set[int] | None = None,
    ) -> set[int]:
        """Search books by Calibre query syntax."""
        ...

    def all_book_ids(self) -> frozenset[int]:
        """Get all book IDs in the library."""
        ...

    def field_for(
        self,
        name: str,
        book_id: int,
        default_value: Any = None,
    ) -> Any:
        """Get a field value for a book."""
        ...

    def format_abspath(
        self,
        book_id: int,
        fmt: str,
    ) -> str | None:
        """Get absolute path to a book format."""
        ...

    def formats(self, book_id: int) -> tuple[str, ...]:
        """Get available formats for a book."""
        ...


class IndexingJob:
    """Background indexing job for Calibre's job system.

    This class follows ADR-008 for background indexing architecture.
    It integrates with Calibre's threaded job system for bulk indexing.

    Usage:
        job = IndexingJob(
            db=calibre_db,
            book_ids=[1, 2, 3],
            profile_id="default",
            engine=semantic_engine,
        )

        # Run in background thread
        results = job.run(progress_callback)
    """

    def __init__(
        self,
        db: CalibreDBProtocol,
        book_ids: list[int],
        profile_id: str,
        engine: "SemanticSearchEngine",
        skip_indexed: bool = True,
    ) -> None:
        """Initialize the indexing job.

        Args:
            db: Calibre database instance
            book_ids: List of book IDs to index
            profile_id: Embedding profile to use
            engine: Semantic search engine
            skip_indexed: If True, skip already-indexed books
        """
        self.db = db
        self.book_ids = book_ids
        self.profile_id = profile_id
        self.engine = engine
        self.skip_indexed = skip_indexed

        self.cancelled = False
        self.results = IndexingResults()

    def run(
        self,
        progress_callback: Callable[[int, int, str], None] | None = None,
    ) -> IndexingResults:
        """Run the indexing job.

        Args:
            progress_callback: Optional callback(current, total, message)

        Returns:
            IndexingResults with success/failure details
        """
        from calibre_semantic.core.types import BookIdentifier
        from calibre_semantic.extraction.epub import EPUBExtractor

        start_time = time.time()
        total = len(self.book_ids)

        for i, book_id in enumerate(self.book_ids):
            if self.cancelled:
                logger.info("Indexing job cancelled")
                break

            # Get book title for progress
            title = self.db.field_for("title", book_id, default_value=f"Book {book_id}")

            if progress_callback:
                progress_callback(i, total, f"Indexing: {title}")

            try:
                # Check if already indexed
                book_identifier = self._create_book_identifier(book_id)
                if self.skip_indexed and self.engine.is_indexed(
                    book_identifier, profile_id=self.profile_id
                ):
                    self.results.skipped.append(book_id)
                    continue

                # Get book format and extract content
                chunks = self._extract_and_index(book_id, book_identifier)

                self.results.succeeded.append(book_id)
                self.results.total_chunks += chunks

            except Exception as e:
                logger.error(f"Failed to index book {book_id}: {e}")
                self.results.failed.append((book_id, str(e)))

        self.results.duration_seconds = time.time() - start_time
        return self.results

    def cancel(self) -> None:
        """Request cancellation of the indexing job."""
        self.cancelled = True

    def _create_book_identifier(self, book_id: int) -> "BookIdentifier":
        """Create a BookIdentifier for a Calibre book."""
        from calibre_semantic.core.types import BookIdentifier

        # Get library ID from database
        library_id = getattr(self.db, "library_id", "default")
        if callable(library_id):
            library_id = library_id()

        # Get preferred format
        formats = self.db.formats(book_id)
        format_type = "EPUB" if "EPUB" in formats else (formats[0] if formats else "UNKNOWN")

        return BookIdentifier(
            library_id=library_id,
            book_id=book_id,
            format=format_type,
        )

    def _extract_and_index(
        self,
        book_id: int,
        book_identifier: "BookIdentifier",
    ) -> int:
        """Extract content from book and index it.

        Returns the number of chunks indexed.
        """
        from calibre_semantic.extraction.epub import EPUBExtractor

        # Get path to EPUB (preferred) or other format
        formats = self.db.formats(book_id)
        book_path = None

        for fmt in ["EPUB", "AZW3", "MOBI", "PDF"]:
            if fmt in formats:
                book_path = self.db.format_abspath(book_id, fmt)
                if book_path:
                    break

        if not book_path:
            raise ValueError(f"No supported format found for book {book_id}")

        # Extract and index
        return self.engine.index_epub(
            epub_path=book_path,
            book_id=book_identifier,
            profile_id=self.profile_id,
            force_reindex=True,  # We already checked skip_indexed
        )


# =============================================================================
# Library Search Engine
# =============================================================================

class LibrarySearchEngine:
    """Semantic search engine for Calibre library.

    This class orchestrates hybrid search combining Calibre's metadata
    filtering with ChromaDB's semantic search, per ADR-006.

    The search process:
    1. Apply metadata filters in Calibre DB to get candidate book IDs
    2. Pass book IDs to ChromaDB for semantic search within those books
    3. Enrich results with book metadata from Calibre

    Usage:
        from calibre_semantic.library import LibrarySearchEngine

        engine = LibrarySearchEngine(db=calibre_db, chromadb_path="/path/to/vectors")

        # Simple semantic search
        results = engine.search("consciousness and perception")

        # Hybrid search with metadata filter
        filter_builder = MetadataFilterBuilder()
        filter_builder.add_authors(["Heidegger", "Husserl"])
        filter_builder.add_tags(["phenomenology"])

        results = engine.search(
            query="being and time",
            metadata_filter=filter_builder,
        )
    """

    def __init__(
        self,
        db: CalibreDBProtocol,
        chromadb_path: str | Path | None = None,
        engine: "SemanticSearchEngine | None" = None,
    ) -> None:
        """Initialize the library search engine.

        Args:
            db: Calibre database instance (Cache.new_api or similar)
            chromadb_path: Path to ChromaDB storage (default: in library folder)
            engine: Optional pre-configured SemanticSearchEngine
        """
        self.db = db
        self._chromadb_path = chromadb_path
        self._engine = engine
        self._engine_initialized = engine is not None

    @property
    def engine(self) -> "SemanticSearchEngine":
        """Get or create the semantic search engine."""
        if not self._engine_initialized:
            self._engine = self._create_engine()
            self._engine_initialized = True
        return self._engine

    def _create_engine(self) -> "SemanticSearchEngine":
        """Create a SemanticSearchEngine configured for library search."""
        from calibre_semantic import SemanticSearchEngine
        from calibre_semantic.core.types import (
            ChunkingConfig,
            EmbeddingConfig,
            SemanticSearchConfig,
            VectorStoreConfig,
        )

        # Determine ChromaDB path
        chromadb_path = self._chromadb_path
        if chromadb_path is None:
            # Default to library folder
            db_path = getattr(self.db, "dbpath", None)
            if callable(db_path):
                db_path = db_path()
            if db_path:
                chromadb_path = Path(db_path).parent / "semantic_search"
            else:
                chromadb_path = Path.home() / ".calibre-semantic"

        chromadb_path = Path(chromadb_path)
        chromadb_path.mkdir(parents=True, exist_ok=True)

        config = SemanticSearchConfig(
            embedding=EmbeddingConfig(
                provider="sentence-transformers",
                model="all-MiniLM-L6-v2",
            ),
            vector_store=VectorStoreConfig(
                backend="chromadb",
                path=str(chromadb_path),
            ),
            chunking=ChunkingConfig(
                strategy="semantic",
                target_size=512,
                overlap=50,
            ),
        )

        return SemanticSearchEngine(config)

    def search(
        self,
        query: str,
        metadata_filter: MetadataFilterBuilder | str | None = None,
        profile_id: str | None = None,
        limit: int = 20,
        min_score: float = 0.3,
    ) -> LibrarySearchResults:
        """Perform hybrid semantic search across the library.

        This implements the ADR-006 hybrid query architecture:
        1. Filter books by metadata in Calibre DB
        2. Semantic search within matching books via ChromaDB

        Args:
            query: Semantic search query
            metadata_filter: MetadataFilterBuilder or raw Calibre query string
            profile_id: Embedding profile to use (default: library-default)
            limit: Maximum number of results
            min_score: Minimum similarity score (0-1)

        Returns:
            LibrarySearchResults with enriched results
        """
        import time
        start_time = time.time()

        profile = profile_id or DEFAULT_LIBRARY_PROFILE

        # Step 1: Get candidate book IDs from metadata filter
        filter_query = ""
        if metadata_filter is not None:
            if isinstance(metadata_filter, MetadataFilterBuilder):
                filter_query = metadata_filter.build()
            else:
                filter_query = metadata_filter

        if filter_query:
            # Use Calibre DB search to get matching book IDs
            matching_books = self.db.search(filter_query)
            logger.debug(f"Metadata filter matched {len(matching_books)} books")
        else:
            # No filter - search all indexed books
            matching_books = None

        # Step 2: Semantic search in ChromaDB
        # Convert Calibre book IDs to BookIdentifiers
        filter_book_ids = None
        if matching_books is not None:
            from calibre_semantic.core.types import BookIdentifier

            library_id = getattr(self.db, "library_id", "default")
            if callable(library_id):
                library_id = library_id()

            filter_book_ids = [
                BookIdentifier(
                    library_id=library_id,
                    book_id=bid,
                    format="EPUB",  # Format doesn't matter for filtering
                )
                for bid in matching_books
            ]

        search_results = self.engine.search(
            query=query,
            limit=limit,
            min_score=min_score,
            filter_book_ids=filter_book_ids,
            profile_id=profile,
        )

        # Step 3: Enrich results with Calibre metadata
        results = []
        for chunk, score in search_results.results:
            book_id = chunk.book_id.book_id

            # Get book metadata from Calibre
            title = self.db.field_for("title", book_id, default_value="Unknown")
            authors = self.db.field_for("authors", book_id, default_value=[])
            if isinstance(authors, str):
                authors = [authors]

            # Build location info
            location = {}
            if chunk.location:
                location = {
                    "spine_name": chunk.location.spine_name,
                    "spine_index": chunk.location.spine_index,
                    "start_offset": chunk.location.start_offset,
                    "end_offset": chunk.location.end_offset,
                }

            results.append(LibrarySearchResult(
                book_id=book_id,
                title=title,
                authors=authors,
                score=score,
                chunk_text=chunk.text,
                chunk_location=location,
            ))

        elapsed_ms = (time.time() - start_time) * 1000

        return LibrarySearchResults(
            results=results,
            total_matches=len(search_results.results),
            query=query,
            metadata_filter=filter_query,
            profile_id=profile,
            search_time_ms=elapsed_ms,
        )

    def index_book(
        self,
        book_id: int,
        profile_id: str | None = None,
        force_reindex: bool = False,
    ) -> int:
        """Index a single book for semantic search.

        Args:
            book_id: Calibre book ID
            profile_id: Embedding profile to use
            force_reindex: If True, re-index even if already indexed

        Returns:
            Number of chunks indexed
        """
        profile = profile_id or DEFAULT_LIBRARY_PROFILE

        job = IndexingJob(
            db=self.db,
            book_ids=[book_id],
            profile_id=profile,
            engine=self.engine,
            skip_indexed=not force_reindex,
        )

        results = job.run()

        if results.failed:
            raise RuntimeError(f"Failed to index book {book_id}: {results.failed[0][1]}")

        return results.total_chunks

    def index_books(
        self,
        book_ids: list[int],
        profile_id: str | None = None,
        progress_callback: Callable[[int, int, str], None] | None = None,
        skip_indexed: bool = True,
    ) -> IndexingResults:
        """Index multiple books for semantic search.

        Args:
            book_ids: List of Calibre book IDs
            profile_id: Embedding profile to use
            progress_callback: Optional callback(current, total, message)
            skip_indexed: If True, skip already-indexed books

        Returns:
            IndexingResults with details of success/failure
        """
        profile = profile_id or DEFAULT_LIBRARY_PROFILE

        job = IndexingJob(
            db=self.db,
            book_ids=book_ids,
            profile_id=profile,
            engine=self.engine,
            skip_indexed=skip_indexed,
        )

        return job.run(progress_callback)

    def is_book_indexed(
        self,
        book_id: int,
        profile_id: str | None = None,
    ) -> bool:
        """Check if a book is indexed for semantic search."""
        from calibre_semantic.core.types import BookIdentifier

        profile = profile_id or DEFAULT_LIBRARY_PROFILE

        library_id = getattr(self.db, "library_id", "default")
        if callable(library_id):
            library_id = library_id()

        book_identifier = BookIdentifier(
            library_id=library_id,
            book_id=book_id,
            format="EPUB",
        )

        return self.engine.is_indexed(book_identifier, profile_id=profile)

    def get_indexed_books(
        self,
        profile_id: str | None = None,
    ) -> list[int]:
        """Get list of book IDs that are indexed.

        Returns:
            List of Calibre book IDs
        """
        profile = profile_id or DEFAULT_LIBRARY_PROFILE

        indexed = self.engine.get_indexed_books(profile_id=profile)

        # Extract Calibre book IDs
        return [bid.book_id for bid in indexed]

    def remove_book(
        self,
        book_id: int,
        profile_id: str | None = None,
    ) -> int:
        """Remove a book from the semantic index.

        Returns:
            Number of chunks removed
        """
        from calibre_semantic.core.types import BookIdentifier

        profile = profile_id or DEFAULT_LIBRARY_PROFILE

        library_id = getattr(self.db, "library_id", "default")
        if callable(library_id):
            library_id = library_id()

        book_identifier = BookIdentifier(
            library_id=library_id,
            book_id=book_id,
            format="EPUB",
        )

        return self.engine.remove_book(book_identifier, profile_id=profile)

    def get_profiles(self) -> list["EmbeddingProfile"]:
        """Get all available embedding profiles."""
        return self.engine.get_profiles()

    def get_stats(
        self,
        profile_id: str | None = None,
    ) -> dict[str, Any]:
        """Get statistics for the semantic index.

        Returns:
            Dict with chunk_count, indexed_books, etc.
        """
        profile = profile_id or DEFAULT_LIBRARY_PROFILE
        return self.engine.get_stats(profile_id=profile)


# =============================================================================
# Convenience Functions
# =============================================================================

def get_library_engine(
    db: CalibreDBProtocol,
    chromadb_path: str | Path | None = None,
) -> LibrarySearchEngine:
    """Get or create a LibrarySearchEngine for a Calibre database.

    This is a convenience function that caches engines per database.

    Args:
        db: Calibre database instance
        chromadb_path: Optional path to ChromaDB storage

    Returns:
        LibrarySearchEngine instance
    """
    # Use a simple cache keyed by database path
    cache_key = getattr(db, "dbpath", id(db))
    if callable(cache_key):
        cache_key = cache_key()

    if not hasattr(get_library_engine, "_cache"):
        get_library_engine._cache = {}

    if cache_key not in get_library_engine._cache:
        get_library_engine._cache[cache_key] = LibrarySearchEngine(
            db=db,
            chromadb_path=chromadb_path,
        )

    return get_library_engine._cache[cache_key]
