"""Core types and protocols for calibre-semantic.

This module defines the fundamental data structures and interfaces (protocols)
used throughout the library. All components depend on these types, enabling
loose coupling and easy testing through dependency injection.
"""

from __future__ import annotations

from dataclasses import dataclass, field
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
    index_on_add: bool = True
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
            index_on_add=data.get("index_on_add", True),
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
    """

    def add(self, chunks: Sequence[EmbeddedChunk]) -> None:
        """Add embedded chunks to the store.

        Args:
            chunks: Sequence of embedded chunks to store
        """
        ...

    def remove(self, chunk_ids: Sequence[str]) -> None:
        """Remove chunks by ID.

        Args:
            chunk_ids: Sequence of chunk IDs to remove
        """
        ...

    def remove_book(self, book_id: BookIdentifier) -> int:
        """Remove all chunks for a book.

        Args:
            book_id: The book whose chunks should be removed

        Returns:
            Number of chunks removed
        """
        ...

    def search(
        self,
        query_embedding: Vector,
        limit: int = 10,
        filter_book_ids: Sequence[BookIdentifier] | None = None,
        filter_libraries: Sequence[str] | None = None,
        min_score: float = 0.0,
    ) -> list[tuple[TextChunk, float]]:
        """Search for similar chunks.

        Args:
            query_embedding: The query vector to search for
            limit: Maximum number of results
            filter_book_ids: Optional filter to specific books
            filter_libraries: Optional filter to specific libraries
            min_score: Minimum similarity score threshold

        Returns:
            List of (chunk, score) tuples, ordered by descending score
        """
        ...

    def get_indexed_books(self) -> set[BookIdentifier]:
        """Get set of all indexed book identifiers.

        Returns:
            Set of BookIdentifier for all indexed books
        """
        ...

    def get_chunk_count(self, book_id: BookIdentifier | None = None) -> int:
        """Get total chunk count.

        Args:
            book_id: Optional filter to count chunks for specific book

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

    def clear(self) -> None:
        """Remove all data from the store."""
        ...
