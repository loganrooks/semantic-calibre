"""MCP (Model Context Protocol) server for semantic search.

This module provides an MCP server that exposes semantic search
capabilities to AI assistants like Claude.

## Tools Provided

- `semantic_search`: Search across indexed books by meaning
- `search_in_book`: Search within a specific book
- `index_epub`: Index an EPUB file
- `list_indexed_books`: List all indexed books
- `get_index_stats`: Get indexing statistics
- `remove_book`: Remove a book from the index

## Usage

Run the server from command line:
    python -m calibre_semantic.mcp

Or in Claude Desktop's config (claude_desktop_config.json):
    {
      "mcpServers": {
        "calibre-semantic": {
          "command": "python",
          "args": ["-m", "calibre_semantic.mcp"],
          "env": {
            "CALIBRE_LIBRARY": "/path/to/calibre/library"
          }
        }
      }
    }
"""

from calibre_semantic.mcp.server import SemanticSearchServer, run_server

__all__ = [
    "SemanticSearchServer",
    "run_server",
]
