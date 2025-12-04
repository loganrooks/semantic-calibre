"""Tests for ChromaDB vector store implementation.

These tests verify the ChromaDB provider works correctly for Phase 3
library search with metadata filtering.
"""

from __future__ import annotations

import pytest
import numpy as np
from pathlib import Path

from calibre_semantic.core.types import (
    BookIdentifier,
    ChunkLocation,
    ChunkType,
    EmbeddedChunk,
    TextChunk,
    VectorStoreConfig,
)

# Skip all tests if chromadb is not installed
chromadb = pytest.importorskip("chromadb")

from calibre_semantic.providers.vectordb.chromadb import (
    ChromaDBStore,
    _sanitize_collection_name,
    DEFAULT_PROFILE_ID,
)


class TestCollectionNameSanitization:
    """Tests for collection name sanitization."""

    def test_simple_profile_id(self):
        """Simple alphanumeric profile IDs work."""
        result = _sanitize_collection_name("my_profile")
        assert result.startswith("semantic_")
        assert "my_profile" in result

    def test_profile_id_with_special_chars(self):
        """Special characters are replaced with underscores."""
        result = _sanitize_collection_name("my.profile/test")
        assert "." not in result
        assert "/" not in result

    def test_profile_id_starting_with_number(self):
        """Profile IDs starting with number get prefix."""
        result = _sanitize_collection_name("123profile")
        # Should start with letter after prefix
        after_prefix = result.replace("semantic_", "")
        assert after_prefix[0].isalpha()

    def test_very_long_profile_id(self):
        """Long profile IDs are truncated."""
        long_id = "a" * 100
        result = _sanitize_collection_name(long_id)
        assert len(result) <= 63


class TestChromaDBStoreBasic:
    """Basic tests for ChromaDB store operations."""

    @pytest.fixture
    def store(self):
        """Create an in-memory ChromaDB store."""
        config = VectorStoreConfig(backend="chromadb", path=None)
        store = ChromaDBStore(config)
        # Clear any existing data for test isolation
        store.clear()
        yield store
        store.close()

    @pytest.fixture
    def sample_chunks(self):
        """Create sample embedded chunks for testing."""
        book_id = BookIdentifier(
            library_id="test-library-uuid",
            book_id=42,
            format="EPUB",
        )

        chunks = []
        for i in range(5):
            chunk = TextChunk(
                id=f"chunk-{i}",
                book_id=book_id,
                text=f"This is test chunk number {i} with some content.",
                location=ChunkLocation(
                    spine_index=i,
                    spine_name=f"chapter{i}.xhtml",
                    start_offset=0,
                    end_offset=100,
                    cfi=f"/4/2[chapter{i}]",
                ),
                chunk_type=ChunkType.PARAGRAPH,
                chapter_title=f"Chapter {i}",
                metadata={"test_key": f"value_{i}"},
            )
            # Create a simple embedding vector
            embedding = np.random.rand(384).astype(np.float32)
            embedding = embedding / np.linalg.norm(embedding)  # Normalize
            chunks.append(EmbeddedChunk(
                chunk=chunk,
                embedding=embedding,
                model_id="test-model",
            ))
        return chunks

    def test_add_and_count(self, store, sample_chunks):
        """Test adding chunks and counting them."""
        assert store.get_chunk_count() == 0

        store.add(sample_chunks)

        assert store.get_chunk_count() == 5

    def test_add_with_profile(self, store, sample_chunks):
        """Test adding chunks to specific profile."""
        store.add(sample_chunks, profile_id="profile-a")
        store.add(sample_chunks[:2], profile_id="profile-b")

        assert store.get_chunk_count(profile_id="profile-a") == 5
        assert store.get_chunk_count(profile_id="profile-b") == 2
        # Default profile should be empty
        assert store.get_chunk_count() == 0

    def test_get_indexed_books(self, store, sample_chunks):
        """Test getting indexed book identifiers."""
        store.add(sample_chunks)

        books = store.get_indexed_books()
        assert len(books) == 1
        book = list(books)[0]
        assert book.library_id == "test-library-uuid"
        assert book.book_id == 42
        assert book.format == "EPUB"

    def test_remove_book(self, store, sample_chunks):
        """Test removing all chunks for a book."""
        store.add(sample_chunks)
        assert store.get_chunk_count() == 5

        book_id = sample_chunks[0].chunk.book_id
        removed = store.remove_book(book_id)

        assert removed == 5
        assert store.get_chunk_count() == 0

    def test_search_basic(self, store, sample_chunks):
        """Test basic vector search."""
        store.add(sample_chunks)

        # Use the embedding of the first chunk as query
        query_embedding = sample_chunks[0].embedding

        results = store.search(query_embedding, limit=3)

        assert len(results) == 3
        # First result should be the same chunk (highest similarity)
        first_chunk, first_score = results[0]
        assert first_chunk.id == "chunk-0"
        assert first_score > 0.9  # Should be very similar

    def test_search_with_book_filter(self, store):
        """Test search with book_id filter (per ADR-006)."""
        # Create chunks for two different books
        book1 = BookIdentifier("lib1", 1, "EPUB")
        book2 = BookIdentifier("lib1", 2, "EPUB")

        chunks = []
        for book_id in [book1, book2]:
            for i in range(3):
                chunk = TextChunk(
                    id=f"{book_id.book_id}-chunk-{i}",
                    book_id=book_id,
                    text=f"Content from book {book_id.book_id} chunk {i}",
                    location=ChunkLocation(i, f"ch{i}.xhtml", 0, 100),
                    chunk_type=ChunkType.PARAGRAPH,
                )
                embedding = np.random.rand(384).astype(np.float32)
                embedding = embedding / np.linalg.norm(embedding)
                chunks.append(EmbeddedChunk(chunk, embedding, "test-model"))

        store.add(chunks)

        # Search with filter to book1 only
        query = np.random.rand(384).astype(np.float32)
        results = store.search(query, limit=10, filter_book_ids=[book1])

        # All results should be from book1
        for chunk, score in results:
            assert chunk.book_id.book_id == 1

    def test_search_with_library_filter(self, store):
        """Test search with library filter."""
        # Create chunks for two different libraries
        lib1_book = BookIdentifier("library-uuid-1", 1, "EPUB")
        lib2_book = BookIdentifier("library-uuid-2", 1, "EPUB")

        chunks = []
        for book_id in [lib1_book, lib2_book]:
            chunk = TextChunk(
                id=f"chunk-{book_id.library_id}",
                book_id=book_id,
                text=f"Content from library {book_id.library_id}",
                location=ChunkLocation(0, "ch.xhtml", 0, 100),
                chunk_type=ChunkType.PARAGRAPH,
            )
            embedding = np.random.rand(384).astype(np.float32)
            chunks.append(EmbeddedChunk(chunk, embedding, "test-model"))

        store.add(chunks)

        query = np.random.rand(384).astype(np.float32)
        results = store.search(query, limit=10, filter_libraries=["library-uuid-1"])

        assert len(results) == 1
        assert results[0][0].book_id.library_id == "library-uuid-1"

    def test_clear_profile(self, store, sample_chunks):
        """Test clearing specific profile."""
        store.add(sample_chunks, profile_id="profile-a")
        store.add(sample_chunks, profile_id="profile-b")

        store.clear(profile_id="profile-a")

        assert store.get_chunk_count(profile_id="profile-a") == 0
        assert store.get_chunk_count(profile_id="profile-b") == 5

    def test_clear_all(self, store, sample_chunks):
        """Test clearing entire store."""
        store.add(sample_chunks, profile_id="profile-a")
        store.add(sample_chunks, profile_id="profile-b")

        store.clear()

        assert store.get_chunk_count(profile_id="profile-a") == 0
        assert store.get_chunk_count(profile_id="profile-b") == 0

    def test_get_profiles(self, store, sample_chunks):
        """Test getting list of profiles."""
        store.add(sample_chunks, profile_id="profile-a")
        store.add(sample_chunks, profile_id="profile-b")

        profiles = store.get_profiles()

        assert "profile-a" in profiles
        assert "profile-b" in profiles

    def test_model_id_persistence(self, store):
        """Test model ID get/set."""
        assert store.get_model_id() is None

        store.set_model_id("google:text-embedding-004:768")
        assert store.get_model_id() == "google:text-embedding-004:768"

    def test_upsert_behavior(self, store, sample_chunks):
        """Test that re-adding chunks updates them."""
        store.add(sample_chunks)
        assert store.get_chunk_count() == 5

        # Modify first chunk text and re-add
        modified_chunk = sample_chunks[0]
        modified_chunk.chunk.text = "Modified content"
        store.add([modified_chunk])

        # Should still be 5, not 6
        assert store.get_chunk_count() == 5


class TestChromaDBStoreMetadataReconstruction:
    """Tests for metadata reconstruction from ChromaDB."""

    @pytest.fixture
    def store(self):
        config = VectorStoreConfig(backend="chromadb", path=None)
        store = ChromaDBStore(config)
        store.clear()  # Ensure isolation
        yield store
        store.close()

    def test_chunk_reconstruction_preserves_location(self, store):
        """Test that chunk location is preserved through add/search cycle."""
        book_id = BookIdentifier("test-lib", 1, "PDF")
        chunk = TextChunk(
            id="test-chunk",
            book_id=book_id,
            text="Test content for reconstruction",
            location=ChunkLocation(
                spine_index=3,
                spine_name="page003.html",
                start_offset=150,
                end_offset=300,
                cfi="/2/4/6[page003]",
            ),
            chunk_type=ChunkType.SECTION,
            chapter_title="Important Chapter",
            section_title="Key Section",
            metadata={"page_number": 42},
        )
        embedding = np.random.rand(384).astype(np.float32)
        embedded = EmbeddedChunk(chunk, embedding, "test-model")

        store.add([embedded])

        results = store.search(embedding, limit=1)
        assert len(results) == 1

        result_chunk, _ = results[0]

        # Verify all fields are preserved
        assert result_chunk.id == "test-chunk"
        assert result_chunk.book_id.library_id == "test-lib"
        assert result_chunk.book_id.book_id == 1
        assert result_chunk.book_id.format == "PDF"
        assert result_chunk.location.spine_index == 3
        assert result_chunk.location.spine_name == "page003.html"
        assert result_chunk.location.start_offset == 150
        assert result_chunk.location.end_offset == 300
        assert result_chunk.location.cfi == "/2/4/6[page003]"
        assert result_chunk.chunk_type == ChunkType.SECTION
        assert result_chunk.chapter_title == "Important Chapter"
        assert result_chunk.section_title == "Key Section"


class TestChromaDBStoreADR006Compliance:
    """Tests verifying ADR-006 hybrid query architecture compliance."""

    @pytest.fixture
    def store(self):
        config = VectorStoreConfig(backend="chromadb", path=None)
        store = ChromaDBStore(config)
        store.clear()  # Ensure isolation
        yield store
        store.close()

    def test_filter_book_ids_from_calibre_db_query(self, store):
        """Test that filter_book_ids parameter works for hybrid queries.

        Per ADR-006: First filter books in Calibre DB, then semantic search
        within matching books using filter_book_ids parameter.
        """
        # Simulate multiple books in index
        books = [
            BookIdentifier("lib", i, "EPUB")
            for i in range(10)
        ]

        chunks = []
        for book_id in books:
            chunk = TextChunk(
                id=f"chunk-{book_id.book_id}",
                book_id=book_id,
                text=f"Philosophy content from book {book_id.book_id}",
                location=ChunkLocation(0, "ch.xhtml", 0, 100),
                chunk_type=ChunkType.PARAGRAPH,
            )
            embedding = np.random.rand(384).astype(np.float32)
            chunks.append(EmbeddedChunk(chunk, embedding, "test-model"))

        store.add(chunks)
        assert store.get_chunk_count() == 10

        # Simulate Calibre DB returning books 2, 5, 7 for metadata filter
        # e.g., author:"Heidegger" and #tradition:"continental"
        filtered_books = [books[2], books[5], books[7]]

        query = np.random.rand(384).astype(np.float32)
        results = store.search(query, limit=10, filter_book_ids=filtered_books)

        # All results should be from the filtered books only
        result_book_ids = {chunk.book_id.book_id for chunk, _ in results}
        expected_book_ids = {2, 5, 7}
        assert result_book_ids == expected_book_ids

    def test_empty_filter_returns_empty(self, store):
        """Test that empty filter_book_ids returns empty results."""
        # Add some chunks
        book_id = BookIdentifier("lib", 1, "EPUB")
        chunk = TextChunk(
            id="test-chunk",
            book_id=book_id,
            text="Some content",
            location=ChunkLocation(0, "ch.xhtml", 0, 100),
            chunk_type=ChunkType.PARAGRAPH,
        )
        embedding = np.random.rand(384).astype(np.float32)
        store.add([EmbeddedChunk(chunk, embedding, "test-model")])

        # Search with empty filter (no books match metadata query)
        query = np.random.rand(384).astype(np.float32)
        results = store.search(query, limit=10, filter_book_ids=[])

        assert len(results) == 0
