"""Vector store abstractions and factory.

This module provides:
1. BaseVectorStore - Abstract base class with common functionality
2. create_vector_store() - Factory function to instantiate stores

Vector stores handle the storage and retrieval of embedding vectors,
enabling efficient semantic similarity search.
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Sequence

from calibre_semantic.core.types import (
    BookIdentifier,
    EmbeddedChunk,
    TextChunk,
    Vector,
    VectorStoreConfig,
)

if TYPE_CHECKING:
    from calibre_semantic.core.types import VectorStore

logger = logging.getLogger(__name__)


class BaseVectorStore(ABC):
    """Abstract base class for vector store implementations.

    Provides common functionality for all vector stores:
    - Model ID tracking for cache invalidation
    - Profile-based namespace isolation
    - Logging

    Subclasses must implement all abstract methods for:
    - Adding/removing chunks
    - Searching by vector similarity
    - Index management

    Profile Support:
        All operations accept an optional profile_id parameter for namespace
        isolation. This allows storing embeddings from different models or
        configurations in the same database without conflicts.

    Example usage:
        class MyStore(BaseVectorStore):
            def add(self, chunks: Sequence[EmbeddedChunk], profile_id: str | None = None) -> None:
                # Store chunks in your backend
                pass

            def search(self, query: Vector, ..., profile_id: str | None = None) -> list[tuple[TextChunk, float]]:
                # Search your backend
                pass
    """

    def __init__(self, config: VectorStoreConfig):
        """Initialize the vector store.

        Args:
            config: Configuration for the vector store
        """
        self.config = config
        self._model_id: str | None = None

    @abstractmethod
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
        pass

    @abstractmethod
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
        pass

    @abstractmethod
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
        pass

    @abstractmethod
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
        pass

    @abstractmethod
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
        pass

    @abstractmethod
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
        pass

    def get_model_id(self) -> str | None:
        """Get the model ID used for embeddings in this store.

        Returns:
            Model ID string or None if not set
        """
        return self._model_id

    def set_model_id(self, model_id: str) -> None:
        """Set the model ID for embeddings in this store.

        Args:
            model_id: The model identifier string
        """
        self._model_id = model_id

    @abstractmethod
    def clear(self, profile_id: str | None = None) -> None:
        """Remove all data from the store or a specific profile.

        Args:
            profile_id: If provided, only clear that profile.
                       If None, clear entire store.
        """
        pass

    def get_profiles(self) -> list[str]:
        """Get list of all profiles with data in the store.

        Returns:
            List of profile IDs. Default implementation returns empty list.
        """
        return []

    def needs_reindex(self, model_id: str) -> bool:
        """Check if store needs reindexing due to model change.

        Args:
            model_id: The current model ID

        Returns:
            True if the store has data from a different model
        """
        current = self.get_model_id()
        return current is not None and current != model_id


# =============================================================================
# Store Registry and Factory
# =============================================================================

# Registry of available backends
# Maps backend name to (module_path, class_name) tuple
_STORE_REGISTRY: dict[str, tuple[str, str]] = {
    "memory": (
        "calibre_semantic.providers.vectordb.memory",
        "InMemoryVectorStore",
    ),
    "sqlite-vec": (
        "calibre_semantic.providers.vectordb.sqlite_vec",
        "SQLiteVecStore",
    ),
    "chromadb": (
        "calibre_semantic.providers.vectordb.chromadb",
        "ChromaDBStore",
    ),
    "faiss": (
        "calibre_semantic.providers.vectordb.faiss",
        "FAISSStore",
    ),
}


def register_backend(name: str, module_path: str, class_name: str) -> None:
    """Register a custom vector store backend.

    Allows extending the library with custom backends without
    modifying the core code.

    Args:
        name: Backend name to use in config
        module_path: Full module path (e.g., "mypackage.vectordb")
        class_name: Name of the store class

    Example:
        >>> register_backend(
        ...     "custom",
        ...     "my_package.vectordb",
        ...     "CustomStore"
        ... )
        >>> config = VectorStoreConfig(backend="custom")
        >>> store = create_vector_store(config)
    """
    _STORE_REGISTRY[name] = (module_path, class_name)
    logger.info(f"Registered vector store backend: {name}")


def get_available_backends() -> list[str]:
    """Get list of registered backend names.

    Returns:
        List of backend name strings
    """
    return list(_STORE_REGISTRY.keys())


def create_vector_store(config: VectorStoreConfig) -> "VectorStore":
    """Factory function to create vector store from configuration.

    Uses dynamic import to only load dependencies when needed.

    Args:
        config: Vector store configuration specifying backend

    Returns:
        Configured VectorStore instance

    Raises:
        ValueError: If backend name is not registered
        ImportError: If backend dependencies are not installed

    Example:
        >>> config = VectorStoreConfig(
        ...     backend="sqlite-vec",
        ...     path=Path("/path/to/store.db")
        ... )
        >>> store = create_vector_store(config)
        >>> store.add(embedded_chunks)
    """
    if config.backend not in _STORE_REGISTRY:
        available = ", ".join(get_available_backends())
        raise ValueError(
            f"Unknown vector store backend: {config.backend}. "
            f"Available backends: {available}"
        )

    module_path, class_name = _STORE_REGISTRY[config.backend]

    try:
        import importlib

        module = importlib.import_module(module_path)
        store_class = getattr(module, class_name)
    except ImportError as e:
        raise ImportError(
            f"Failed to import backend '{config.backend}'. "
            f"Make sure the required dependencies are installed. "
            f"Try: pip install calibre-semantic[{config.backend}]\n"
            f"Original error: {e}"
        ) from e
    except AttributeError as e:
        raise ImportError(
            f"Store class '{class_name}' not found in module '{module_path}'"
        ) from e

    logger.info(f"Creating vector store: {config.backend}")
    return store_class(config)
