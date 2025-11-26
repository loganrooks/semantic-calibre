"""Command-line entry point for MCP server.

Usage:
    python -m calibre_semantic.mcp [--index-path PATH]

Environment variables:
    CALIBRE_SEMANTIC_INDEX: Path to persistent index database
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path


def main() -> None:
    """Main entry point for MCP server."""
    parser = argparse.ArgumentParser(
        description="Calibre Semantic Search MCP Server"
    )
    parser.add_argument(
        "--index-path",
        type=Path,
        default=None,
        help="Path to persistent index database",
    )
    args = parser.parse_args()

    # Check environment variable
    index_path = args.index_path
    if index_path is None:
        env_path = os.environ.get("CALIBRE_SEMANTIC_INDEX")
        if env_path:
            index_path = Path(env_path)

    from calibre_semantic.mcp.server import run_server
    run_server(index_path=index_path)


if __name__ == "__main__":
    main()
