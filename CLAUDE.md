# Semantic Calibre - Project Context

## Overview

This is a **fork of Calibre** (e-book manager) with semantic search capabilities added. The goal is to enable meaning-based search across e-book libraries using vector embeddings.

**Primary Goals:**
1. Cross-library semantic search (find books/passages by meaning)
2. Within-book semantic search (add "Semantic" mode to viewer search)
3. MCP server for AI assistant integration

## Architecture

We use **Option C: Hybrid Adapter Pattern** to minimize fork divergence:

```
┌─────────────────────────────────────────────────────────────────┐
│                   calibre_semantic library                       │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  SemanticSearchEngine                                     │   │
│  │  ├── Chunking (Semantic/Fixed strategies)                │   │
│  │  ├── EmbeddingProvider (CalibreAIAdapter or fallback)    │   │
│  │  └── VectorStore (Memory/SQLite-vec)                     │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

## Repository Structure

```
semantic-calibre/
├── src/calibre/              # Calibre source (synced with upstream)
│   └── gui2/viewer/search.py # Will be modified for semantic search
├── semantic-search/          # Our semantic search library
│   ├── calibre_semantic/     # Main package
│   │   ├── core/             # Types, protocols, factories
│   │   ├── providers/        # Embedding & vector store implementations
│   │   └── search.py         # SemanticSearchEngine
│   └── tests/                # Test suite (pytest)
├── FORK_MAINTENANCE.md       # How to sync with upstream Calibre
└── CLAUDE.md                 # This file
```

## Development Commands

```bash
# Run all tests
cd semantic-search && python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_chunking.py -v

# Run with coverage
python -m pytest tests/ --cov=calibre_semantic

# Check types (when mypy is configured)
mypy calibre_semantic/
```

## Code Conventions

- **TDD Approach**: Write tests first, then implementation
- **Protocol-based design**: Use Python Protocols for abstractions
- **Factory pattern**: Use factories for dynamic provider loading
- **Lazy initialization**: Load heavy dependencies only when needed

### Import Style
```python
from __future__ import annotations
from typing import TYPE_CHECKING, Sequence
if TYPE_CHECKING:
    from calibre_semantic.core.types import SomeType
```

### Test Organization
- One test file per module: `test_<module>.py`
- Test classes grouped by functionality: `TestClassName`
- Fixtures in the test file or `conftest.py`

## Do NOT

- **Do not modify Calibre source** except `src/calibre/gui2/viewer/search.py`
- **Do not commit secrets** or API keys
- **Do not push to main/feature branches** - only push to `claude/` prefixed branches
- **Do not break the embedding provider protocol** - existing implementations depend on it

## Current Status

### Phase 1: Core Library (Complete)
- [x] Embedding provider abstraction
- [x] Vector store abstraction (Memory, SQLite-vec)
- [x] Chunking strategies (Semantic, Fixed)
- [x] SemanticSearchEngine orchestration
- [x] CalibreAIAdapter (Calibre AI integration)
- [x] Book content extraction (EPUB parsing)
- [x] MCP server for AI assistant integration

### Phase 2: Calibre Plugin
- [ ] Plugin skeleton
- [ ] Background indexer
- [ ] Search dialog UI
- [ ] Configuration panel

### Phase 3: Viewer Integration
- [ ] Patch viewer/search.py
- [ ] Test with various book formats

## Key Files

| File | Purpose |
|------|---------|
| `semantic-search/calibre_semantic/core/types.py` | Core types and protocols |
| `semantic-search/calibre_semantic/core/chunking.py` | Text chunking strategies |
| `semantic-search/calibre_semantic/search.py` | Main SemanticSearchEngine |
| `semantic-search/calibre_semantic/extraction/epub.py` | EPUB text extraction |
| `semantic-search/calibre_semantic/mcp/server.py` | MCP server for AI assistants |
| `semantic-search/calibre_semantic/providers/embeddings/calibre_ai.py` | Calibre AI adapter |
| `FORK_MAINTENANCE.md` | How to sync with upstream Calibre |

## Branch Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Tracks upstream Calibre |
| `feature/semantic-search` | Our semantic search development |
| `claude/*` | Claude Code working branches |

## Dependencies

**Core (required):**
- numpy

**Optional:**
- sentence-transformers (local embeddings)
- sqlite-vec (persistent vector storage)
- openai (cloud embeddings)

## Testing Notes

- 148 tests currently passing
- 18 tests skipped (require optional dependencies)
- Use `python -m pytest` (not bare `pytest`) to ensure imports work

## MCP Server Usage

Run the MCP server:
```bash
python -m calibre_semantic.mcp --index-path ./semantic_index.db
```

Or configure in Claude Desktop (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "calibre-semantic": {
      "command": "python",
      "args": ["-m", "calibre_semantic.mcp"],
      "env": {"CALIBRE_SEMANTIC_INDEX": "/path/to/index.db"}
    }
  }
}
```
