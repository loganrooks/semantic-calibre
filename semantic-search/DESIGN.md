# Semantic Search Library Design

## Overview

`calibre-semantic` is a Python library providing semantic search capabilities for e-book collections. It serves as the foundation for:

1. **Viewer Integration** - Within-book semantic search (Phase 2)
2. **Library Search UI** - Cross-library semantic search (Phase 3)
3. **MCP Server** - AI assistant integration
4. **Standalone API** - External integrations

> **Note:** Per [ADR-004](../docs/decisions/004-minimal-viewer-modification.md), we directly modify
> the Calibre fork (specifically `src/calibre/gui2/viewer/search.py`) rather than creating a plugin.

## Design Principles

1. **Abstraction over Implementation** - Core interfaces don't depend on specific embedding models or vector DBs
2. **Offline-First** - Works without internet by default (local models)
3. **Incremental Indexing** - Efficient updates when books are added/modified
4. **Calibre-Native** - Integrates naturally with Calibre's database and conventions
5. **Async-Ready** - Supports both sync and async operations for UI responsiveness

---

## Package Structure

```
calibre_semantic/
├── __init__.py
├── search.py              # Main SemanticSearchEngine orchestration
├── core/
│   ├── __init__.py
│   ├── types.py           # Core data types, protocols, configuration
│   ├── embeddings.py      # Embedding provider abstraction & factory
│   ├── vectordb.py        # Vector storage abstraction & factory
│   ├── chunking.py        # Document chunking strategies
│   └── profiles.py        # Embedding profiles & book index status
├── providers/
│   ├── __init__.py
│   ├── embeddings/
│   │   ├── __init__.py
│   │   ├── sentence_transformers.py  # Local embedding model
│   │   └── calibre_ai.py             # Calibre AI module adapter
│   └── vectordb/
│       ├── __init__.py
│       ├── memory.py      # In-memory store (testing/development)
│       └── sqlite_vec.py  # SQLite-vec persistent store
├── extraction/
│   ├── __init__.py
│   └── epub.py            # EPUB text extraction
└── mcp/
    ├── __init__.py
    ├── __main__.py        # CLI entry point
    └── server.py          # MCP protocol server

# Planned (not yet implemented):
# - providers/embeddings/openai.py      # OpenAI embeddings
# - providers/embeddings/ollama.py      # Ollama local models
# - providers/vectordb/chromadb.py      # ChromaDB backend
# - providers/vectordb/faiss.py         # FAISS backend
```

---

## Core Types (`core/types.py`)

```python
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Protocol, Sequence, AsyncIterator, Iterator, Any
from enum import Enum
from pathlib import Path
import numpy as np
from numpy.typing import NDArray


# =============================================================================
# Core Value Types
# =============================================================================

Vector = NDArray[np.float32]  # Embedding vector type


class ChunkType(Enum):
    """Type of content chunk."""
    PARAGRAPH = "paragraph"
    CHAPTER = "chapter"
    SECTION = "section"
    PAGE = "page"
    SENTENCE = "sentence"


@dataclass(frozen=True)
class BookIdentifier:
    """Unique identifier for a book across libraries."""
    library_id: str          # Calibre library UUID
    book_id: int             # Calibre book ID within library
    format: str              # e.g., "EPUB", "PDF", "MOBI"

    def __str__(self) -> str:
        return f"{self.library_id}:{self.book_id}:{self.format}"

    @classmethod
    def from_string(cls, s: str) -> BookIdentifier:
        library_id, book_id, format = s.split(":")
        return cls(library_id, int(book_id), format)


@dataclass(frozen=True)
class ChunkLocation:
    """Location of a chunk within a book for navigation."""
    spine_index: int         # Index in EPUB spine / page number
    spine_name: str          # Spine item name (e.g., "chapter1.xhtml")
    start_offset: int        # Character offset from start of spine item
    end_offset: int          # End character offset
    cfi: str | None = None   # EPUB CFI for precise navigation (optional)

    def to_dict(self) -> dict:
        return {
            "spine_index": self.spine_index,
            "spine_name": self.spine_name,
            "start_offset": self.start_offset,
            "end_offset": self.end_offset,
            "cfi": self.cfi,
        }


@dataclass
class TextChunk:
    """A chunk of text from a book with location metadata."""
    id: str                           # Unique chunk ID
    book_id: BookIdentifier           # Source book
    text: str                         # The actual text content
    location: ChunkLocation           # Where in the book
    chunk_type: ChunkType             # Type of chunk
    metadata: dict[str, Any] = field(default_factory=dict)  # Additional metadata

    # Optional context for better search results
    chapter_title: str | None = None
    section_title: str | None = None


@dataclass
class EmbeddedChunk:
    """A text chunk with its embedding vector."""
    chunk: TextChunk
    embedding: Vector
    model_id: str            # Which model generated this embedding


@dataclass
class SearchResult:
    """A single semantic search result."""
    chunk: TextChunk
    score: float             # Similarity score (0-1, higher is better)
    highlights: list[tuple[int, int]] = field(default_factory=list)  # (start, end) offsets


@dataclass
class SearchResults:
    """Collection of search results with metadata."""
    query: str
    results: list[SearchResult]
    total_searched: int      # Total chunks searched
    search_time_ms: float    # How long the search took
    model_id: str            # Embedding model used


@dataclass
class BookMetadata:
    """Book metadata from Calibre."""
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
    """Progress information for indexing operations."""
    book_id: BookIdentifier
    status: str              # "pending", "extracting", "chunking", "embedding", "complete", "error"
    progress: float          # 0.0 to 1.0
    message: str | None = None
    error: str | None = None


# =============================================================================
# Core Protocols (Interfaces)
# =============================================================================

class EmbeddingProvider(Protocol):
    """Protocol for embedding generation providers."""

    @property
    def model_id(self) -> str:
        """Unique identifier for this model (used for cache invalidation)."""
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
        """Generate embeddings for multiple texts (sync)."""
        ...

    async def embed_async(self, texts: Sequence[str]) -> list[Vector]:
        """Generate embeddings for multiple texts (async)."""
        ...

    def embed_query(self, query: str) -> Vector:
        """Generate embedding for a search query.

        Some models use different embeddings for queries vs documents.
        """
        ...


class VectorStore(Protocol):
    """Protocol for vector storage backends."""

    def add(self, chunks: Sequence[EmbeddedChunk]) -> None:
        """Add embedded chunks to the store."""
        ...

    def remove(self, chunk_ids: Sequence[str]) -> None:
        """Remove chunks by ID."""
        ...

    def remove_book(self, book_id: BookIdentifier) -> int:
        """Remove all chunks for a book. Returns count removed."""
        ...

    def search(
        self,
        query_embedding: Vector,
        limit: int = 10,
        filter_book_ids: Sequence[BookIdentifier] | None = None,
        filter_libraries: Sequence[str] | None = None,
        min_score: float = 0.0,
    ) -> list[tuple[TextChunk, float]]:
        """Search for similar chunks. Returns (chunk, score) tuples."""
        ...

    def get_indexed_books(self) -> set[BookIdentifier]:
        """Get set of all indexed book identifiers."""
        ...

    def get_chunk_count(self, book_id: BookIdentifier | None = None) -> int:
        """Get total chunk count, optionally filtered by book."""
        ...

    def get_model_id(self) -> str | None:
        """Get the model ID used for embeddings in this store."""
        ...

    def set_model_id(self, model_id: str) -> None:
        """Set/update the model ID (used for cache invalidation)."""
        ...

    def clear(self) -> None:
        """Remove all data from the store."""
        ...


class ChunkingStrategy(Protocol):
    """Protocol for document chunking strategies."""

    def chunk(
        self,
        text: str,
        book_id: BookIdentifier,
        spine_index: int,
        spine_name: str,
        chapter_title: str | None = None,
    ) -> Iterator[TextChunk]:
        """Split text into chunks with location metadata."""
        ...

    @property
    def target_chunk_size(self) -> int:
        """Target size in characters for each chunk."""
        ...

    @property
    def chunk_overlap(self) -> int:
        """Number of characters to overlap between chunks."""
        ...


class TextExtractor(Protocol):
    """Protocol for extracting text from ebook formats."""

    def extract(self, book_path: Path, format: str) -> Iterator[tuple[int, str, str]]:
        """Extract text from a book file.

        Yields: (spine_index, spine_name, text) tuples
        """
        ...

    def supported_formats(self) -> set[str]:
        """Return set of supported format strings (e.g., {"EPUB", "PDF"})."""
        ...


class ProgressCallback(Protocol):
    """Protocol for progress reporting callbacks."""

    def __call__(self, progress: IndexingProgress) -> None:
        """Called with progress updates during indexing."""
        ...


# =============================================================================
# Configuration Types
# =============================================================================

@dataclass
class EmbeddingConfig:
    """Configuration for embedding provider."""
    provider: str = "sentence-transformers"  # Provider name
    model: str = "all-MiniLM-L6-v2"          # Model name/path
    api_key: str | None = None                # For cloud providers
    api_base: str | None = None               # Custom API endpoint
    batch_size: int = 32                      # Batch size for embedding
    device: str = "auto"                      # "cpu", "cuda", "mps", "auto"


@dataclass
class VectorStoreConfig:
    """Configuration for vector store."""
    backend: str = "sqlite-vec"       # Backend name
    path: Path | None = None          # Storage path (None = in-memory)
    options: dict[str, Any] = field(default_factory=dict)


@dataclass
class ChunkingConfig:
    """Configuration for text chunking."""
    strategy: str = "semantic"        # "semantic", "fixed", "paragraph"
    target_size: int = 512            # Target chunk size in characters
    overlap: int = 64                 # Overlap between chunks
    respect_boundaries: bool = True   # Respect paragraph/sentence boundaries


@dataclass
class SemanticSearchConfig:
    """Main configuration for semantic search."""
    embedding: EmbeddingConfig = field(default_factory=EmbeddingConfig)
    vector_store: VectorStoreConfig = field(default_factory=VectorStoreConfig)
    chunking: ChunkingConfig = field(default_factory=ChunkingConfig)

    # Search settings
    default_result_limit: int = 20
    min_similarity_score: float = 0.3

    # Indexing settings
    index_on_add: bool = True         # Auto-index when books added
    background_indexing: bool = True  # Index in background thread

    @classmethod
    def from_dict(cls, data: dict) -> SemanticSearchConfig:
        """Create config from dictionary."""
        return cls(
            embedding=EmbeddingConfig(**data.get("embedding", {})),
            vector_store=VectorStoreConfig(**data.get("vector_store", {})),
            chunking=ChunkingConfig(**data.get("chunking", {})),
            default_result_limit=data.get("default_result_limit", 20),
            min_similarity_score=data.get("min_similarity_score", 0.3),
            index_on_add=data.get("index_on_add", True),
            background_indexing=data.get("background_indexing", True),
        )

    def to_dict(self) -> dict:
        """Convert config to dictionary."""
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
```

---

## Embedding Providers (`core/embeddings.py`)

```python
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Sequence
import numpy as np

from .types import Vector, EmbeddingConfig, EmbeddingProvider


class BaseEmbeddingProvider(ABC):
    """Base class for embedding providers with common functionality."""

    def __init__(self, config: EmbeddingConfig):
        self.config = config
        self._model = None

    @property
    @abstractmethod
    def model_id(self) -> str:
        """Unique identifier for this model."""
        pass

    @property
    @abstractmethod
    def dimension(self) -> int:
        """Dimension of embedding vectors."""
        pass

    @property
    @abstractmethod
    def max_tokens(self) -> int:
        """Maximum tokens per embedding."""
        pass

    @abstractmethod
    def _embed_batch(self, texts: Sequence[str]) -> list[Vector]:
        """Internal method to embed a batch of texts."""
        pass

    def embed(self, texts: Sequence[str]) -> list[Vector]:
        """Generate embeddings for multiple texts with batching."""
        if not texts:
            return []

        results = []
        batch_size = self.config.batch_size

        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            batch_embeddings = self._embed_batch(batch)
            results.extend(batch_embeddings)

        return results

    async def embed_async(self, texts: Sequence[str]) -> list[Vector]:
        """Async embedding - default implementation uses sync."""
        # Subclasses can override for true async
        import asyncio
        return await asyncio.get_event_loop().run_in_executor(
            None, self.embed, texts
        )

    def embed_query(self, query: str) -> Vector:
        """Embed a search query. Override if model uses different query embeddings."""
        return self.embed([query])[0]

    def _normalize(self, vectors: list[Vector]) -> list[Vector]:
        """L2 normalize vectors for cosine similarity."""
        return [v / np.linalg.norm(v) for v in vectors]


def create_embedding_provider(config: EmbeddingConfig) -> EmbeddingProvider:
    """Factory function to create embedding provider from config."""
    providers = {
        "sentence-transformers": "calibre_semantic.providers.embeddings.sentence_transformers.SentenceTransformerProvider",
        "openai": "calibre_semantic.providers.embeddings.openai.OpenAIProvider",
        "ollama": "calibre_semantic.providers.embeddings.ollama.OllamaProvider",
        "voyageai": "calibre_semantic.providers.embeddings.voyageai.VoyageAIProvider",
    }

    if config.provider not in providers:
        raise ValueError(f"Unknown embedding provider: {config.provider}")

    # Dynamic import
    module_path, class_name = providers[config.provider].rsplit(".", 1)
    import importlib
    module = importlib.import_module(module_path)
    provider_class = getattr(module, class_name)

    return provider_class(config)
```

---

## Vector Store (`core/vectordb.py`)

```python
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Sequence
from pathlib import Path

from .types import (
    Vector, TextChunk, EmbeddedChunk, BookIdentifier,
    VectorStoreConfig, VectorStore
)


class BaseVectorStore(ABC):
    """Base class for vector store implementations."""

    def __init__(self, config: VectorStoreConfig):
        self.config = config
        self._model_id: str | None = None

    @abstractmethod
    def add(self, chunks: Sequence[EmbeddedChunk]) -> None:
        """Add embedded chunks to the store."""
        pass

    @abstractmethod
    def remove(self, chunk_ids: Sequence[str]) -> None:
        """Remove chunks by ID."""
        pass

    @abstractmethod
    def remove_book(self, book_id: BookIdentifier) -> int:
        """Remove all chunks for a book."""
        pass

    @abstractmethod
    def search(
        self,
        query_embedding: Vector,
        limit: int = 10,
        filter_book_ids: Sequence[BookIdentifier] | None = None,
        filter_libraries: Sequence[str] | None = None,
        min_score: float = 0.0,
    ) -> list[tuple[TextChunk, float]]:
        """Search for similar chunks."""
        pass

    @abstractmethod
    def get_indexed_books(self) -> set[BookIdentifier]:
        """Get all indexed book identifiers."""
        pass

    @abstractmethod
    def get_chunk_count(self, book_id: BookIdentifier | None = None) -> int:
        """Get chunk count."""
        pass

    def get_model_id(self) -> str | None:
        """Get the embedding model ID."""
        return self._model_id

    def set_model_id(self, model_id: str) -> None:
        """Set the embedding model ID."""
        self._model_id = model_id

    @abstractmethod
    def clear(self) -> None:
        """Clear all data."""
        pass

    def needs_reindex(self, model_id: str) -> bool:
        """Check if store needs reindexing due to model change."""
        current = self.get_model_id()
        return current is not None and current != model_id


def create_vector_store(config: VectorStoreConfig) -> VectorStore:
    """Factory function to create vector store from config."""
    backends = {
        "sqlite-vec": "calibre_semantic.providers.vectordb.sqlite_vec.SQLiteVecStore",
        "chromadb": "calibre_semantic.providers.vectordb.chromadb.ChromaDBStore",
        "faiss": "calibre_semantic.providers.vectordb.faiss.FAISSStore",
    }

    if config.backend not in backends:
        raise ValueError(f"Unknown vector store backend: {config.backend}")

    module_path, class_name = backends[config.backend].rsplit(".", 1)
    import importlib
    module = importlib.import_module(module_path)
    store_class = getattr(module, class_name)

    return store_class(config)
```

---

## Chunking Strategies (`core/chunking.py`)

```python
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterator
import re
import hashlib

from .types import (
    TextChunk, ChunkType, BookIdentifier, ChunkLocation, ChunkingConfig
)


class BaseChunkingStrategy(ABC):
    """Base class for chunking strategies."""

    def __init__(self, config: ChunkingConfig):
        self.config = config

    @property
    def target_chunk_size(self) -> int:
        return self.config.target_size

    @property
    def chunk_overlap(self) -> int:
        return self.config.overlap

    @abstractmethod
    def chunk(
        self,
        text: str,
        book_id: BookIdentifier,
        spine_index: int,
        spine_name: str,
        chapter_title: str | None = None,
    ) -> Iterator[TextChunk]:
        """Split text into chunks."""
        pass

    def _generate_chunk_id(self, book_id: BookIdentifier, spine_index: int, offset: int) -> str:
        """Generate deterministic chunk ID."""
        content = f"{book_id}:{spine_index}:{offset}"
        return hashlib.sha256(content.encode()).hexdigest()[:16]


class SemanticChunkingStrategy(BaseChunkingStrategy):
    """Chunks text respecting semantic boundaries (paragraphs, sentences)."""

    # Regex patterns for boundary detection
    PARAGRAPH_PATTERN = re.compile(r'\n\s*\n')
    SENTENCE_PATTERN = re.compile(r'(?<=[.!?])\s+(?=[A-Z])')

    def chunk(
        self,
        text: str,
        book_id: BookIdentifier,
        spine_index: int,
        spine_name: str,
        chapter_title: str | None = None,
    ) -> Iterator[TextChunk]:
        """Split text into semantic chunks."""

        # First, split into paragraphs
        paragraphs = self.PARAGRAPH_PATTERN.split(text)

        current_chunk = ""
        current_start = 0
        chunk_start = 0

        for para in paragraphs:
            para = para.strip()
            if not para:
                current_start += 2  # Account for paragraph break
                continue

            # If adding this paragraph exceeds target, yield current chunk
            if current_chunk and len(current_chunk) + len(para) > self.target_chunk_size:
                yield self._create_chunk(
                    text=current_chunk,
                    book_id=book_id,
                    spine_index=spine_index,
                    spine_name=spine_name,
                    start_offset=chunk_start,
                    chapter_title=chapter_title,
                )

                # Start new chunk with overlap
                overlap_text = self._get_overlap_text(current_chunk)
                current_chunk = overlap_text + para
                chunk_start = current_start - len(overlap_text)
            else:
                if current_chunk:
                    current_chunk += "\n\n" + para
                else:
                    current_chunk = para
                    chunk_start = current_start

            current_start += len(para) + 2  # +2 for paragraph break

        # Yield final chunk
        if current_chunk.strip():
            yield self._create_chunk(
                text=current_chunk,
                book_id=book_id,
                spine_index=spine_index,
                spine_name=spine_name,
                start_offset=chunk_start,
                chapter_title=chapter_title,
            )

    def _get_overlap_text(self, text: str) -> str:
        """Get overlap text from end of chunk, respecting sentence boundaries."""
        if len(text) <= self.chunk_overlap:
            return text

        overlap_region = text[-self.chunk_overlap * 2:]

        # Try to find sentence boundary
        sentences = self.SENTENCE_PATTERN.split(overlap_region)
        if len(sentences) > 1:
            return sentences[-1]

        return text[-self.chunk_overlap:]

    def _create_chunk(
        self,
        text: str,
        book_id: BookIdentifier,
        spine_index: int,
        spine_name: str,
        start_offset: int,
        chapter_title: str | None,
    ) -> TextChunk:
        """Create a TextChunk instance."""
        chunk_id = self._generate_chunk_id(book_id, spine_index, start_offset)

        return TextChunk(
            id=chunk_id,
            book_id=book_id,
            text=text,
            location=ChunkLocation(
                spine_index=spine_index,
                spine_name=spine_name,
                start_offset=start_offset,
                end_offset=start_offset + len(text),
            ),
            chunk_type=ChunkType.PARAGRAPH,
            chapter_title=chapter_title,
        )


class FixedSizeChunkingStrategy(BaseChunkingStrategy):
    """Chunks text into fixed-size pieces with overlap."""

    def chunk(
        self,
        text: str,
        book_id: BookIdentifier,
        spine_index: int,
        spine_name: str,
        chapter_title: str | None = None,
    ) -> Iterator[TextChunk]:
        """Split text into fixed-size chunks."""

        start = 0
        while start < len(text):
            end = min(start + self.target_chunk_size, len(text))

            # Try to end at word boundary
            if end < len(text):
                space_idx = text.rfind(' ', start, end)
                if space_idx > start:
                    end = space_idx

            chunk_text = text[start:end].strip()

            if chunk_text:
                chunk_id = self._generate_chunk_id(book_id, spine_index, start)

                yield TextChunk(
                    id=chunk_id,
                    book_id=book_id,
                    text=chunk_text,
                    location=ChunkLocation(
                        spine_index=spine_index,
                        spine_name=spine_name,
                        start_offset=start,
                        end_offset=end,
                    ),
                    chunk_type=ChunkType.SECTION,
                    chapter_title=chapter_title,
                )

            start = end - self.chunk_overlap
            if start >= len(text) - self.chunk_overlap:
                break


def create_chunking_strategy(config: ChunkingConfig) -> BaseChunkingStrategy:
    """Factory function to create chunking strategy from config."""
    strategies = {
        "semantic": SemanticChunkingStrategy,
        "fixed": FixedSizeChunkingStrategy,
    }

    if config.strategy not in strategies:
        raise ValueError(f"Unknown chunking strategy: {config.strategy}")

    return strategies[config.strategy](config)
```

---

## Search Orchestration (`core/search.py`)

```python
from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence, Callable, Awaitable
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor

from .types import (
    TextChunk, EmbeddedChunk, BookIdentifier, BookMetadata,
    SearchResult, SearchResults, IndexingProgress, SemanticSearchConfig,
    EmbeddingProvider, VectorStore, ChunkingStrategy, TextExtractor, ProgressCallback
)
from .embeddings import create_embedding_provider
from .vectordb import create_vector_store
from .chunking import create_chunking_strategy


class SemanticSearchEngine:
    """Main orchestration class for semantic search operations."""

    def __init__(
        self,
        config: SemanticSearchConfig,
        text_extractor: TextExtractor | None = None,
    ):
        self.config = config
        self.embedding_provider = create_embedding_provider(config.embedding)
        self.vector_store = create_vector_store(config.vector_store)
        self.chunking_strategy = create_chunking_strategy(config.chunking)
        self.text_extractor = text_extractor

        self._executor = ThreadPoolExecutor(max_workers=2)

        # Check for model change requiring reindex
        if self.vector_store.needs_reindex(self.embedding_provider.model_id):
            # Store will need to be cleared and reindexed
            pass

        self.vector_store.set_model_id(self.embedding_provider.model_id)

    # =========================================================================
    # Search Operations
    # =========================================================================

    def search(
        self,
        query: str,
        limit: int | None = None,
        book_ids: Sequence[BookIdentifier] | None = None,
        library_ids: Sequence[str] | None = None,
        min_score: float | None = None,
    ) -> SearchResults:
        """Perform semantic search across indexed books.

        Args:
            query: Natural language search query
            limit: Maximum results to return
            book_ids: Filter to specific books
            library_ids: Filter to specific libraries
            min_score: Minimum similarity score (0-1)

        Returns:
            SearchResults with ranked results
        """
        start_time = time.perf_counter()

        limit = limit or self.config.default_result_limit
        min_score = min_score or self.config.min_similarity_score

        # Generate query embedding
        query_embedding = self.embedding_provider.embed_query(query)

        # Search vector store
        raw_results = self.vector_store.search(
            query_embedding=query_embedding,
            limit=limit,
            filter_book_ids=book_ids,
            filter_libraries=library_ids,
            min_score=min_score,
        )

        # Convert to SearchResult objects
        results = [
            SearchResult(
                chunk=chunk,
                score=score,
                highlights=self._compute_highlights(query, chunk.text),
            )
            for chunk, score in raw_results
        ]

        elapsed = (time.perf_counter() - start_time) * 1000

        return SearchResults(
            query=query,
            results=results,
            total_searched=self.vector_store.get_chunk_count(
                book_ids[0] if book_ids and len(book_ids) == 1 else None
            ),
            search_time_ms=elapsed,
            model_id=self.embedding_provider.model_id,
        )

    async def search_async(
        self,
        query: str,
        limit: int | None = None,
        book_ids: Sequence[BookIdentifier] | None = None,
        library_ids: Sequence[str] | None = None,
        min_score: float | None = None,
    ) -> SearchResults:
        """Async version of search."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            self._executor,
            lambda: self.search(query, limit, book_ids, library_ids, min_score)
        )

    def search_in_book(
        self,
        query: str,
        book_id: BookIdentifier,
        limit: int = 50,
        min_score: float | None = None,
    ) -> SearchResults:
        """Search within a single book (for viewer integration)."""
        return self.search(
            query=query,
            limit=limit,
            book_ids=[book_id],
            min_score=min_score or 0.2,  # Lower threshold for in-book search
        )

    def _compute_highlights(self, query: str, text: str) -> list[tuple[int, int]]:
        """Compute highlight positions for query terms in text."""
        highlights = []
        query_words = query.lower().split()
        text_lower = text.lower()

        for word in query_words:
            start = 0
            while True:
                pos = text_lower.find(word, start)
                if pos == -1:
                    break
                highlights.append((pos, pos + len(word)))
                start = pos + 1

        # Merge overlapping highlights
        highlights.sort()
        merged = []
        for start, end in highlights:
            if merged and start <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(merged[-1][1], end))
            else:
                merged.append((start, end))

        return merged

    # =========================================================================
    # Indexing Operations
    # =========================================================================

    def index_book(
        self,
        book_metadata: BookMetadata,
        progress_callback: ProgressCallback | None = None,
    ) -> int:
        """Index a single book.

        Args:
            book_metadata: Book metadata including file path
            progress_callback: Optional callback for progress updates

        Returns:
            Number of chunks indexed
        """
        book_id = book_metadata.book_id

        def report(status: str, progress: float, message: str | None = None, error: str | None = None):
            if progress_callback:
                progress_callback(IndexingProgress(
                    book_id=book_id,
                    status=status,
                    progress=progress,
                    message=message,
                    error=error,
                ))

        try:
            report("extracting", 0.1, f"Extracting text from {book_metadata.title}")

            if not self.text_extractor:
                raise RuntimeError("No text extractor configured")

            if not book_metadata.file_path:
                raise ValueError("Book file path not provided")

            # Remove existing chunks for this book
            self.vector_store.remove_book(book_id)

            # Extract text and chunk
            chunks: list[TextChunk] = []
            for spine_index, spine_name, text in self.text_extractor.extract(
                book_metadata.file_path, book_id.format
            ):
                for chunk in self.chunking_strategy.chunk(
                    text=text,
                    book_id=book_id,
                    spine_index=spine_index,
                    spine_name=spine_name,
                ):
                    chunks.append(chunk)

            report("embedding", 0.4, f"Generating embeddings for {len(chunks)} chunks")

            # Generate embeddings in batches
            texts = [c.text for c in chunks]
            embeddings = self.embedding_provider.embed(texts)

            # Create embedded chunks
            embedded_chunks = [
                EmbeddedChunk(
                    chunk=chunk,
                    embedding=embedding,
                    model_id=self.embedding_provider.model_id,
                )
                for chunk, embedding in zip(chunks, embeddings)
            ]

            report("storing", 0.8, "Storing embeddings")

            # Store in vector database
            self.vector_store.add(embedded_chunks)

            report("complete", 1.0, f"Indexed {len(chunks)} chunks")

            return len(chunks)

        except Exception as e:
            report("error", 0.0, error=str(e))
            raise

    async def index_book_async(
        self,
        book_metadata: BookMetadata,
        progress_callback: ProgressCallback | None = None,
    ) -> int:
        """Async version of index_book."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            self._executor,
            lambda: self.index_book(book_metadata, progress_callback)
        )

    def index_books(
        self,
        books: Sequence[BookMetadata],
        progress_callback: ProgressCallback | None = None,
    ) -> dict[BookIdentifier, int | Exception]:
        """Index multiple books.

        Returns:
            Dict mapping book_id to chunk count or exception
        """
        results = {}

        for book in books:
            try:
                count = self.index_book(book, progress_callback)
                results[book.book_id] = count
            except Exception as e:
                results[book.book_id] = e

        return results

    def remove_book(self, book_id: BookIdentifier) -> int:
        """Remove a book from the index.

        Returns:
            Number of chunks removed
        """
        return self.vector_store.remove_book(book_id)

    # =========================================================================
    # Index Management
    # =========================================================================

    def get_indexed_books(self) -> set[BookIdentifier]:
        """Get set of all indexed book identifiers."""
        return self.vector_store.get_indexed_books()

    def is_indexed(self, book_id: BookIdentifier) -> bool:
        """Check if a book is indexed."""
        return book_id in self.get_indexed_books()

    def get_stats(self) -> dict:
        """Get indexing statistics."""
        indexed_books = self.get_indexed_books()
        return {
            "total_books": len(indexed_books),
            "total_chunks": self.vector_store.get_chunk_count(),
            "model_id": self.embedding_provider.model_id,
            "model_dimension": self.embedding_provider.dimension,
        }

    def clear_index(self) -> None:
        """Clear the entire index."""
        self.vector_store.clear()

    def close(self) -> None:
        """Clean up resources."""
        self._executor.shutdown(wait=True)
```

---

## Calibre Integration (`calibre/library.py`)

```python
from __future__ import annotations
from typing import Iterator, TYPE_CHECKING
from pathlib import Path
import json

from ..core.types import (
    BookIdentifier, BookMetadata, TextChunk, ChunkLocation,
    TextExtractor, SemanticSearchConfig
)
from ..core.search import SemanticSearchEngine

if TYPE_CHECKING:
    from calibre.library import db as calibre_db


class CalibreTextExtractor:
    """Extract text from Calibre books using Calibre's built-in extractors."""

    def __init__(self):
        # Import Calibre's text extraction utilities
        from calibre.db.fts.text import extract_text
        self._extract_text = extract_text

    def extract(self, book_path: Path, format: str) -> Iterator[tuple[int, str, str]]:
        """Extract text from a book file.

        Yields: (spine_index, spine_name, text) tuples
        """
        # Use Calibre's text extraction which supports many formats
        text_iter = self._extract_text(str(book_path))

        for idx, (name, text) in enumerate(text_iter):
            if text and text.strip():
                yield idx, name, text

    def supported_formats(self) -> set[str]:
        """Return supported format strings."""
        return {"EPUB", "PDF", "MOBI", "AZW3", "DOCX", "TXT", "RTF", "HTML", "FB2"}


class CalibreLibraryIntegration:
    """Integration with Calibre library database."""

    def __init__(
        self,
        db: calibre_db,
        config: SemanticSearchConfig | None = None,
    ):
        self.db = db
        self.library_id = self._get_library_id()

        # Setup config with library-specific storage path
        if config is None:
            config = SemanticSearchConfig()

        if config.vector_store.path is None:
            config.vector_store.path = Path(db.library_path) / ".calibre-semantic"

        self.config = config

        # Initialize search engine with Calibre text extractor
        self.engine = SemanticSearchEngine(
            config=config,
            text_extractor=CalibreTextExtractor(),
        )

    def _get_library_id(self) -> str:
        """Get unique library identifier."""
        return self.db.library_id

    def get_book_metadata(self, book_id: int, format: str) -> BookMetadata:
        """Get book metadata from Calibre database."""
        mi = self.db.get_metadata(book_id)
        file_path = self.db.format_abspath(book_id, format)

        return BookMetadata(
            book_id=BookIdentifier(
                library_id=self.library_id,
                book_id=book_id,
                format=format,
            ),
            title=mi.title,
            authors=list(mi.authors) if mi.authors else [],
            series=mi.series,
            series_index=mi.series_index,
            tags=list(mi.tags) if mi.tags else [],
            language=mi.language,
            publisher=mi.publisher,
            description=mi.comments,
            file_path=Path(file_path) if file_path else None,
        )

    def get_books_needing_index(self) -> Iterator[BookMetadata]:
        """Get books that haven't been indexed yet."""
        indexed = self.engine.get_indexed_books()
        indexed_local = {
            (b.book_id, b.format)
            for b in indexed
            if b.library_id == self.library_id
        }

        for book_id in self.db.all_book_ids():
            for format in self.db.formats(book_id):
                if (book_id, format) not in indexed_local:
                    yield self.get_book_metadata(book_id, format)

    def search(
        self,
        query: str,
        limit: int = 20,
        book_ids: list[int] | None = None,
    ):
        """Search across the library."""
        filter_book_ids = None
        if book_ids:
            filter_book_ids = [
                BookIdentifier(self.library_id, bid, "")
                for bid in book_ids
            ]

        return self.engine.search(
            query=query,
            limit=limit,
            book_ids=filter_book_ids,
            library_ids=[self.library_id],
        )

    def index_all(self, progress_callback=None):
        """Index all books in the library."""
        books = list(self.get_books_needing_index())
        return self.engine.index_books(books, progress_callback)


class MultiLibrarySearch:
    """Search across multiple Calibre libraries."""

    def __init__(self, config: SemanticSearchConfig):
        self.config = config
        self.libraries: dict[str, CalibreLibraryIntegration] = {}

    def add_library(self, db: "calibre_db") -> None:
        """Add a library to search."""
        integration = CalibreLibraryIntegration(db, self.config)
        self.libraries[integration.library_id] = integration

    def search(
        self,
        query: str,
        limit: int = 20,
        library_ids: list[str] | None = None,
    ):
        """Search across all registered libraries."""
        # This would use a shared vector store for cross-library search
        # Implementation depends on architecture decision
        pass
```

---

## MCP Server Interface (`mcp/server.py`)

```python
from __future__ import annotations
from typing import Any
import json
from dataclasses import asdict

from ..core.types import SemanticSearchConfig, BookIdentifier
from ..core.search import SemanticSearchEngine


class SemanticSearchMCPServer:
    """MCP (Model Context Protocol) server for semantic search.

    Exposes semantic search capabilities to AI assistants like Claude.
    """

    def __init__(self, engine: SemanticSearchEngine):
        self.engine = engine

    def get_tools(self) -> list[dict]:
        """Return MCP tool definitions."""
        return [
            {
                "name": "semantic_search_books",
                "description": "Search through e-book library using natural language. "
                              "Returns relevant passages from books that semantically match the query.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Natural language search query"
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of results",
                            "default": 10
                        },
                        "book_filter": {
                            "type": "string",
                            "description": "Optional: filter by book title (partial match)"
                        }
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "get_book_passage",
                "description": "Get a specific passage from a book by chunk ID",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "chunk_id": {
                            "type": "string",
                            "description": "The chunk ID from a previous search result"
                        }
                    },
                    "required": ["chunk_id"]
                }
            },
            {
                "name": "list_indexed_books",
                "description": "List all books that have been indexed for semantic search",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            },
            {
                "name": "get_index_stats",
                "description": "Get statistics about the semantic search index",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            }
        ]

    def handle_tool_call(self, tool_name: str, arguments: dict) -> dict:
        """Handle an MCP tool call."""
        handlers = {
            "semantic_search_books": self._handle_search,
            "get_book_passage": self._handle_get_passage,
            "list_indexed_books": self._handle_list_books,
            "get_index_stats": self._handle_stats,
        }

        handler = handlers.get(tool_name)
        if not handler:
            return {"error": f"Unknown tool: {tool_name}"}

        try:
            return handler(arguments)
        except Exception as e:
            return {"error": str(e)}

    def _handle_search(self, args: dict) -> dict:
        """Handle semantic search tool call."""
        results = self.engine.search(
            query=args["query"],
            limit=args.get("limit", 10),
        )

        return {
            "query": results.query,
            "total_results": len(results.results),
            "search_time_ms": results.search_time_ms,
            "results": [
                {
                    "chunk_id": r.chunk.id,
                    "score": round(r.score, 3),
                    "book": str(r.chunk.book_id),
                    "chapter": r.chunk.chapter_title,
                    "text": r.chunk.text[:500] + "..." if len(r.chunk.text) > 500 else r.chunk.text,
                    "location": r.chunk.location.to_dict(),
                }
                for r in results.results
            ]
        }

    def _handle_get_passage(self, args: dict) -> dict:
        """Handle get passage tool call."""
        # Would need chunk retrieval by ID
        return {"error": "Not yet implemented"}

    def _handle_list_books(self, args: dict) -> dict:
        """Handle list indexed books tool call."""
        books = self.engine.get_indexed_books()
        return {
            "total_books": len(books),
            "books": [str(b) for b in books]
        }

    def _handle_stats(self, args: dict) -> dict:
        """Handle stats tool call."""
        return self.engine.get_stats()


# MCP Protocol Implementation
class MCPProtocolHandler:
    """Handle MCP protocol messages over stdin/stdout."""

    def __init__(self, server: SemanticSearchMCPServer):
        self.server = server

    def handle_message(self, message: dict) -> dict:
        """Handle an incoming MCP message."""
        method = message.get("method")

        if method == "tools/list":
            return {
                "tools": self.server.get_tools()
            }

        elif method == "tools/call":
            params = message.get("params", {})
            tool_name = params.get("name")
            arguments = params.get("arguments", {})

            result = self.server.handle_tool_call(tool_name, arguments)

            return {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps(result, indent=2)
                    }
                ]
            }

        return {"error": f"Unknown method: {method}"}

    def run(self):
        """Run the MCP server (stdin/stdout mode)."""
        import sys

        for line in sys.stdin:
            try:
                message = json.loads(line)
                response = self.handle_message(message)
                print(json.dumps(response), flush=True)
            except json.JSONDecodeError:
                print(json.dumps({"error": "Invalid JSON"}), flush=True)
            except Exception as e:
                print(json.dumps({"error": str(e)}), flush=True)
```

---

## Viewer Integration (`calibre/viewer.py`)

```python
from __future__ import annotations
from typing import Iterator, TYPE_CHECKING
from pathlib import Path

from ..core.types import (
    BookIdentifier, TextChunk, SearchResult, SearchResults,
    ChunkLocation, SemanticSearchConfig
)
from ..core.search import SemanticSearchEngine

if TYPE_CHECKING:
    from calibre.gui2.viewer.web_view import ViewerBridge


class ViewerSemanticSearch:
    """Semantic search integration for Calibre e-book viewer.

    This class provides the bridge between the viewer's search UI
    and the semantic search engine.
    """

    def __init__(
        self,
        book_path: Path,
        book_id: BookIdentifier,
        config: SemanticSearchConfig | None = None,
    ):
        self.book_path = book_path
        self.book_id = book_id
        self.config = config or SemanticSearchConfig()

        # Use in-memory vector store for single-book search
        self.config.vector_store.path = None  # In-memory

        self.engine: SemanticSearchEngine | None = None
        self._indexed = False

    def ensure_indexed(self, text_by_name: dict[str, str]) -> None:
        """Index the current book's text.

        Args:
            text_by_name: Dict mapping spine names to extracted text
                         (from viewer's existing text extraction)
        """
        if self._indexed:
            return

        from ..core.embeddings import create_embedding_provider
        from ..core.vectordb import create_vector_store
        from ..core.chunking import create_chunking_strategy
        from ..core.types import EmbeddedChunk

        embedding_provider = create_embedding_provider(self.config.embedding)
        vector_store = create_vector_store(self.config.vector_store)
        chunking_strategy = create_chunking_strategy(self.config.chunking)

        # Chunk all text
        chunks: list[TextChunk] = []
        for spine_index, (name, text) in enumerate(text_by_name.items()):
            if not text or not text.strip():
                continue

            for chunk in chunking_strategy.chunk(
                text=text,
                book_id=self.book_id,
                spine_index=spine_index,
                spine_name=name,
            ):
                chunks.append(chunk)

        # Generate embeddings
        texts = [c.text for c in chunks]
        embeddings = embedding_provider.embed(texts)

        # Store
        embedded_chunks = [
            EmbeddedChunk(chunk=c, embedding=e, model_id=embedding_provider.model_id)
            for c, e in zip(chunks, embeddings)
        ]
        vector_store.add(embedded_chunks)
        vector_store.set_model_id(embedding_provider.model_id)

        # Create engine with pre-populated store
        self.engine = SemanticSearchEngine.__new__(SemanticSearchEngine)
        self.engine.config = self.config
        self.engine.embedding_provider = embedding_provider
        self.engine.vector_store = vector_store
        self.engine.chunking_strategy = chunking_strategy

        self._indexed = True

    def search(self, query: str, limit: int = 50) -> Iterator[ViewerSearchResult]:
        """Search within the current book.

        Yields ViewerSearchResult objects compatible with viewer's result handling.
        """
        if not self.engine:
            return

        results = self.engine.search_in_book(
            query=query,
            book_id=self.book_id,
            limit=limit,
        )

        for result in results.results:
            yield ViewerSearchResult(
                spine_name=result.chunk.location.spine_name,
                spine_index=result.chunk.location.spine_index,
                text=result.chunk.text,
                before="",  # Full chunk is the context
                after="",
                score=result.score,
                offset=result.chunk.location.start_offset,
            )


class ViewerSearchResult:
    """Search result compatible with viewer's result handling."""

    def __init__(
        self,
        spine_name: str,
        spine_index: int,
        text: str,
        before: str,
        after: str,
        score: float,
        offset: int,
    ):
        self.spine_name = spine_name
        self.spine_index = spine_index
        self.text = text
        self.before = before
        self.after = after
        self.score = score
        self.offset = offset

    def to_viewer_result(self) -> dict:
        """Convert to format expected by viewer JavaScript."""
        return {
            "spine_name": self.spine_name,
            "spine_index": self.spine_index,
            "text": self.text,
            "before": self.before,
            "after": self.after,
            "score": self.score,
        }
```

---

## Usage Examples

### Basic Library Search

```python
from calibre_semantic import SemanticSearchEngine, SemanticSearchConfig
from calibre_semantic.calibre import CalibreLibraryIntegration

# With Calibre database
from calibre.library import db

config = SemanticSearchConfig()
library = CalibreLibraryIntegration(db.db, config)

# Index all books (background)
library.index_all(progress_callback=lambda p: print(f"{p.status}: {p.progress:.0%}"))

# Search
results = library.search("philosophical arguments about free will")
for r in results.results:
    print(f"{r.score:.2f} - {r.chunk.chapter_title}: {r.chunk.text[:100]}...")
```

### MCP Server

```python
from calibre_semantic import SemanticSearchEngine, SemanticSearchConfig
from calibre_semantic.mcp import SemanticSearchMCPServer, MCPProtocolHandler

config = SemanticSearchConfig()
engine = SemanticSearchEngine(config)

server = SemanticSearchMCPServer(engine)
handler = MCPProtocolHandler(server)
handler.run()  # Listens on stdin/stdout
```

### Viewer Integration

```python
from calibre_semantic.calibre.viewer import ViewerSemanticSearch
from calibre_semantic.core.types import BookIdentifier

# In viewer's search.py
semantic_search = ViewerSemanticSearch(
    book_path=current_book_path,
    book_id=BookIdentifier(library_id, book_id, "EPUB"),
)

# When user selects semantic search mode
semantic_search.ensure_indexed(searchable_text_cache)

for result in semantic_search.search("meaning of life"):
    # Display in search results panel
    add_result_to_panel(result)
```

---

## Configuration File Format

```json
{
  "embedding": {
    "provider": "sentence-transformers",
    "model": "all-MiniLM-L6-v2",
    "batch_size": 32,
    "device": "auto"
  },
  "vector_store": {
    "backend": "sqlite-vec",
    "path": null
  },
  "chunking": {
    "strategy": "semantic",
    "target_size": 512,
    "overlap": 64,
    "respect_boundaries": true
  },
  "default_result_limit": 20,
  "min_similarity_score": 0.3,
  "index_on_add": true,
  "background_indexing": true
}
```

---

## Next Steps

1. **Implement embedding providers** - Start with sentence-transformers
2. **Implement SQLite-vec backend** - For tight Calibre integration
3. **Create Calibre plugin skeleton** - InterfaceActionBase implementation
4. **Modify viewer search.py** - Add semantic mode
5. **Build MCP server** - Enable AI assistant integration
6. **Testing infrastructure** - Unit tests for core components
