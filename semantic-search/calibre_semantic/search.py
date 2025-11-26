"""SemanticSearchEngine - Main orchestration for semantic search.

This module provides the high-level API for semantic search operations,
coordinating between embedding providers, vector stores, and chunking
strategies.

Usage:
    >>> from calibre_semantic import SemanticSearchEngine
    >>> from calibre_semantic.core import SemanticSearchConfig
    >>> config = SemanticSearchConfig()
    >>> engine = SemanticSearchEngine(config)
    >>> engine.index_text(text, book_id, 0, "chapter1.xhtml")
    >>> results = engine.search("machine learning")
"""

from __future__ import annotations

import logging
import time
from typing import TYPE_CHECKING, Sequence

from calibre_semantic.core.chunking import create_chunking_strategy
from calibre_semantic.core.types import (
    BookIdentifier,
    EmbeddedChunk,
    EmbeddingProvider,
    SearchResult,
    SearchResults,
    SemanticSearchConfig,
    VectorStore,
)

if TYPE_CHECKING:
    pass

logger = logging.getLogger(__name__)


class SemanticSearchEngine:
    """Main orchestration class for semantic search.

    This class coordinates between:
    - Embedding provider: generates embeddings for text
    - Vector store: stores and searches embeddings
    - Chunking strategy: splits text into searchable chunks

    Attributes:
        config: The semantic search configuration
        _embedding_provider: The embedding provider instance
        _vector_store: The vector store instance
        _chunking_strategy: The chunking strategy instance
    """

    def __init__(
        self,
        config: SemanticSearchConfig,
        embedding_provider: EmbeddingProvider | None = None,
        vector_store: VectorStore | None = None,
    ):
        """Initialize the semantic search engine.

        Args:
            config: Semantic search configuration
            embedding_provider: Optional pre-configured embedding provider
            vector_store: Optional pre-configured vector store

        If embedding_provider or vector_store are not provided, they will
        be created based on the configuration.
        """
        self._config = config

        # Use provided components or create from config
        if embedding_provider is not None:
            self._embedding_provider = embedding_provider
        else:
            from calibre_semantic.core.embeddings import create_embedding_provider
            self._embedding_provider = create_embedding_provider(config.embedding)

        if vector_store is not None:
            self._vector_store = vector_store
        else:
            from calibre_semantic.core.vectordb import create_vector_store
            self._vector_store = create_vector_store(config.vector_store)

        # Create chunking strategy
        self._chunking_strategy = create_chunking_strategy(config.chunking)

        # Set model ID in vector store if not already set
        stored_model = self._vector_store.get_model_id()
        if stored_model is None:
            self._vector_store.set_model_id(self._embedding_provider.model_id)
        elif stored_model != self._embedding_provider.model_id:
            logger.warning(
                f"Vector store model ({stored_model}) differs from "
                f"embedding provider ({self._embedding_provider.model_id}). "
                "Consider clearing the index."
            )

        logger.info(
            f"Initialized SemanticSearchEngine with model={self.model_id}, "
            f"dimension={self.embedding_dimension}"
        )

    @property
    def config(self) -> SemanticSearchConfig:
        """Get the configuration."""
        return self._config

    @property
    def model_id(self) -> str:
        """Get the embedding model identifier."""
        return self._embedding_provider.model_id

    @property
    def embedding_dimension(self) -> int:
        """Get the embedding vector dimension."""
        return self._embedding_provider.dimension

    # =========================================================================
    # Indexing Operations
    # =========================================================================

    def index_text(
        self,
        text: str,
        book_id: BookIdentifier,
        spine_index: int,
        spine_name: str,
        chapter_title: str | None = None,
        force_reindex: bool = False,
    ) -> int:
        """Index text content from a book.

        Splits the text into chunks, generates embeddings, and stores them
        in the vector store.

        Args:
            text: The text content to index
            book_id: The book identifier
            spine_index: Index in EPUB spine or page number
            spine_name: Spine item filename
            chapter_title: Optional chapter title
            force_reindex: If True, remove existing chunks first

        Returns:
            Number of chunks indexed
        """
        if force_reindex:
            self._vector_store.remove_book(book_id)

        # Skip empty text
        if not text or not text.strip():
            return 0

        # Split into chunks
        chunks = list(self._chunking_strategy.chunk(
            text=text,
            book_id=book_id,
            spine_index=spine_index,
            spine_name=spine_name,
            chapter_title=chapter_title,
        ))

        if not chunks:
            return 0

        # Generate embeddings
        texts = [chunk.text for chunk in chunks]
        embeddings = self._embedding_provider.embed(texts)

        # Create embedded chunks
        embedded_chunks = [
            EmbeddedChunk(
                chunk=chunk,
                embedding=embedding,
                model_id=self.model_id,
            )
            for chunk, embedding in zip(chunks, embeddings)
        ]

        # Store in vector store
        self._vector_store.add(embedded_chunks)

        logger.debug(
            f"Indexed {len(chunks)} chunks for book {book_id}, "
            f"spine_index={spine_index}"
        )

        return len(chunks)

    def index_book_content(
        self,
        book_id: BookIdentifier,
        spine_items: Sequence[tuple[str, str]],
        chapter_titles: dict[int, str] | None = None,
        force_reindex: bool = False,
    ) -> int:
        """Index all content from a book.

        Args:
            book_id: The book identifier
            spine_items: List of (spine_name, content) tuples
            chapter_titles: Optional dict mapping spine_index to chapter title
            force_reindex: If True, remove existing chunks first

        Returns:
            Total number of chunks indexed
        """
        if force_reindex:
            self._vector_store.remove_book(book_id)

        total_chunks = 0
        chapter_titles = chapter_titles or {}

        for spine_index, (spine_name, content) in enumerate(spine_items):
            chapter_title = chapter_titles.get(spine_index)
            count = self.index_text(
                text=content,
                book_id=book_id,
                spine_index=spine_index,
                spine_name=spine_name,
                chapter_title=chapter_title,
                force_reindex=False,  # Already handled above
            )
            total_chunks += count

        logger.info(
            f"Indexed {total_chunks} chunks from {len(spine_items)} "
            f"spine items for book {book_id}"
        )

        return total_chunks

    # =========================================================================
    # Search Operations
    # =========================================================================

    def search(
        self,
        query: str,
        limit: int | None = None,
        filter_book_ids: Sequence[BookIdentifier] | None = None,
        filter_libraries: Sequence[str] | None = None,
        min_score: float | None = None,
    ) -> SearchResults:
        """Search for semantically similar content.

        Args:
            query: The search query text
            limit: Maximum number of results (default from config)
            filter_book_ids: Optional filter to specific books
            filter_libraries: Optional filter to specific libraries
            min_score: Minimum similarity score (default from config)

        Returns:
            SearchResults containing matched chunks with scores
        """
        start_time = time.perf_counter()

        # Use defaults from config
        if limit is None:
            limit = self._config.default_result_limit
        if min_score is None:
            min_score = self._config.min_similarity_score

        # Generate query embedding
        query_embedding = self._embedding_provider.embed_query(query)

        # Search vector store
        results = self._vector_store.search(
            query_embedding=query_embedding,
            limit=limit,
            filter_book_ids=filter_book_ids,
            filter_libraries=filter_libraries,
            min_score=min_score,
        )

        # Convert to SearchResult objects
        search_results = [
            SearchResult(chunk=chunk, score=score)
            for chunk, score in results
        ]

        elapsed_ms = (time.perf_counter() - start_time) * 1000

        return SearchResults(
            query=query,
            results=search_results,
            total_searched=self._vector_store.get_chunk_count(),
            search_time_ms=elapsed_ms,
            model_id=self.model_id,
        )

    # =========================================================================
    # Book Management
    # =========================================================================

    def is_indexed(self, book_id: BookIdentifier) -> bool:
        """Check if a book has been indexed.

        Args:
            book_id: The book identifier to check

        Returns:
            True if the book has indexed chunks
        """
        return book_id in self._vector_store.get_indexed_books()

    def remove_book(self, book_id: BookIdentifier) -> int:
        """Remove all indexed content for a book.

        Args:
            book_id: The book identifier

        Returns:
            Number of chunks removed
        """
        count = self._vector_store.remove_book(book_id)
        logger.info(f"Removed {count} chunks for book {book_id}")
        return count

    def get_indexed_books(self) -> set[BookIdentifier]:
        """Get all indexed book identifiers.

        Returns:
            Set of BookIdentifier for all indexed books
        """
        return self._vector_store.get_indexed_books()

    def get_stats(self) -> dict:
        """Get statistics about the search index.

        Returns:
            Dictionary with index statistics
        """
        indexed_books = self._vector_store.get_indexed_books()
        return {
            "total_chunks": self._vector_store.get_chunk_count(),
            "total_books": len(indexed_books),
            "model_id": self.model_id,
            "embedding_dimension": self.embedding_dimension,
        }

    def clear(self) -> None:
        """Clear all indexed content."""
        self._vector_store.clear()
        logger.info("Cleared all indexed content")
