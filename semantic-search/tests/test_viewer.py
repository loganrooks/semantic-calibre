"""Tests for viewer integration module.

These tests verify the convenience API for Calibre viewer integration.
"""

from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from calibre_semantic.viewer import (
    DEFAULT_VIEWER_PROFILE,
    ViewerSearchResult,
    _create_book_id,
    clear_book_index,
    index_book_for_viewer,
    is_book_indexed,
    search_viewer_book,
)


class TestCreateBookId:
    """Tests for _create_book_id helper."""

    def test_creates_book_identifier(self):
        """Should create a BookIdentifier from path."""
        book_id = _create_book_id("/path/to/book.epub")

        assert book_id.library_id == "viewer"
        assert book_id.format == "EPUB"
        assert isinstance(book_id.book_id, int)

    def test_different_paths_different_ids(self):
        """Different paths should produce different book IDs."""
        id1 = _create_book_id("/path/to/book1.epub")
        id2 = _create_book_id("/path/to/book2.epub")

        assert id1.book_id != id2.book_id

    def test_handles_path_object(self):
        """Should accept Path objects."""
        book_id = _create_book_id(Path("/path/to/book.pdf"))

        assert book_id.format == "PDF"

    def test_custom_library_id(self):
        """Should accept custom library_id."""
        book_id = _create_book_id("/path/to/book.epub", library_id="custom")

        assert book_id.library_id == "custom"


class TestViewerSearchResult:
    """Tests for ViewerSearchResult dataclass."""

    def test_create_result(self):
        """Should create a ViewerSearchResult."""
        result = ViewerSearchResult(
            before="context before",
            text="matched text",
            after="context after",
            offset=100,
            spine_idx=2,
            spine_name="chapter01.xhtml",
            score=0.85,
            chunk_text="full chunk text here",
        )

        assert result.before == "context before"
        assert result.text == "matched text"
        assert result.after == "context after"
        assert result.offset == 100
        assert result.spine_idx == 2
        assert result.spine_name == "chapter01.xhtml"
        assert result.score == 0.85
        assert result.chunk_text == "full chunk text here"


class TestIsBookIndexed:
    """Tests for is_book_indexed function."""

    def test_returns_false_when_not_indexed(self):
        """Should return False for non-indexed book."""
        mock_engine = MagicMock()
        mock_engine.is_indexed.return_value = False

        result = is_book_indexed("/path/to/book.epub", engine=mock_engine)

        assert result is False
        mock_engine.is_indexed.assert_called_once()

    def test_returns_true_when_indexed(self):
        """Should return True for indexed book."""
        mock_engine = MagicMock()
        mock_engine.is_indexed.return_value = True

        result = is_book_indexed("/path/to/book.epub", engine=mock_engine)

        assert result is True

    def test_uses_default_profile(self):
        """Should use default profile when not specified."""
        mock_engine = MagicMock()
        mock_engine.is_indexed.return_value = False

        is_book_indexed("/path/to/book.epub", engine=mock_engine)

        call_kwargs = mock_engine.is_indexed.call_args[1]
        assert call_kwargs["profile_id"] == DEFAULT_VIEWER_PROFILE

    def test_uses_custom_profile(self):
        """Should use custom profile when specified."""
        mock_engine = MagicMock()
        mock_engine.is_indexed.return_value = False

        is_book_indexed(
            "/path/to/book.epub",
            profile_id="custom-profile",
            engine=mock_engine,
        )

        call_kwargs = mock_engine.is_indexed.call_args[1]
        assert call_kwargs["profile_id"] == "custom-profile"


class TestIndexBookForViewer:
    """Tests for index_book_for_viewer function."""

    def test_indexes_book_content(self):
        """Should index spine items."""
        mock_engine = MagicMock()
        mock_engine.index_book_content.return_value = 42

        spine_items = [
            ("chapter01.xhtml", "Chapter 1 content here."),
            ("chapter02.xhtml", "Chapter 2 content here."),
        ]

        result = index_book_for_viewer(
            book_path="/path/to/book.epub",
            spine_items=spine_items,
            engine=mock_engine,
        )

        assert result == 42
        mock_engine.index_book_content.assert_called_once()

    def test_uses_default_profile(self):
        """Should use default profile."""
        mock_engine = MagicMock()
        mock_engine.index_book_content.return_value = 10

        index_book_for_viewer(
            book_path="/path/to/book.epub",
            spine_items=[("ch1.xhtml", "content")],
            engine=mock_engine,
        )

        call_kwargs = mock_engine.index_book_content.call_args[1]
        assert call_kwargs["profile_id"] == DEFAULT_VIEWER_PROFILE


class TestSearchViewerBook:
    """Tests for search_viewer_book function."""

    def test_returns_empty_when_not_indexed_no_auto(self):
        """Should return empty list when not indexed and auto_index=False."""
        mock_engine = MagicMock()
        mock_engine.is_indexed.return_value = False

        results = search_viewer_book(
            query="test query",
            book_path="/path/to/book.epub",
            engine=mock_engine,
            auto_index=False,
        )

        assert results == []
        mock_engine.search.assert_not_called()

    def test_raises_when_not_indexed_no_spine_items(self):
        """Should raise when auto_index=True but no spine_items."""
        mock_engine = MagicMock()
        mock_engine.is_indexed.return_value = False

        with pytest.raises(ValueError, match="spine_items not provided"):
            search_viewer_book(
                query="test query",
                book_path="/path/to/book.epub",
                spine_items=None,
                engine=mock_engine,
                auto_index=True,
            )

    def test_auto_indexes_when_needed(self):
        """Should auto-index when book not indexed and spine_items provided."""
        mock_engine = MagicMock()
        mock_engine.is_indexed.return_value = False
        mock_engine.index_book_content.return_value = 10

        # Mock search results
        mock_results = MagicMock()
        mock_results.results = []
        mock_engine.search.return_value = mock_results

        spine_items = [("ch1.xhtml", "content")]

        search_viewer_book(
            query="test query",
            book_path="/path/to/book.epub",
            spine_items=spine_items,
            engine=mock_engine,
            auto_index=True,
        )

        mock_engine.index_book_content.assert_called_once()

    def test_searches_indexed_book(self):
        """Should search when book is indexed."""
        mock_engine = MagicMock()
        mock_engine.is_indexed.return_value = True

        # Create mock chunk with location
        mock_chunk = MagicMock()
        mock_chunk.text = "This is the matched chunk text."
        mock_chunk.location = MagicMock()
        mock_chunk.location.spine_index = "0"
        mock_chunk.location.char_offset = 100

        mock_results = MagicMock()
        mock_results.results = [(mock_chunk, 0.85)]
        mock_engine.search.return_value = mock_results

        results = search_viewer_book(
            query="test query",
            book_path="/path/to/book.epub",
            engine=mock_engine,
        )

        assert len(results) == 1
        assert isinstance(results[0], ViewerSearchResult)
        assert results[0].score == 0.85
        assert results[0].chunk_text == "This is the matched chunk text."

    def test_respects_limit_and_min_score(self):
        """Should pass limit and min_score to search."""
        mock_engine = MagicMock()
        mock_engine.is_indexed.return_value = True

        mock_results = MagicMock()
        mock_results.results = []
        mock_engine.search.return_value = mock_results

        search_viewer_book(
            query="test query",
            book_path="/path/to/book.epub",
            engine=mock_engine,
            limit=5,
            min_score=0.5,
        )

        call_kwargs = mock_engine.search.call_args[1]
        assert call_kwargs["limit"] == 5
        assert call_kwargs["min_score"] == 0.5


class TestClearBookIndex:
    """Tests for clear_book_index function."""

    def test_removes_book(self):
        """Should remove book from engine."""
        mock_engine = MagicMock()
        mock_engine.remove_book.return_value = 42

        result = clear_book_index("/path/to/book.epub", engine=mock_engine)

        assert result == 42
        mock_engine.remove_book.assert_called_once()

    def test_uses_default_profile(self):
        """Should use default profile."""
        mock_engine = MagicMock()
        mock_engine.remove_book.return_value = 0

        clear_book_index("/path/to/book.epub", engine=mock_engine)

        call_kwargs = mock_engine.remove_book.call_args[1]
        assert call_kwargs["profile_id"] == DEFAULT_VIEWER_PROFILE
