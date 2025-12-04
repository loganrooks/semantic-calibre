"""ChromaDB vector store implementation with profile support.

This store uses ChromaDB for persistent vector storage with native HNSW indexing.
It provides:
- Persistent storage with automatic HNSW index management
- Profile-based namespace isolation via collections
- Efficient metadata filtering on book_id
- Native support for large-scale libraries (Phase 3)

Installation:
    pip install calibre-semantic[chromadb]

Usage:
    >>> from calibre_semantic.providers.vectordb.chromadb import ChromaDBStore
    >>> from calibre_semantic.core.types import VectorStoreConfig
    >>> from pathlib import Path
    >>> config = VectorStoreConfig(
    ...     backend="chromadb",
    ...     path=Path("/path/to/chromadb/")
    ... )
    >>> store = ChromaDBStore(config)
    >>> store.add(embedded_chunks, profile_id="my-profile")
    >>> results = store.search(query_vector, profile_id="my-profile", limit=10)

Per ADR-006: This store only stores book_id as metadata for filtering.
Full book metadata is fetched from Calibre DB at query time.
"""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any, Sequence

import numpy as np

from calibre_semantic.core.types import (
    BookIdentifier,
    ChunkLocation,
    ChunkType,
    EmbeddedChunk,
    TextChunk,
    Vector,
    VectorStoreConfig,
)
from calibre_semantic.core.vectordb import BaseVectorStore

logger = logging.getLogger(__name__)

# Default profile for backwards compatibility
DEFAULT_PROFILE_ID = "_default"

# Collection name prefix
COLLECTION_PREFIX = "semantic_"


def _sanitize_collection_name(profile_id: str) -> str:
    """Sanitize profile ID into valid ChromaDB collection name.

    ChromaDB collection names must:
    - Be 3-63 characters
    - Start and end with alphanumeric
    - Contain only alphanumeric, underscore, hyphen
    - Not contain consecutive periods

    Args:
        profile_id: The profile ID to sanitize

    Returns:
        Valid collection name
    """
    # Replace invalid characters with underscore
    name = re.sub(r'[^a-zA-Z0-9_-]', '_', profile_id)
    # Ensure starts with letter
    if not name[0].isalpha():
        name = 'p' + name
    # Truncate if needed (leaving room for prefix)
    max_len = 63 - len(COLLECTION_PREFIX)
    name = name[:max_len]
    # Ensure ends with alphanumeric
    while name and not name[-1].isalnum():
        name = name[:-1]
    if len(name) < 3:
        name = name + '_profile'
    return COLLECTION_PREFIX + name


class ChromaDBStore(BaseVectorStore):
    """ChromaDB-based vector store with profile support.

    Uses ChromaDB for efficient vector similarity search with HNSW indexing.
    Each profile maps to a separate ChromaDB collection for isolation.

    Metadata stored per chunk (per ADR-006):
    - book_library_id: Calibre library UUID
    - book_id: Calibre book ID (integer stored as string)
    - book_format: Book format (EPUB, PDF, etc.)
    - chunk_index: Position in book for ordering
    - spine_index, spine_name, start_offset, end_offset, cfi: Location info
    - chunk_type, chapter_title, section_title: Content metadata

    Attributes:
        config: The vector store configuration
        _client: ChromaDB client
        _collections: Cache of collection objects by profile ID
    """

    def __init__(self, config: VectorStoreConfig):
        """Initialize the ChromaDB store.

        Args:
            config: Vector store configuration with path to database directory

        Raises:
            ImportError: If chromadb is not installed
        """
        super().__init__(config)

        try:
            import chromadb
            from chromadb.config import Settings
        except ImportError as e:
            raise ImportError(
                "chromadb is required for this backend. "
                "Install it with: pip install calibre-semantic[chromadb]"
            ) from e

        # Determine storage path
        if config.path is None:
            # In-memory mode
            self._client = chromadb.Client()
            logger.info("Initialized ChromaDB store (in-memory)")
        else:
            # Persistent mode
            db_path = Path(config.path)
            db_path.mkdir(parents=True, exist_ok=True)

            settings = Settings(
                chroma_db_impl="duckdb+parquet",
                persist_directory=str(db_path),
                anonymized_telemetry=False,
            )
            self._client = chromadb.Client(settings)
            logger.info(f"Initialized ChromaDB store at {db_path}")

        # Collection cache
        self._collections: dict[str, Any] = {}

        # Load model ID from metadata collection if exists
        self._load_metadata()

    def _load_metadata(self) -> None:
        """Load store-level metadata from special metadata collection."""
        try:
            meta_collection = self._client.get_or_create_collection(
                name="_metadata",
                metadata={"purpose": "store_metadata"},
            )
            # Try to get model_id
            result = meta_collection.get(ids=["model_id"])
            if result["documents"] and result["documents"][0]:
                self._model_id = result["documents"][0]
        except Exception as e:
            logger.debug(f"Could not load metadata: {e}")

    def _save_metadata(self) -> None:
        """Save store-level metadata to special metadata collection."""
        try:
            meta_collection = self._client.get_or_create_collection(
                name="_metadata",
                metadata={"purpose": "store_metadata"},
            )
            if self._model_id:
                meta_collection.upsert(
                    ids=["model_id"],
                    documents=[self._model_id],
                )
        except Exception as e:
            logger.warning(f"Could not save metadata: {e}")

    def _get_collection(self, profile_id: str) -> Any:
        """Get or create a collection for the given profile.

        Args:
            profile_id: The profile ID

        Returns:
            ChromaDB Collection object
        """
        if profile_id not in self._collections:
            collection_name = _sanitize_collection_name(profile_id)
            self._collections[profile_id] = self._client.get_or_create_collection(
                name=collection_name,
                metadata={
                    "profile_id": profile_id,
                    "hnsw:space": "cosine",  # Use cosine similarity
                },
            )
        return self._collections[profile_id]

    def add(
        self,
        chunks: Sequence[EmbeddedChunk],
        profile_id: str | None = None,
    ) -> None:
        """Add embedded chunks to the store.

        Args:
            chunks: Sequence of embedded chunks to store
            profile_id: Profile to add chunks to (uses default if None)
        """
        if not chunks:
            return

        profile_id = profile_id or DEFAULT_PROFILE_ID
        collection = self._get_collection(profile_id)

        # Prepare batch data
        ids = []
        embeddings = []
        documents = []
        metadatas = []

        for embedded_chunk in chunks:
            chunk = embedded_chunk.chunk
            book_id = chunk.book_id

            ids.append(chunk.id)
            embeddings.append(embedded_chunk.embedding.tolist())
            documents.append(chunk.text)

            # Store metadata for filtering and reconstruction
            # Per ADR-006: Only store book_id components for filtering
            metadata = {
                "book_library_id": book_id.library_id,
                "book_id": str(book_id.book_id),  # ChromaDB requires string values
                "book_format": book_id.format,
                # Location info for navigation
                "spine_index": chunk.location.spine_index,
                "spine_name": chunk.location.spine_name,
                "start_offset": chunk.location.start_offset,
                "end_offset": chunk.location.end_offset,
                "chunk_type": chunk.chunk_type.value,
            }

            # Optional fields
            if chunk.location.cfi:
                metadata["cfi"] = chunk.location.cfi
            if chunk.chapter_title:
                metadata["chapter_title"] = chunk.chapter_title
            if chunk.section_title:
                metadata["section_title"] = chunk.section_title
            if chunk.metadata:
                metadata["chunk_metadata"] = json.dumps(chunk.metadata)

            metadatas.append(metadata)

        # Upsert to handle duplicates
        collection.upsert(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
        )

        logger.debug(f"Added {len(chunks)} chunks to profile '{profile_id}'")

    def remove(
        self,
        chunk_ids: Sequence[str],
        profile_id: str | None = None,
    ) -> None:
        """Remove chunks by ID.

        Args:
            chunk_ids: Sequence of chunk IDs to remove
            profile_id: Profile to remove from (uses default if None)
        """
        if not chunk_ids:
            return

        profile_id = profile_id or DEFAULT_PROFILE_ID
        collection = self._get_collection(profile_id)

        collection.delete(ids=list(chunk_ids))
        logger.debug(f"Removed {len(chunk_ids)} chunks from profile '{profile_id}'")

    def remove_book(
        self,
        book_id: BookIdentifier,
        profile_id: str | None = None,
    ) -> int:
        """Remove all chunks for a book from a profile.

        Args:
            book_id: The book whose chunks should be removed
            profile_id: Profile to remove from (uses default if None)

        Returns:
            Number of chunks removed
        """
        profile_id = profile_id or DEFAULT_PROFILE_ID
        collection = self._get_collection(profile_id)

        # Query for chunks matching this book
        where_filter = {
            "$and": [
                {"book_library_id": {"$eq": book_id.library_id}},
                {"book_id": {"$eq": str(book_id.book_id)}},
                {"book_format": {"$eq": book_id.format}},
            ]
        }

        # Get matching chunk IDs
        result = collection.get(where=where_filter)
        chunk_ids = result.get("ids", [])

        if chunk_ids:
            collection.delete(ids=chunk_ids)
            logger.debug(
                f"Removed {len(chunk_ids)} chunks for book {book_id} "
                f"from profile '{profile_id}'"
            )

        return len(chunk_ids)

    def search(
        self,
        query_embedding: Vector,
        limit: int = 10,
        profile_id: str | None = None,
        filter_book_ids: Sequence[BookIdentifier] | None = None,
        filter_libraries: Sequence[str] | None = None,
        min_score: float = 0.0,
    ) -> list[tuple[TextChunk, float]]:
        """Search for similar chunks using vector similarity.

        Uses ChromaDB's native HNSW index for efficient approximate search.

        Args:
            query_embedding: The query vector to search for
            limit: Maximum number of results
            profile_id: Profile to search in (uses default if None)
            filter_book_ids: Optional filter to specific books (from Calibre DB query)
            filter_libraries: Optional filter to specific libraries
            min_score: Minimum similarity score threshold

        Returns:
            List of (chunk, score) tuples, ordered by descending score
        """
        profile_id = profile_id or DEFAULT_PROFILE_ID

        try:
            collection = self._get_collection(profile_id)
        except Exception:
            # Collection doesn't exist, return empty
            return []

        # Handle empty filter_book_ids (no books matched metadata query)
        # Per ADR-006: If Calibre DB returns no matching books, return empty results
        if filter_book_ids is not None and len(filter_book_ids) == 0:
            return []

        # Build where filter for book_ids (per ADR-006 hybrid query)
        where_filter = None
        if filter_book_ids or filter_libraries:
            conditions = []

            if filter_book_ids:
                # Filter to specific books (result of Calibre DB metadata query)
                book_conditions = []
                for bid in filter_book_ids:
                    book_conditions.append({
                        "$and": [
                            {"book_library_id": {"$eq": bid.library_id}},
                            {"book_id": {"$eq": str(bid.book_id)}},
                            {"book_format": {"$eq": bid.format}},
                        ]
                    })
                if len(book_conditions) == 1:
                    conditions.append(book_conditions[0])
                else:
                    conditions.append({"$or": book_conditions})

            if filter_libraries:
                if len(filter_libraries) == 1:
                    conditions.append({
                        "book_library_id": {"$eq": filter_libraries[0]}
                    })
                else:
                    conditions.append({
                        "book_library_id": {"$in": list(filter_libraries)}
                    })

            if len(conditions) == 1:
                where_filter = conditions[0]
            else:
                where_filter = {"$and": conditions}

        # Query ChromaDB
        result = collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=limit,
            where=where_filter,
            include=["embeddings", "documents", "metadatas", "distances"],
        )

        # Process results
        results = []
        if result["ids"] and result["ids"][0]:
            ids = result["ids"][0]
            documents = result["documents"][0] if result["documents"] else [None] * len(ids)
            metadatas = result["metadatas"][0] if result["metadatas"] else [{}] * len(ids)
            distances = result["distances"][0] if result["distances"] else [0] * len(ids)

            for i, chunk_id in enumerate(ids):
                # Convert distance to similarity score
                # ChromaDB returns L2 distance for cosine, need to convert
                # For cosine similarity: score = 1 - distance
                # But ChromaDB returns squared distances for cosine space
                distance = distances[i]
                score = 1.0 - distance

                if score < min_score:
                    continue

                metadata = metadatas[i] or {}
                text = documents[i] or ""

                chunk = self._metadata_to_chunk(chunk_id, text, metadata)
                results.append((chunk, score))

        return results

    def _metadata_to_chunk(
        self,
        chunk_id: str,
        text: str,
        metadata: dict[str, Any],
    ) -> TextChunk:
        """Convert ChromaDB metadata back to TextChunk.

        Args:
            chunk_id: The chunk ID
            text: The document text
            metadata: Metadata dictionary from ChromaDB

        Returns:
            Reconstructed TextChunk
        """
        # Reconstruct BookIdentifier
        book_id = BookIdentifier(
            library_id=metadata.get("book_library_id", ""),
            book_id=int(metadata.get("book_id", 0)),
            format=metadata.get("book_format", "EPUB"),
        )

        # Reconstruct ChunkLocation
        location = ChunkLocation(
            spine_index=metadata.get("spine_index", 0),
            spine_name=metadata.get("spine_name", ""),
            start_offset=metadata.get("start_offset", 0),
            end_offset=metadata.get("end_offset", 0),
            cfi=metadata.get("cfi"),
        )

        # Parse chunk type
        chunk_type_str = metadata.get("chunk_type", "paragraph")
        try:
            chunk_type = ChunkType(chunk_type_str)
        except ValueError:
            chunk_type = ChunkType.PARAGRAPH

        # Parse additional metadata
        chunk_metadata = {}
        if "chunk_metadata" in metadata:
            try:
                chunk_metadata = json.loads(metadata["chunk_metadata"])
            except json.JSONDecodeError:
                pass

        return TextChunk(
            id=chunk_id,
            book_id=book_id,
            text=text,
            location=location,
            chunk_type=chunk_type,
            metadata=chunk_metadata,
            chapter_title=metadata.get("chapter_title"),
            section_title=metadata.get("section_title"),
        )

    def get_indexed_books(
        self,
        profile_id: str | None = None,
    ) -> set[BookIdentifier]:
        """Get set of all indexed book identifiers in a profile.

        Args:
            profile_id: Profile to query (uses default if None)

        Returns:
            Set of BookIdentifier for all indexed books
        """
        profile_id = profile_id or DEFAULT_PROFILE_ID

        try:
            collection = self._get_collection(profile_id)
        except Exception:
            return set()

        # Get all metadata
        result = collection.get(include=["metadatas"])

        books = set()
        if result["metadatas"]:
            for metadata in result["metadatas"]:
                if metadata:
                    try:
                        book_id = BookIdentifier(
                            library_id=metadata.get("book_library_id", ""),
                            book_id=int(metadata.get("book_id", 0)),
                            format=metadata.get("book_format", "EPUB"),
                        )
                        books.add(book_id)
                    except (ValueError, TypeError):
                        continue

        return books

    def get_chunk_count(
        self,
        book_id: BookIdentifier | None = None,
        profile_id: str | None = None,
    ) -> int:
        """Get total chunk count in a profile.

        Args:
            book_id: Optional filter to count chunks for specific book
            profile_id: Profile to query (uses default if None)

        Returns:
            Number of chunks in store
        """
        profile_id = profile_id or DEFAULT_PROFILE_ID

        try:
            collection = self._get_collection(profile_id)
        except Exception:
            return 0

        if book_id is None:
            return collection.count()

        # Filter by book
        where_filter = {
            "$and": [
                {"book_library_id": {"$eq": book_id.library_id}},
                {"book_id": {"$eq": str(book_id.book_id)}},
                {"book_format": {"$eq": book_id.format}},
            ]
        }
        result = collection.get(where=where_filter)
        return len(result.get("ids", []))

    def get_profiles(self) -> list[str]:
        """Get list of all profiles with data in the store.

        Returns:
            List of profile IDs
        """
        profiles = []
        for collection in self._client.list_collections():
            name = collection.name
            if name.startswith(COLLECTION_PREFIX):
                # Get original profile_id from metadata
                meta = collection.metadata or {}
                profile_id = meta.get("profile_id")
                if profile_id:
                    profiles.append(profile_id)
        return sorted(profiles)

    def get_model_id(self) -> str | None:
        """Get the model ID from store metadata."""
        return self._model_id

    def set_model_id(self, model_id: str) -> None:
        """Set the model ID in store metadata."""
        self._model_id = model_id
        self._save_metadata()

    def clear(self, profile_id: str | None = None) -> None:
        """Remove all data from the store or a specific profile.

        Args:
            profile_id: If provided, only clear that profile.
                       If None, clear entire store.
        """
        if profile_id is not None:
            # Clear specific profile by deleting collection
            collection_name = _sanitize_collection_name(profile_id)
            try:
                self._client.delete_collection(collection_name)
                if profile_id in self._collections:
                    del self._collections[profile_id]
                logger.info(f"Cleared profile '{profile_id}' from ChromaDB store")
            except Exception as e:
                logger.warning(f"Could not clear profile '{profile_id}': {e}")
        else:
            # Clear all collections except metadata
            for collection in self._client.list_collections():
                if collection.name != "_metadata":
                    try:
                        self._client.delete_collection(collection.name)
                    except Exception as e:
                        logger.warning(f"Could not delete collection {collection.name}: {e}")

            self._collections.clear()
            self._model_id = None

            # Also clear metadata collection
            try:
                self._client.delete_collection("_metadata")
            except Exception:
                pass

            logger.info("Cleared entire ChromaDB store")

    def persist(self) -> None:
        """Persist any pending changes to disk.

        ChromaDB with duckdb+parquet should auto-persist, but this
        can be called explicitly.
        """
        try:
            if hasattr(self._client, 'persist'):
                self._client.persist()
        except Exception as e:
            logger.warning(f"Could not persist ChromaDB: {e}")

    def close(self) -> None:
        """Close the ChromaDB client and persist data."""
        self.persist()
        self._collections.clear()

    def __del__(self):
        """Ensure data is persisted on cleanup."""
        try:
            self.persist()
        except Exception:
            pass
