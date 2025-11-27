"""SemanticSearchEngine - Main orchestration for semantic search.

This module provides the high-level API for semantic search operations,
coordinating between embedding providers, vector stores, and chunking
strategies.

Profile Support:
    All operations accept an optional profile_id parameter for namespace
    isolation. This allows storing embeddings from different models or
    configurations in the same database.

Usage:
    >>> from calibre_semantic import SemanticSearchEngine
    >>> from calibre_semantic.core import SemanticSearchConfig
    >>> config = SemanticSearchConfig()
    >>> engine = SemanticSearchEngine(config)
    >>> engine.index_text(text, book_id, 0, "chapter1.xhtml", profile_id="my-profile")
    >>> results = engine.search("machine learning", profile_id="my-profile")
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

    Profile Support:
        All operations accept an optional profile_id parameter for namespace
        isolation. Use profiles to:
        - Store embeddings from different models separately
        - Create different search indexes for different use cases
        - Keep embeddings from different libraries isolated

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
        profile_id: str | None = None,
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
            profile_id: Profile namespace (uses default if None)

        Returns:
            Number of chunks indexed
        """
        if force_reindex:
            self._vector_store.remove_book(book_id, profile_id=profile_id)

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
        self._vector_store.add(embedded_chunks, profile_id=profile_id)

        logger.debug(
            f"Indexed {len(chunks)} chunks for book {book_id}, "
            f"spine_index={spine_index}, profile={profile_id}"
        )

        return len(chunks)

    def index_book_content(
        self,
        book_id: BookIdentifier,
        spine_items: Sequence[tuple[str, str]],
        chapter_titles: dict[int, str] | None = None,
        force_reindex: bool = False,
        profile_id: str | None = None,
    ) -> int:
        """Index all content from a book.

        Args:
            book_id: The book identifier
            spine_items: List of (spine_name, content) tuples
            chapter_titles: Optional dict mapping spine_index to chapter title
            force_reindex: If True, remove existing chunks first
            profile_id: Profile namespace (uses default if None)

        Returns:
            Total number of chunks indexed
        """
        if force_reindex:
            self._vector_store.remove_book(book_id, profile_id=profile_id)

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
                profile_id=profile_id,
            )
            total_chunks += count

        logger.info(
            f"Indexed {total_chunks} chunks from {len(spine_items)} "
            f"spine items for book {book_id} (profile={profile_id})"
        )

        return total_chunks

    def index_epub(
        self,
        epub_path: str | bytes,
        book_id: BookIdentifier,
        force_reindex: bool = False,
        profile_id: str | None = None,
    ) -> int:
        """Index an EPUB file.

        Extracts text content from all spine items and indexes them.

        Args:
            epub_path: Path to EPUB file or EPUB bytes
            book_id: The book identifier
            force_reindex: If True, remove existing chunks first
            profile_id: Profile namespace (uses default if None)

        Returns:
            Total number of chunks indexed

        Raises:
            EPUBError: If the EPUB file is invalid
        """
        from calibre_semantic.extraction.epub import EPUBExtractor

        if force_reindex:
            self._vector_store.remove_book(book_id, profile_id=profile_id)

        total_chunks = 0

        with EPUBExtractor(epub_path) as extractor:
            for item in extractor.iter_content():
                if not item['text'].strip():
                    continue

                count = self.index_text(
                    text=item['text'],
                    book_id=book_id,
                    spine_index=item['spine_index'],
                    spine_name=item['spine_name'],
                    chapter_title=item['chapter_title'],
                    force_reindex=False,  # Already handled above
                    profile_id=profile_id,
                )
                total_chunks += count

        logger.info(
            f"Indexed {total_chunks} chunks from EPUB for book {book_id} "
            f"(profile={profile_id})"
        )
        return total_chunks

    # =========================================================================
    # Search Operations
    # =========================================================================

    def search(
        self,
        query: str,
        limit: int | None = None,
        profile_id: str | None = None,
        filter_book_ids: Sequence[BookIdentifier] | None = None,
        filter_libraries: Sequence[str] | None = None,
        min_score: float | None = None,
    ) -> SearchResults:
        """Search for semantically similar content.

        Args:
            query: The search query text
            limit: Maximum number of results (default from config)
            profile_id: Profile namespace to search (uses default if None)
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
            profile_id=profile_id,
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
            total_searched=self._vector_store.get_chunk_count(profile_id=profile_id),
            search_time_ms=elapsed_ms,
            model_id=self.model_id,
        )

    # =========================================================================
    # Book Management
    # =========================================================================

    def is_indexed(
        self,
        book_id: BookIdentifier,
        profile_id: str | None = None,
    ) -> bool:
        """Check if a book has been indexed in a profile.

        Args:
            book_id: The book identifier to check
            profile_id: Profile namespace (uses default if None)

        Returns:
            True if the book has indexed chunks
        """
        return book_id in self._vector_store.get_indexed_books(profile_id=profile_id)

    def remove_book(
        self,
        book_id: BookIdentifier,
        profile_id: str | None = None,
    ) -> int:
        """Remove all indexed content for a book from a profile.

        Args:
            book_id: The book identifier
            profile_id: Profile namespace (uses default if None)

        Returns:
            Number of chunks removed
        """
        count = self._vector_store.remove_book(book_id, profile_id=profile_id)
        logger.info(f"Removed {count} chunks for book {book_id} (profile={profile_id})")
        return count

    def get_indexed_books(
        self,
        profile_id: str | None = None,
    ) -> set[BookIdentifier]:
        """Get all indexed book identifiers in a profile.

        Args:
            profile_id: Profile namespace (uses default if None)

        Returns:
            Set of BookIdentifier for all indexed books
        """
        return self._vector_store.get_indexed_books(profile_id=profile_id)

    def get_profiles(self) -> list[str]:
        """Get all profiles with data in the store.

        Returns:
            List of profile IDs
        """
        return self._vector_store.get_profiles()

    def get_stats(self, profile_id: str | None = None) -> dict:
        """Get statistics about the search index.

        Args:
            profile_id: Profile namespace (uses default if None for overall stats)

        Returns:
            Dictionary with index statistics
        """
        indexed_books = self._vector_store.get_indexed_books(profile_id=profile_id)
        return {
            "profile_id": profile_id,
            "total_chunks": self._vector_store.get_chunk_count(profile_id=profile_id),
            "total_books": len(indexed_books),
            "model_id": self.model_id,
            "embedding_dimension": self.embedding_dimension,
        }

    def clear(self, profile_id: str | None = None) -> None:
        """Clear indexed content.

        Args:
            profile_id: If provided, only clear that profile.
                       If None, clear entire store.
        """
        self._vector_store.clear(profile_id=profile_id)
        if profile_id:
            logger.info(f"Cleared profile '{profile_id}'")
        else:
            logger.info("Cleared all indexed content")
