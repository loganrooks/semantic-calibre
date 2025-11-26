"""MCP Server implementation for semantic search.

This module implements the Model Context Protocol (MCP) server that
exposes semantic search functionality to AI assistants.

The server communicates over stdio using JSON-RPC 2.0 protocol.
"""

from __future__ import annotations

import json
import logging
import sys
from pathlib import Path
from typing import Any

from calibre_semantic.core.types import (
    BookIdentifier,
    SemanticSearchConfig,
    VectorStoreConfig,
)
from calibre_semantic.search import SemanticSearchEngine

logger = logging.getLogger(__name__)


class SemanticSearchServer:
    """MCP server for semantic search operations.

    This server exposes semantic search capabilities through the
    Model Context Protocol, allowing AI assistants to:
    - Search for books/passages by meaning
    - Index new EPUB files
    - Manage the search index

    Attributes:
        engine: The SemanticSearchEngine instance
        config: Server configuration
    """

    # Server metadata
    SERVER_NAME = "calibre-semantic"
    SERVER_VERSION = "0.1.0"

    # Tool definitions for MCP
    TOOLS = [
        {
            "name": "semantic_search",
            "description": "Search for books and passages by meaning. Returns relevant text chunks with similarity scores.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query (describe what you're looking for)"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of results (default: 10)",
                        "default": 10
                    },
                    "min_score": {
                        "type": "number",
                        "description": "Minimum similarity score 0-1 (default: 0.3)",
                        "default": 0.3
                    }
                },
                "required": ["query"]
            }
        },
        {
            "name": "search_in_book",
            "description": "Search within a specific book by its ID.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query"
                    },
                    "book_id": {
                        "type": "string",
                        "description": "Book identifier (format: library_id:book_id:format)"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum results",
                        "default": 10
                    }
                },
                "required": ["query", "book_id"]
            }
        },
        {
            "name": "index_epub",
            "description": "Index an EPUB file for semantic search.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "epub_path": {
                        "type": "string",
                        "description": "Path to the EPUB file"
                    },
                    "library_id": {
                        "type": "string",
                        "description": "Library identifier",
                        "default": "default"
                    },
                    "book_id": {
                        "type": "integer",
                        "description": "Book ID within the library"
                    }
                },
                "required": ["epub_path", "book_id"]
            }
        },
        {
            "name": "list_indexed_books",
            "description": "List all books that have been indexed for semantic search.",
            "inputSchema": {
                "type": "object",
                "properties": {}
            }
        },
        {
            "name": "get_index_stats",
            "description": "Get statistics about the semantic search index.",
            "inputSchema": {
                "type": "object",
                "properties": {}
            }
        },
        {
            "name": "remove_book",
            "description": "Remove a book from the semantic search index.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "book_id": {
                        "type": "string",
                        "description": "Book identifier to remove"
                    }
                },
                "required": ["book_id"]
            }
        }
    ]

    def __init__(
        self,
        config: SemanticSearchConfig | None = None,
        index_path: Path | None = None,
    ):
        """Initialize the MCP server.

        Args:
            config: Optional search configuration
            index_path: Optional path for persistent index storage
        """
        if config is None:
            # Create default config with persistent storage if path provided
            if index_path:
                config = SemanticSearchConfig(
                    vector_store=VectorStoreConfig(
                        backend="sqlite-vec",
                        path=index_path,
                    )
                )
            else:
                config = SemanticSearchConfig()

        self._config = config
        self._engine: SemanticSearchEngine | None = None

    @property
    def engine(self) -> SemanticSearchEngine:
        """Lazy initialization of search engine."""
        if self._engine is None:
            self._engine = SemanticSearchEngine(self._config)
        return self._engine

    # =========================================================================
    # MCP Protocol Handlers
    # =========================================================================

    def handle_initialize(self, params: dict[str, Any]) -> dict[str, Any]:
        """Handle MCP initialize request."""
        return {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "tools": {},
            },
            "serverInfo": {
                "name": self.SERVER_NAME,
                "version": self.SERVER_VERSION,
            }
        }

    def handle_list_tools(self, params: dict[str, Any]) -> dict[str, Any]:
        """Handle tools/list request."""
        return {"tools": self.TOOLS}

    def handle_call_tool(self, params: dict[str, Any]) -> dict[str, Any]:
        """Handle tools/call request."""
        tool_name = params.get("name", "")
        arguments = params.get("arguments", {})

        # Dispatch to appropriate handler
        handlers = {
            "semantic_search": self._tool_semantic_search,
            "search_in_book": self._tool_search_in_book,
            "index_epub": self._tool_index_epub,
            "list_indexed_books": self._tool_list_indexed_books,
            "get_index_stats": self._tool_get_index_stats,
            "remove_book": self._tool_remove_book,
        }

        handler = handlers.get(tool_name)
        if handler is None:
            return {
                "content": [{"type": "text", "text": f"Unknown tool: {tool_name}"}],
                "isError": True,
            }

        try:
            result = handler(arguments)
            return {
                "content": [{"type": "text", "text": json.dumps(result, indent=2)}],
            }
        except Exception as e:
            logger.exception(f"Error in tool {tool_name}")
            return {
                "content": [{"type": "text", "text": f"Error: {str(e)}"}],
                "isError": True,
            }

    # =========================================================================
    # Tool Implementations
    # =========================================================================

    def _tool_semantic_search(self, args: dict[str, Any]) -> dict[str, Any]:
        """Execute semantic search."""
        query = args["query"]
        limit = args.get("limit", 10)
        min_score = args.get("min_score", 0.3)

        results = self.engine.search(
            query=query,
            limit=limit,
            min_score=min_score,
        )

        return {
            "query": results.query,
            "total_searched": results.total_searched,
            "search_time_ms": round(results.search_time_ms, 2),
            "results": [
                {
                    "score": round(r.score, 3),
                    "text": r.chunk.text,
                    "book_id": str(r.chunk.book_id),
                    "chapter": r.chunk.chapter_title,
                    "location": {
                        "spine_name": r.chunk.location.spine_name,
                        "spine_index": r.chunk.location.spine_index,
                    }
                }
                for r in results.results
            ]
        }

    def _tool_search_in_book(self, args: dict[str, Any]) -> dict[str, Any]:
        """Search within a specific book."""
        query = args["query"]
        book_id_str = args["book_id"]
        limit = args.get("limit", 10)

        try:
            book_id = BookIdentifier.from_string(book_id_str)
        except ValueError as e:
            raise ValueError(f"Invalid book_id format: {e}")

        results = self.engine.search(
            query=query,
            limit=limit,
            filter_book_ids=[book_id],
        )

        return {
            "query": results.query,
            "book_id": book_id_str,
            "results": [
                {
                    "score": round(r.score, 3),
                    "text": r.chunk.text,
                    "chapter": r.chunk.chapter_title,
                    "location": r.chunk.location.spine_name,
                }
                for r in results.results
            ]
        }

    def _tool_index_epub(self, args: dict[str, Any]) -> dict[str, Any]:
        """Index an EPUB file."""
        epub_path = Path(args["epub_path"])
        library_id = args.get("library_id", "default")
        book_id_num = args["book_id"]

        if not epub_path.exists():
            raise FileNotFoundError(f"EPUB file not found: {epub_path}")

        book_id = BookIdentifier(library_id, book_id_num, "EPUB")

        chunk_count = self.engine.index_epub(
            epub_path=str(epub_path),
            book_id=book_id,
            force_reindex=True,
        )

        return {
            "success": True,
            "book_id": str(book_id),
            "chunks_indexed": chunk_count,
            "message": f"Successfully indexed {chunk_count} chunks from {epub_path.name}"
        }

    def _tool_list_indexed_books(self, args: dict[str, Any]) -> dict[str, Any]:
        """List all indexed books."""
        indexed = self.engine.get_indexed_books()

        return {
            "total_books": len(indexed),
            "books": [
                {
                    "book_id": str(bid),
                    "library": bid.library_id,
                    "id": bid.book_id,
                    "format": bid.format,
                    "chunk_count": self.engine._vector_store.get_chunk_count(bid),
                }
                for bid in indexed
            ]
        }

    def _tool_get_index_stats(self, args: dict[str, Any]) -> dict[str, Any]:
        """Get index statistics."""
        stats = self.engine.get_stats()
        return {
            "total_chunks": stats["total_chunks"],
            "total_books": stats["total_books"],
            "embedding_model": stats["model_id"],
            "embedding_dimension": stats["embedding_dimension"],
        }

    def _tool_remove_book(self, args: dict[str, Any]) -> dict[str, Any]:
        """Remove a book from the index."""
        book_id_str = args["book_id"]

        try:
            book_id = BookIdentifier.from_string(book_id_str)
        except ValueError as e:
            raise ValueError(f"Invalid book_id format: {e}")

        removed_count = self.engine.remove_book(book_id)

        return {
            "success": True,
            "book_id": book_id_str,
            "chunks_removed": removed_count,
        }

    # =========================================================================
    # Server Loop
    # =========================================================================

    def run(self) -> None:
        """Run the MCP server (stdio transport)."""
        logger.info(f"Starting {self.SERVER_NAME} v{self.SERVER_VERSION}")

        for line in sys.stdin:
            try:
                request = json.loads(line)
                response = self._handle_request(request)
                if response:
                    print(json.dumps(response), flush=True)
            except json.JSONDecodeError:
                logger.error(f"Invalid JSON: {line}")
            except Exception as e:
                logger.exception("Error handling request")
                error_response = {
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {"code": -32603, "message": str(e)}
                }
                print(json.dumps(error_response), flush=True)

    def _handle_request(self, request: dict[str, Any]) -> dict[str, Any] | None:
        """Handle a single JSON-RPC request."""
        method = request.get("method", "")
        params = request.get("params", {})
        request_id = request.get("id")

        # Method dispatch
        handlers = {
            "initialize": self.handle_initialize,
            "tools/list": self.handle_list_tools,
            "tools/call": self.handle_call_tool,
        }

        handler = handlers.get(method)
        if handler is None:
            if request_id is not None:
                return {
                    "jsonrpc": "2.0",
                    "id": request_id,
                    "error": {"code": -32601, "message": f"Unknown method: {method}"}
                }
            return None

        result = handler(params)

        if request_id is not None:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": result,
            }

        return None


def run_server(
    index_path: Path | None = None,
    config: SemanticSearchConfig | None = None,
) -> None:
    """Run the MCP server.

    Args:
        index_path: Optional path for persistent index storage
        config: Optional search configuration
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        stream=sys.stderr,
    )

    server = SemanticSearchServer(config=config, index_path=index_path)
    server.run()
