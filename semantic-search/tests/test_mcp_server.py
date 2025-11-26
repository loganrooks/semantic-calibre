"""Tests for MCP server.

Tests validate:
- Server initialization
- Tool definitions
- Tool execution
- Error handling
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch
import json

import numpy as np
import pytest

from calibre_semantic.core.types import (
    BookIdentifier,
    ChunkLocation,
    ChunkType,
    SemanticSearchConfig,
    TextChunk,
)


# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def mock_engine():
    """Create a mock SemanticSearchEngine."""
    engine = MagicMock()
    engine.get_stats.return_value = {
        "total_chunks": 100,
        "total_books": 5,
        "model_id": "test-model",
        "embedding_dimension": 384,
    }
    engine.get_indexed_books.return_value = set()
    engine._vector_store = MagicMock()
    engine._vector_store.get_chunk_count.return_value = 0
    return engine


@pytest.fixture
def server(mock_engine):
    """Create a server with mocked engine."""
    from calibre_semantic.mcp.server import SemanticSearchServer

    server = SemanticSearchServer()
    server._engine = mock_engine
    return server


# =============================================================================
# Initialization Tests
# =============================================================================


class TestServerInitialization:
    """Tests for server initialization."""

    def test_server_can_be_created(self) -> None:
        """Server should initialize without errors."""
        from calibre_semantic.mcp.server import SemanticSearchServer

        server = SemanticSearchServer()
        assert server is not None

    def test_server_has_name_and_version(self) -> None:
        """Server should have name and version."""
        from calibre_semantic.mcp.server import SemanticSearchServer

        assert SemanticSearchServer.SERVER_NAME == "calibre-semantic"
        assert SemanticSearchServer.SERVER_VERSION is not None

    def test_handle_initialize_returns_capabilities(self, server) -> None:
        """Initialize should return server capabilities."""
        result = server.handle_initialize({})

        assert "protocolVersion" in result
        assert "capabilities" in result
        assert "serverInfo" in result
        assert result["serverInfo"]["name"] == "calibre-semantic"


# =============================================================================
# Tool Definition Tests
# =============================================================================


class TestToolDefinitions:
    """Tests for tool definitions."""

    def test_tools_are_defined(self) -> None:
        """Server should define tools."""
        from calibre_semantic.mcp.server import SemanticSearchServer

        assert len(SemanticSearchServer.TOOLS) > 0

    def test_each_tool_has_required_fields(self) -> None:
        """Each tool should have name, description, and inputSchema."""
        from calibre_semantic.mcp.server import SemanticSearchServer

        for tool in SemanticSearchServer.TOOLS:
            assert "name" in tool
            assert "description" in tool
            assert "inputSchema" in tool

    def test_handle_list_tools_returns_tools(self, server) -> None:
        """list_tools should return all tool definitions."""
        result = server.handle_list_tools({})

        assert "tools" in result
        assert len(result["tools"]) > 0

    def test_semantic_search_tool_exists(self) -> None:
        """semantic_search tool should be defined."""
        from calibre_semantic.mcp.server import SemanticSearchServer

        tool_names = [t["name"] for t in SemanticSearchServer.TOOLS]
        assert "semantic_search" in tool_names

    def test_index_epub_tool_exists(self) -> None:
        """index_epub tool should be defined."""
        from calibre_semantic.mcp.server import SemanticSearchServer

        tool_names = [t["name"] for t in SemanticSearchServer.TOOLS]
        assert "index_epub" in tool_names


# =============================================================================
# Tool Execution Tests
# =============================================================================


class TestToolExecution:
    """Tests for tool execution."""

    def test_call_unknown_tool_returns_error(self, server) -> None:
        """Calling unknown tool should return error."""
        result = server.handle_call_tool({
            "name": "unknown_tool",
            "arguments": {}
        })

        assert result.get("isError") is True
        assert "Unknown tool" in result["content"][0]["text"]

    def test_semantic_search_calls_engine(self, server, mock_engine) -> None:
        """semantic_search should call engine.search."""
        from calibre_semantic.core.types import SearchResults

        mock_engine.search.return_value = SearchResults(
            query="test",
            results=[],
            total_searched=0,
            search_time_ms=1.0,
            model_id="test",
        )

        result = server.handle_call_tool({
            "name": "semantic_search",
            "arguments": {"query": "test query"}
        })

        mock_engine.search.assert_called_once()
        assert result.get("isError") is None

    def test_get_index_stats_returns_stats(self, server) -> None:
        """get_index_stats should return statistics."""
        result = server.handle_call_tool({
            "name": "get_index_stats",
            "arguments": {}
        })

        assert result.get("isError") is None
        content = json.loads(result["content"][0]["text"])
        assert "total_chunks" in content
        assert "total_books" in content

    def test_list_indexed_books_returns_list(self, server) -> None:
        """list_indexed_books should return book list."""
        result = server.handle_call_tool({
            "name": "list_indexed_books",
            "arguments": {}
        })

        assert result.get("isError") is None
        content = json.loads(result["content"][0]["text"])
        assert "total_books" in content
        assert "books" in content

    def test_remove_book_calls_engine(self, server, mock_engine) -> None:
        """remove_book should call engine.remove_book."""
        mock_engine.remove_book.return_value = 10

        result = server.handle_call_tool({
            "name": "remove_book",
            "arguments": {"book_id": "lib:1:EPUB"}
        })

        mock_engine.remove_book.assert_called_once()
        assert result.get("isError") is None

    def test_invalid_book_id_returns_error(self, server) -> None:
        """Invalid book_id format should return error."""
        result = server.handle_call_tool({
            "name": "remove_book",
            "arguments": {"book_id": "invalid"}
        })

        assert result.get("isError") is True


# =============================================================================
# Search Result Formatting Tests
# =============================================================================


class TestSearchResultFormatting:
    """Tests for search result formatting."""

    def test_search_results_include_required_fields(self, server, mock_engine) -> None:
        """Search results should include all required fields."""
        from calibre_semantic.core.types import SearchResult, SearchResults

        mock_chunk = TextChunk(
            id="chunk-1",
            book_id=BookIdentifier("lib", 1, "EPUB"),
            text="Sample text content",
            location=ChunkLocation(
                spine_index=0,
                spine_name="chapter1.xhtml",
                start_offset=0,
                end_offset=20,
            ),
            chunk_type=ChunkType.PARAGRAPH,
            chapter_title="Chapter 1",
        )

        mock_engine.search.return_value = SearchResults(
            query="test",
            results=[SearchResult(chunk=mock_chunk, score=0.85)],
            total_searched=100,
            search_time_ms=5.5,
            model_id="test-model",
        )

        result = server.handle_call_tool({
            "name": "semantic_search",
            "arguments": {"query": "test"}
        })

        content = json.loads(result["content"][0]["text"])

        assert "query" in content
        assert "results" in content
        assert len(content["results"]) == 1

        first_result = content["results"][0]
        assert "score" in first_result
        assert "text" in first_result
        assert "book_id" in first_result
        assert "chapter" in first_result
        assert "location" in first_result


# =============================================================================
# Error Handling Tests
# =============================================================================


class TestErrorHandling:
    """Tests for error handling."""

    def test_tool_error_returns_error_response(self, server, mock_engine) -> None:
        """Tool errors should return proper error response."""
        mock_engine.search.side_effect = RuntimeError("Test error")

        result = server.handle_call_tool({
            "name": "semantic_search",
            "arguments": {"query": "test"}
        })

        assert result.get("isError") is True
        assert "Error" in result["content"][0]["text"]

    def test_index_nonexistent_epub_returns_error(self, server) -> None:
        """Indexing nonexistent EPUB should return error."""
        result = server.handle_call_tool({
            "name": "index_epub",
            "arguments": {
                "epub_path": "/nonexistent/path.epub",
                "book_id": 1,
            }
        })

        assert result.get("isError") is True
        assert "not found" in result["content"][0]["text"].lower()
