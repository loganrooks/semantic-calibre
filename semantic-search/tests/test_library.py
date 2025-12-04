"""Tests for library integration module.

These tests verify the Phase 3 library integration components:
- MetadataFilterBuilder: Building Calibre search queries
- IndexingJob: Background indexing
- LibrarySearchEngine: Hybrid search orchestration
"""

from __future__ import annotations

import pytest
from unittest.mock import MagicMock, patch
from dataclasses import dataclass
from typing import Any

from calibre_semantic.library import (
    MetadataFilter,
    MetadataFilterBuilder,
    IndexStatus,
    IndexingResults,
    IndexingJob,
    LibrarySearchResult,
    LibrarySearchResults,
    LibrarySearchEngine,
    get_library_engine,
    DEFAULT_LIBRARY_PROFILE,
)


# =============================================================================
# MetadataFilter Tests
# =============================================================================

class TestMetadataFilter:
    """Tests for the MetadataFilter dataclass."""

    def test_simple_filter(self):
        """Test simple filter conversion to query."""
        f = MetadataFilter(field="authors", values=["John Smith"])
        assert f.to_query() == 'authors:"John Smith"'

    def test_multiple_values(self):
        """Test filter with multiple values (OR)."""
        f = MetadataFilter(field="tags", values=["philosophy", "ethics"])
        assert f.to_query() == "(tags:philosophy OR tags:ethics)"

    def test_exact_match_operator(self):
        """Test exact match operator."""
        f = MetadataFilter(field="authors", operator="=", values=["John Smith"])
        assert f.to_query() == 'authors="John Smith"'

    def test_negated_filter(self):
        """Test negated filter."""
        f = MetadataFilter(field="tags", values=["fiction"], negate=True)
        assert f.to_query() == "NOT tags:fiction"

    def test_empty_values(self):
        """Test filter with no values returns empty string."""
        f = MetadataFilter(field="authors", values=[])
        assert f.to_query() == ""

    def test_value_without_spaces(self):
        """Test value without spaces is not quoted."""
        f = MetadataFilter(field="tags", values=["philosophy"])
        assert f.to_query() == "tags:philosophy"

    def test_comparison_operator(self):
        """Test comparison operators."""
        f = MetadataFilter(field="rating", operator=">=", values=["4"])
        assert f.to_query() == "rating>=4"


# =============================================================================
# MetadataFilterBuilder Tests
# =============================================================================

class TestMetadataFilterBuilder:
    """Tests for the MetadataFilterBuilder class."""

    def test_empty_builder(self):
        """Test empty builder produces empty query."""
        builder = MetadataFilterBuilder()
        assert builder.build() == ""
        assert builder.is_empty()

    def test_add_authors(self):
        """Test adding author filter."""
        builder = MetadataFilterBuilder()
        builder.add_authors(["John Smith"])
        assert builder.build() == 'authors:"John Smith"'
        assert not builder.is_empty()

    def test_add_multiple_authors(self):
        """Test adding multiple authors (OR)."""
        builder = MetadataFilterBuilder()
        builder.add_authors(["John Smith", "Jane Doe"])
        assert builder.build() == '(authors:"John Smith" OR authors:"Jane Doe")'

    def test_add_tags(self):
        """Test adding tag filter."""
        builder = MetadataFilterBuilder()
        builder.add_tags(["philosophy", "ethics"])
        assert builder.build() == "(tags:philosophy OR tags:ethics)"

    def test_add_custom_column(self):
        """Test adding custom column filter."""
        builder = MetadataFilterBuilder()
        builder.add_custom("#tradition", ["continental"])
        assert builder.build() == "#tradition:continental"

    def test_custom_column_without_hash(self):
        """Test custom column name without # prefix is fixed."""
        builder = MetadataFilterBuilder()
        builder.add_custom("tradition", ["continental"])
        assert builder.build() == "#tradition:continental"

    def test_chain_multiple_filters(self):
        """Test chaining multiple filters."""
        builder = MetadataFilterBuilder()
        builder.add_authors(["Heidegger"]).add_tags(["phenomenology"])
        result = builder.build()
        assert "authors:Heidegger" in result
        assert "tags:phenomenology" in result
        assert " AND " in result

    def test_add_rating_range(self):
        """Test adding rating filter."""
        builder = MetadataFilterBuilder()
        builder.add_rating(min_rating=4, max_rating=5)
        result = builder.build()
        assert "rating>=4" in result
        assert "rating<=5" in result

    def test_add_date_range(self):
        """Test adding date range filter."""
        builder = MetadataFilterBuilder()
        builder.add_date_range("pubdate", start="2020-01-01", end="2023-12-31")
        result = builder.build()
        assert "pubdate>2020-01-01" in result
        assert "pubdate<2023-12-31" in result

    def test_add_formats(self):
        """Test adding format filter."""
        builder = MetadataFilterBuilder()
        builder.add_formats(["epub", "pdf"])
        result = builder.build()
        assert "EPUB" in result
        assert "PDF" in result

    def test_add_series(self):
        """Test adding series filter."""
        builder = MetadataFilterBuilder()
        builder.add_series(["Lord of the Rings"])
        assert builder.build() == 'series:"Lord of the Rings"'

    def test_add_publisher(self):
        """Test adding publisher filter."""
        builder = MetadataFilterBuilder()
        builder.add_publisher(["Penguin Books"])
        assert builder.build() == 'publisher:"Penguin Books"'

    def test_add_languages(self):
        """Test adding language filter."""
        builder = MetadataFilterBuilder()
        builder.add_languages(["English", "German"])
        result = builder.build()
        assert "languages:English" in result
        assert "languages:German" in result

    def test_negated_filter(self):
        """Test negated filter."""
        builder = MetadataFilterBuilder()
        builder.add_tags(["fiction"], negate=True)
        assert builder.build() == "NOT tags:fiction"

    def test_clear(self):
        """Test clearing all filters."""
        builder = MetadataFilterBuilder()
        builder.add_authors(["Test"])
        builder.clear()
        assert builder.is_empty()
        assert builder.build() == ""

    def test_complex_filter(self):
        """Test complex filter with multiple conditions."""
        builder = MetadataFilterBuilder()
        builder.add_authors(["Husserl", "Heidegger"])
        builder.add_tags(["phenomenology"])
        builder.add_custom("#tradition", ["continental"])
        builder.add_rating(min_rating=4)

        result = builder.build()

        # All parts should be present
        assert "Husserl" in result
        assert "Heidegger" in result
        assert "phenomenology" in result
        assert "#tradition:continental" in result
        assert "rating>=4" in result

        # Should be joined with AND
        assert result.count(" AND ") == 3


# =============================================================================
# IndexingResults Tests
# =============================================================================

class TestIndexingResults:
    """Tests for the IndexingResults dataclass."""

    def test_empty_results(self):
        """Test empty results."""
        results = IndexingResults()
        assert results.total_processed == 0
        assert results.success_rate == 1.0  # No failures

    def test_with_succeeded(self):
        """Test with successful indexes."""
        results = IndexingResults(succeeded=[1, 2, 3])
        assert results.total_processed == 3
        assert results.success_rate == 1.0

    def test_with_mixed_results(self):
        """Test with mixed success/failure."""
        results = IndexingResults(
            succeeded=[1, 2],
            failed=[(3, "Error")],
            skipped=[4],
        )
        assert results.total_processed == 4
        assert results.success_rate == pytest.approx(2/3)

    def test_all_failed(self):
        """Test when all fail."""
        results = IndexingResults(
            failed=[(1, "Error 1"), (2, "Error 2")],
        )
        assert results.success_rate == 0.0


# =============================================================================
# IndexingJob Tests
# =============================================================================

class TestIndexingJob:
    """Tests for the IndexingJob class."""

    def test_job_initialization(self):
        """Test job initialization."""
        mock_db = MagicMock()
        mock_engine = MagicMock()

        job = IndexingJob(
            db=mock_db,
            book_ids=[1, 2, 3],
            profile_id="test-profile",
            engine=mock_engine,
        )

        assert job.book_ids == [1, 2, 3]
        assert job.profile_id == "test-profile"
        assert not job.cancelled

    def test_cancel(self):
        """Test job cancellation."""
        mock_db = MagicMock()
        mock_engine = MagicMock()

        job = IndexingJob(
            db=mock_db,
            book_ids=[1, 2, 3],
            profile_id="test-profile",
            engine=mock_engine,
        )

        job.cancel()
        assert job.cancelled


# =============================================================================
# LibrarySearchResult Tests
# =============================================================================

class TestLibrarySearchResult:
    """Tests for LibrarySearchResult dataclass."""

    def test_result_creation(self):
        """Test creating a search result."""
        result = LibrarySearchResult(
            book_id=123,
            title="Being and Time",
            authors=["Martin Heidegger"],
            score=0.92,
            chunk_text="The question of the meaning of Being...",
        )

        assert result.book_id == 123
        assert result.title == "Being and Time"
        assert result.score == 0.92


# =============================================================================
# LibrarySearchResults Tests
# =============================================================================

class TestLibrarySearchResults:
    """Tests for LibrarySearchResults dataclass."""

    def test_results_collection(self):
        """Test results collection."""
        results = LibrarySearchResults(
            results=[
                LibrarySearchResult(
                    book_id=1,
                    title="Test Book",
                    authors=["Author"],
                    score=0.9,
                    chunk_text="Some text",
                )
            ],
            total_matches=1,
            query="test query",
            metadata_filter="authors:Author",
            profile_id="default",
            search_time_ms=50.0,
        )

        assert len(results.results) == 1
        assert results.total_matches == 1
        assert results.query == "test query"
        assert results.search_time_ms == 50.0


# =============================================================================
# MetadataFilterBuilder Edge Cases
# =============================================================================

class TestMetadataFilterBuilderEdgeCases:
    """Edge case tests for MetadataFilterBuilder."""

    def test_empty_author_list(self):
        """Test adding empty author list does nothing."""
        builder = MetadataFilterBuilder()
        builder.add_authors([])
        assert builder.is_empty()

    def test_none_values_in_list(self):
        """Test list with string values works."""
        builder = MetadataFilterBuilder()
        builder.add_tags(["tag1", "tag2"])
        assert "tag1" in builder.build()

    def test_special_characters_in_value(self):
        """Test values with special characters are quoted."""
        builder = MetadataFilterBuilder()
        builder.add_authors(["O'Brien, Patrick"])
        # Values with spaces are quoted
        assert "O'Brien" in builder.build()

    def test_fluent_interface(self):
        """Test fluent interface returns self."""
        builder = MetadataFilterBuilder()
        result = builder.add_authors(["Test"]).add_tags(["tag"])
        assert result is builder


# =============================================================================
# IndexStatus Enum Tests
# =============================================================================

class TestIndexStatus:
    """Tests for IndexStatus enum."""

    def test_status_values(self):
        """Test enum values."""
        assert IndexStatus.NOT_INDEXED.value == "not_indexed"
        assert IndexStatus.INDEXING.value == "indexing"
        assert IndexStatus.COMPLETE.value == "complete"
        assert IndexStatus.FAILED.value == "failed"


# =============================================================================
# Integration Tests (with mocks)
# =============================================================================

class TestLibrarySearchEngineWithMocks:
    """Integration tests for LibrarySearchEngine using mocks."""

    @pytest.fixture
    def mock_db(self):
        """Create a mock Calibre database."""
        db = MagicMock()
        db.search.return_value = {1, 2, 3}
        db.all_book_ids.return_value = frozenset([1, 2, 3, 4, 5])
        db.field_for.side_effect = lambda name, book_id, default_value=None: {
            "title": f"Book {book_id}",
            "authors": [f"Author {book_id}"],
        }.get(name, default_value)
        db.library_id = "test-library"
        db.dbpath = "/tmp/test/metadata.db"
        return db

    @pytest.fixture
    def mock_engine(self):
        """Create a mock semantic search engine."""
        engine = MagicMock()
        engine.is_indexed.return_value = True
        engine.search.return_value = MagicMock(results=[])
        engine.get_profiles.return_value = []
        engine.get_stats.return_value = {"chunk_count": 0}
        return engine

    def test_engine_creation(self, mock_db):
        """Test LibrarySearchEngine can be created."""
        engine = LibrarySearchEngine(db=mock_db)
        assert engine.db is mock_db

    def test_search_with_metadata_filter(self, mock_db, mock_engine):
        """Test search with metadata filter uses Calibre DB first."""
        library_engine = LibrarySearchEngine(
            db=mock_db,
            engine=mock_engine,
        )

        filter_builder = MetadataFilterBuilder()
        filter_builder.add_authors(["Test Author"])

        results = library_engine.search(
            query="test query",
            metadata_filter=filter_builder,
        )

        # Should have called Calibre DB search
        mock_db.search.assert_called_once()
        call_args = mock_db.search.call_args[0]
        assert "authors" in call_args[0]

        # Should have called semantic search engine
        mock_engine.search.assert_called_once()

    def test_search_without_filter(self, mock_db, mock_engine):
        """Test search without metadata filter."""
        library_engine = LibrarySearchEngine(
            db=mock_db,
            engine=mock_engine,
        )

        results = library_engine.search(query="test query")

        # Should NOT have called Calibre DB search
        mock_db.search.assert_not_called()

        # Should have called semantic search engine
        mock_engine.search.assert_called_once()

    def test_is_book_indexed(self, mock_db, mock_engine):
        """Test checking if a book is indexed."""
        library_engine = LibrarySearchEngine(
            db=mock_db,
            engine=mock_engine,
        )

        result = library_engine.is_book_indexed(book_id=1)

        assert result is True
        mock_engine.is_indexed.assert_called_once()

    def test_get_indexed_books(self, mock_db, mock_engine):
        """Test getting list of indexed books."""
        from calibre_semantic.core.types import BookIdentifier

        mock_engine.get_indexed_books.return_value = [
            BookIdentifier(library_id="test", book_id=1, format="EPUB"),
            BookIdentifier(library_id="test", book_id=2, format="EPUB"),
        ]

        library_engine = LibrarySearchEngine(
            db=mock_db,
            engine=mock_engine,
        )

        result = library_engine.get_indexed_books()

        assert result == [1, 2]

    def test_get_profiles(self, mock_db, mock_engine):
        """Test getting embedding profiles."""
        library_engine = LibrarySearchEngine(
            db=mock_db,
            engine=mock_engine,
        )

        library_engine.get_profiles()

        mock_engine.get_profiles.assert_called_once()

    def test_get_stats(self, mock_db, mock_engine):
        """Test getting index statistics."""
        library_engine = LibrarySearchEngine(
            db=mock_db,
            engine=mock_engine,
        )

        library_engine.get_stats()

        mock_engine.get_stats.assert_called_once()


# =============================================================================
# get_library_engine Tests
# =============================================================================

class TestGetLibraryEngine:
    """Tests for the get_library_engine convenience function."""

    def test_caches_engine(self):
        """Test that engines are cached per database."""
        mock_db1 = MagicMock()
        mock_db1.dbpath = "/path/to/db1.db"

        mock_db2 = MagicMock()
        mock_db2.dbpath = "/path/to/db2.db"

        # Clear any existing cache
        if hasattr(get_library_engine, "_cache"):
            get_library_engine._cache.clear()

        # Same DB should return same engine
        with patch.object(LibrarySearchEngine, '_create_engine'):
            engine1a = get_library_engine(mock_db1)
            engine1b = get_library_engine(mock_db1)
            assert engine1a is engine1b

            # Different DB should return different engine
            engine2 = get_library_engine(mock_db2)
            assert engine2 is not engine1a


# =============================================================================
# Default Profile Tests
# =============================================================================

class TestDefaultProfile:
    """Tests for default profile constant."""

    def test_default_profile_value(self):
        """Test default profile has expected value."""
        assert DEFAULT_LIBRARY_PROFILE == "library-default"
