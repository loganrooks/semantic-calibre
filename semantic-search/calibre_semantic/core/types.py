"""Core types and protocols for calibre-semantic.

This module defines the fundamental data structures and interfaces (protocols)
used throughout the library. All components depend on these types, enabling
loose coupling and easy testing through dependency injection.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import TYPE_CHECKING, Any, Protocol, Sequence, runtime_checkable

import numpy as np
from numpy.typing import NDArray

if TYPE_CHECKING:
    pass

# =============================================================================
# Type Aliases
# =============================================================================

Vector = NDArray[np.float32]
"""Embedding vector type - 1D array of float32 values."""


# =============================================================================
# Enums
# =============================================================================


class ChunkType(Enum):
    """Type of content chunk extracted from a book."""

    PARAGRAPH = "paragraph"
    CHAPTER = "chapter"
    SECTION = "section"
    PAGE = "page"
    SENTENCE = "sentence"


class IndexStrategy(Enum):
    """Vector index strategy for search.

    Different strategies have different trade-offs:
    - FLAT: Exact search, O(n), best for <50k vectors
    - HNSW: Approximate, O(log n), good for 50k-10M vectors
    - IVF: Approximate with clustering, good for >1M vectors
    """

    FLAT = "flat"
    HNSW = "hnsw"
    IVF = "ivf"


class IndexStatus(Enum):
    """Status of a book's indexing in a profile."""

    PENDING = "pending"
    INDEXING = "indexing"
    COMPLETE = "complete"
    FAILED = "failed"
    STALE = "stale"  # Book modified after indexing


# =============================================================================
# Core Value Types
# =============================================================================


@dataclass(frozen=True)
class BookIdentifier:
    """Unique identifier for a book across libraries.

    This immutable identifier uniquely identifies a specific format of a book
    within a specific Calibre library. It's used as the primary key for
    tracking which books have been indexed.

    Attributes:
        library_id: UUID of the Calibre library
        book_id: Calibre's internal book ID within the library
        format: Book format (e.g., "EPUB", "PDF", "MOBI")
    """

    library_id: str
    book_id: int
    format: str

    def __str__(self) -> str:
        """Return string representation for serialization."""
        return f"{self.library_id}:{self.book_id}:{self.format}"

    @classmethod
    def from_string(cls, s: str) -> BookIdentifier:
        """Create from string representation.

        Args:
            s: String in format "library_id:book_id:format"

        Returns:
            BookIdentifier instance

        Raises:
            ValueError: If string format is invalid
        """
        parts = s.split(":")
        if len(parts) != 3:
            raise ValueError(f"Invalid BookIdentifier string: {s}")
        return cls(parts[0], int(parts[1]), parts[2])


@dataclass(frozen=True)
class ChunkLocation:
    """Location of a text chunk within a book for navigation.

    Stores enough information to navigate back to the exact location
    of a search result within the e-book viewer.

    Attributes:
        spine_index: Index in EPUB spine or page number for PDF
        spine_name: Spine item filename (e.g., "chapter1.xhtml")
        start_offset: Character offset from start of spine item
        end_offset: Character offset for end of chunk
        cfi: Optional EPUB CFI for precise navigation
    """

    spine_index: int
    spine_name: str
    start_offset: int
    end_offset: int
    cfi: str | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "spine_index": self.spine_index,
            "spine_name": self.spine_name,
            "start_offset": self.start_offset,
            "end_offset": self.end_offset,
            "cfi": self.cfi,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ChunkLocation:
        """Create from dictionary."""
        return cls(
            spine_index=data["spine_index"],
            spine_name=data["spine_name"],
            start_offset=data["start_offset"],
            end_offset=data["end_offset"],
            cfi=data.get("cfi"),
        )


@dataclass
class TextChunk:
    """A chunk of text from a book with location metadata.

    Represents a searchable unit of text extracted from a book.
    Each chunk is small enough to be meaningfully embedded but large
    enough to contain useful context.

    Attributes:
        id: Unique chunk identifier (deterministic hash)
        book_id: Source book identifier
        text: The actual text content
        location: Where in the book this chunk is located
        chunk_type: What kind of content boundary this represents
        metadata: Additional metadata (e.g., heading level)
        chapter_title: Title of containing chapter (if known)
        section_title: Title of containing section (if known)
    """

    id: str
    book_id: BookIdentifier
    text: str
    location: ChunkLocation
    chunk_type: ChunkType
    metadata: dict[str, Any] = field(default_factory=dict)
    chapter_title: str | None = None
    section_title: str | None = None


@dataclass
class EmbeddedChunk:
    """A text chunk with its computed embedding vector.

    Attributes:
        chunk: The source text chunk
        embedding: The embedding vector
        model_id: Identifier of the model that generated this embedding
    """

    chunk: TextChunk
    embedding: Vector
    model_id: str


@dataclass
class SearchResult:
    """A single semantic search result.

    Attributes:
        chunk: The matching text chunk
        score: Similarity score (0-1, higher is more similar)
        highlights: List of (start, end) character offsets for highlighting
    """

    chunk: TextChunk
    score: float
    highlights: list[tuple[int, int]] = field(default_factory=list)


@dataclass
class SearchResults:
    """Collection of search results with metadata.

    Attributes:
        query: The original search query
        results: List of search results, ordered by relevance
        total_searched: Total number of chunks searched
        search_time_ms: Search duration in milliseconds
        model_id: Embedding model used for this search
    """

    query: str
    results: list[SearchResult]
    total_searched: int
    search_time_ms: float
    model_id: str


@dataclass
class BookMetadata:
    """Book metadata from Calibre.

    Attributes:
        book_id: Unique book identifier
        title: Book title
        authors: List of author names
        series: Series name (if part of a series)
        series_index: Position in series
        tags: List of tags/categories
        language: ISO language code
        publisher: Publisher name
        publication_date: Publication date string
        description: Book description/summary
        file_path: Path to the book file
    """

    book_id: BookIdentifier
    title: str
    authors: list[str]
    series: str | None = None
    series_index: float | None = None
    tags: list[str] = field(default_factory=list)
    language: str | None = None
    publisher: str | None = None
    publication_date: str | None = None
    description: str | None = None
    file_path: Path | None = None


@dataclass
class IndexingProgress:
    """Progress information for indexing operations.

    Used to report progress during book indexing, enabling
    UI updates and cancellation.

    Attributes:
        book_id: The book being indexed
        status: Current status string
        progress: Progress from 0.0 to 1.0
        message: Human-readable status message
        error: Error message if status is "error"
    """

    book_id: BookIdentifier
    status: str  # "pending", "extracting", "chunking", "embedding", "complete", "error"
    progress: float
    message: str | None = None
    error: str | None = None


# =============================================================================
# Configuration Types
# =============================================================================


@dataclass
class EmbeddingConfig:
    """Configuration for embedding provider.

    Attributes:
        provider: Provider name (e.g., "sentence-transformers", "openai")
        model: Model name or path
        api_key: API key for cloud providers
        api_base: Custom API endpoint URL
        batch_size: Number of texts to embed at once
        device: Compute device ("cpu", "cuda", "mps", "auto")
    """

    provider: str = "sentence-transformers"
    model: str = "all-MiniLM-L6-v2"
    api_key: str | None = None
    api_base: str | None = None
    batch_size: int = 32
    device: str = "auto"


@dataclass
class VectorStoreConfig:
    """Configuration for vector store.

    Attributes:
        backend: Backend name (e.g., "sqlite-vec", "chromadb")
        path: Storage path (None for in-memory)
        options: Backend-specific options
    """

    backend: str = "sqlite-vec"
    path: Path | None = None
    options: dict[str, Any] = field(default_factory=dict)


@dataclass
class ChunkingConfig:
    """Configuration for text chunking.

    Attributes:
        strategy: Chunking strategy name
        target_size: Target chunk size in characters
        overlap: Number of characters to overlap between chunks
        respect_boundaries: Whether to respect paragraph/sentence boundaries
    """

    strategy: str = "semantic"
    target_size: int = 512
    overlap: int = 64
    respect_boundaries: bool = True


@dataclass
class SemanticSearchConfig:
    """Main configuration for semantic search.

    This is the top-level configuration object that combines all
    sub-configurations and search settings.

    Attributes:
        embedding: Embedding provider configuration
        vector_store: Vector store configuration
        chunking: Chunking strategy configuration
        default_result_limit: Default max results to return
        min_similarity_score: Minimum score threshold
        index_on_add: Whether to auto-index new books
        background_indexing: Whether to index in background
    """

    embedding: EmbeddingConfig = field(default_factory=EmbeddingConfig)
    vector_store: VectorStoreConfig = field(default_factory=VectorStoreConfig)
    chunking: ChunkingConfig = field(default_factory=ChunkingConfig)
    default_result_limit: int = 20
    min_similarity_score: float = 0.3
    index_on_add: bool = False  # ADR-002: On-demand indexing by default
    background_indexing: bool = True

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SemanticSearchConfig:
        """Create configuration from dictionary.

        Args:
            data: Configuration dictionary

        Returns:
            SemanticSearchConfig instance
        """
        embedding_data = data.get("embedding", {})
        vector_store_data = data.get("vector_store", {})
        chunking_data = data.get("chunking", {})

        # Handle path conversion for vector_store
        if "path" in vector_store_data and vector_store_data["path"] is not None:
            vector_store_data["path"] = Path(vector_store_data["path"])

        return cls(
            embedding=EmbeddingConfig(**embedding_data),
            vector_store=VectorStoreConfig(**vector_store_data),
            chunking=ChunkingConfig(**chunking_data),
            default_result_limit=data.get("default_result_limit", 20),
            min_similarity_score=data.get("min_similarity_score", 0.3),
            index_on_add=data.get("index_on_add", False),  # ADR-002
            background_indexing=data.get("background_indexing", True),
        )

    def to_dict(self) -> dict[str, Any]:
        """Convert configuration to dictionary for serialization."""
        return {
            "embedding": {
                "provider": self.embedding.provider,
                "model": self.embedding.model,
                "api_key": self.embedding.api_key,
                "api_base": self.embedding.api_base,
                "batch_size": self.embedding.batch_size,
                "device": self.embedding.device,
            },
            "vector_store": {
                "backend": self.vector_store.backend,
                "path": str(self.vector_store.path) if self.vector_store.path else None,
                "options": self.vector_store.options,
            },
            "chunking": {
                "strategy": self.chunking.strategy,
                "target_size": self.chunking.target_size,
                "overlap": self.chunking.overlap,
                "respect_boundaries": self.chunking.respect_boundaries,
            },
            "default_result_limit": self.default_result_limit,
            "min_similarity_score": self.min_similarity_score,
            "index_on_add": self.index_on_add,
            "background_indexing": self.background_indexing,
        }


# =============================================================================
# Embedding Profiles
# =============================================================================


@dataclass
class EmbeddingProfile:
    """A named embedding configuration for indexing books.

    Profiles allow users to create multiple embedding configurations
    with different providers, models, and dimensions. Books can be
    indexed into one or more profiles.

    Important: Embeddings from different profiles are NOT compatible.
    You cannot search across profiles with different providers/models
    because they exist in different vector spaces.

    Attributes:
        id: Unique identifier (e.g., "philosophy-gemini-768")
        name: Human-readable name (e.g., "Philosophy Research")
        provider: Embedding provider ("google", "openai", "sentence-transformers")
        model: Model identifier
        dimension: Embedding vector dimension
        index_strategy: Vector index strategy (flat, hnsw, ivf)
        index_options: Strategy-specific configuration
        created_at: When this profile was created
        description: Optional description of the profile's purpose

    Example:
        >>> profile = EmbeddingProfile(
        ...     id="research-gemini",
        ...     name="Research Collection",
        ...     provider="google",
        ...     model="models/text-embedding-004",
        ...     dimension=768,
        ... )
    """

    id: str
    name: str
    provider: str
    model: str
    dimension: int
    index_strategy: IndexStrategy = IndexStrategy.FLAT
    index_options: dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    description: str | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "provider": self.provider,
            "model": self.model,
            "dimension": self.dimension,
            "index_strategy": self.index_strategy.value,
            "index_options": self.index_options,
            "created_at": self.created_at.isoformat(),
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> EmbeddingProfile:
        """Create from dictionary."""
        return cls(
            id=data["id"],
            name=data["name"],
            provider=data["provider"],
            model=data["model"],
            dimension=data["dimension"],
            index_strategy=IndexStrategy(data.get("index_strategy", "flat")),
            index_options=data.get("index_options", {}),
            created_at=datetime.fromisoformat(data["created_at"])
            if isinstance(data.get("created_at"), str)
            else data.get("created_at", datetime.now()),
            description=data.get("description"),
        )

    @property
    def model_id(self) -> str:
        """Get unique model identifier for cache invalidation."""
        return f"{self.provider}:{self.model}:{self.dimension}"


@dataclass
class BookIndexStatus:
    """Tracks indexing status of a book within a profile.

    Each book can be indexed in multiple profiles. This dataclass
    tracks the status of each book-profile combination.

    Attributes:
        book_id: The book being tracked
        profile_id: The embedding profile
        status: Current indexing status
        indexed_at: When indexing completed (if complete)
        chunk_count: Number of chunks indexed
        error_message: Error details if status is FAILED
    """

    book_id: BookIdentifier
    profile_id: str
    status: IndexStatus = IndexStatus.PENDING
    indexed_at: datetime | None = None
    chunk_count: int = 0
    error_message: str | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "book_id": str(self.book_id),
            "profile_id": self.profile_id,
            "status": self.status.value,
            "indexed_at": self.indexed_at.isoformat() if self.indexed_at else None,
            "chunk_count": self.chunk_count,
            "error_message": self.error_message,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> BookIndexStatus:
        """Create from dictionary."""
        book_id = data["book_id"]
        if isinstance(book_id, str):
            book_id = BookIdentifier.from_string(book_id)

        return cls(
            book_id=book_id,
            profile_id=data["profile_id"],
            status=IndexStatus(data.get("status", "pending")),
            indexed_at=datetime.fromisoformat(data["indexed_at"])
            if data.get("indexed_at")
            else None,
            chunk_count=data.get("chunk_count", 0),
            error_message=data.get("error_message"),
        )


# =============================================================================
# Protocols (Interfaces)
# =============================================================================


@runtime_checkable
class EmbeddingProvider(Protocol):
    """Protocol for embedding generation providers.

    This interface defines what any embedding provider must implement.
    Using a Protocol enables static type checking while allowing any
    implementation that provides the required methods.

    The @runtime_checkable decorator allows isinstance() checks.
    """

    @property
    def model_id(self) -> str:
        """Unique identifier for this model.

        Used for cache invalidation - if model changes, embeddings
        need to be regenerated.
        """
        ...

    @property
    def dimension(self) -> int:
        """Dimension of embedding vectors produced by this model."""
        ...

    @property
    def max_tokens(self) -> int:
        """Maximum tokens this model can embed at once."""
        ...

    def embed(self, texts: Sequence[str]) -> list[Vector]:
        """Generate embeddings for multiple texts.

        Args:
            texts: Sequence of text strings to embed

        Returns:
            List of embedding vectors, one per input text
        """
        ...

    async def embed_async(self, texts: Sequence[str]) -> list[Vector]:
        """Generate embeddings for multiple texts asynchronously.

        Args:
            texts: Sequence of text strings to embed

        Returns:
            List of embedding vectors, one per input text
        """
        ...

    def embed_query(self, query: str) -> Vector:
        """Generate embedding for a search query.

        Some models use different embeddings for queries vs documents.
        This method allows providers to handle that distinction.

        Args:
            query: The search query text

        Returns:
            Query embedding vector
        """
        ...


@runtime_checkable
class VectorStore(Protocol):
    """Protocol for vector storage backends.

    Defines the interface for storing and searching embedding vectors.
    Implementations might use SQLite-vec, ChromaDB, FAISS, etc.

    Profile Support:
        All data operations accept an optional profile_id parameter for
        namespace isolation. This allows storing embeddings from different
        models or configurations in the same database without conflicts.
    """

    def add(
        self,
        chunks: Sequence[EmbeddedChunk],
        profile_id: str | None = None,
    ) -> None:
        """Add embedded chunks to the store.

        Args:
            chunks: Sequence of embedded chunks to store
            profile_id: Profile namespace (uses default if None)
        """
        ...

    def remove(
        self,
        chunk_ids: Sequence[str],
        profile_id: str | None = None,
    ) -> None:
        """Remove chunks by ID.

        Args:
            chunk_ids: Sequence of chunk IDs to remove
            profile_id: Profile namespace (uses default if None)
        """
        ...

    def remove_book(
        self,
        book_id: BookIdentifier,
        profile_id: str | None = None,
    ) -> int:
        """Remove all chunks for a book from a profile.

        Args:
            book_id: The book whose chunks should be removed
            profile_id: Profile namespace (uses default if None)

        Returns:
            Number of chunks removed
        """
        ...

    def search(
        self,
        query_embedding: Vector,
        limit: int = 10,
        profile_id: str | None = None,
        filter_book_ids: Sequence[BookIdentifier] | None = None,
        filter_libraries: Sequence[str] | None = None,
        min_score: float = 0.0,
    ) -> list[tuple[TextChunk, float]]:
        """Search for similar chunks within a profile.

        Args:
            query_embedding: The query vector to search for
            limit: Maximum number of results
            profile_id: Profile namespace to search (uses default if None)
            filter_book_ids: Optional filter to specific books
            filter_libraries: Optional filter to specific libraries
            min_score: Minimum similarity score threshold

        Returns:
            List of (chunk, score) tuples, ordered by descending score
        """
        ...

    def get_indexed_books(
        self,
        profile_id: str | None = None,
    ) -> set[BookIdentifier]:
        """Get set of all indexed book identifiers in a profile.

        Args:
            profile_id: Profile namespace (uses default if None)

        Returns:
            Set of BookIdentifier for all indexed books
        """
        ...

    def get_chunk_count(
        self,
        book_id: BookIdentifier | None = None,
        profile_id: str | None = None,
    ) -> int:
        """Get total chunk count in a profile.

        Args:
            book_id: Optional filter to count chunks for specific book
            profile_id: Profile namespace (uses default if None)

        Returns:
            Number of chunks in store
        """
        ...

    def get_model_id(self) -> str | None:
        """Get the model ID used for embeddings in this store.

        Returns:
            Model ID string or None if not set
        """
        ...

    def set_model_id(self, model_id: str) -> None:
        """Set the model ID for embeddings in this store.

        Args:
            model_id: The model identifier string
        """
        ...

    def clear(self, profile_id: str | None = None) -> None:
        """Remove all data from the store or a specific profile.

        Args:
            profile_id: If provided, only clear that profile.
                       If None, clear entire store.
        """
        ...

    def get_profiles(self) -> list[str]:
        """Get list of all profiles with data in the store.

        Returns:
            List of profile IDs.
        """
        ...
