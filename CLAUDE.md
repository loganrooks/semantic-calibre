# Semantic Calibre - Project Context

> **Current Phase:** 3 - Library Search UI (In Progress)
> **Last Updated:** 2025-12-03
> **Phase 2 Status:** Complete (PR pending)

## Quick Links

| Document | Purpose |
|----------|---------|
| [ROADMAP.md](ROADMAP.md) | Progress tracking and planned features |
| [docs/ISSUES.md](docs/ISSUES.md) | Design decisions index and known issues |
| [docs/CALIBRE_AI.md](docs/CALIBRE_AI.md) | Calibre AI integration guide |
| [FORK_MAINTENANCE.md](FORK_MAINTENANCE.md) | Upstream sync procedures |
| [semantic-search/DESIGN.md](semantic-search/DESIGN.md) | Library architecture |

## Overview

This is a **fork of Calibre** (e-book manager) with semantic search capabilities. Find books and passages by meaning, not just keywords.

**Key Design Decisions (ADRs):**
- [ADR-001](docs/decisions/001-embedding-profiles.md): Embedding Profiles (not single model)
- [ADR-002](docs/decisions/002-on-demand-indexing.md): On-demand indexing (not auto-index)
- [ADR-003](docs/decisions/003-calibre-ai-integration.md): Integrate with Calibre's AI module
- [ADR-004](docs/decisions/004-minimal-viewer-modification.md): Minimal Calibre source changes
- [ADR-005](docs/decisions/005-vector-index-strategies.md): Vector index strategies (SQLite-vec for viewer, ChromaDB/HNSW for library)
- [ADR-006](docs/decisions/006-hybrid-metadata-filtering.md): Hybrid metadata filtering (Calibre DB + Vector Store)
- [ADR-007](docs/decisions/007-library-ui-integration.md): Library UI integration (minimal modification)
- [ADR-008](docs/decisions/008-background-indexing.md): Background indexing architecture

## Repository Structure

```
semantic-calibre/
├── src/calibre/              # Calibre source (synced with upstream)
│   ├── ai/                   # Calibre AI module (we extend this)
│   └── gui2/viewer/search.py # Only viewer file we modify
├── semantic-search/          # Our semantic search library
│   ├── calibre_semantic/     # Main package
│   │   ├── core/             # Types, protocols, factories
│   │   ├── providers/        # Embedding & vector store implementations
│   │   └── search.py         # SemanticSearchEngine
│   └── tests/                # Test suite (pytest)
├── docs/                     # Documentation
│   ├── ISSUES.md             # Decision index & known issues
│   ├── CALIBRE_AI.md         # AI integration guide
│   └── decisions/            # ADR files
├── ROADMAP.md                # Project roadmap
├── FORK_MAINTENANCE.md       # Upstream sync guide
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

# Check project status
# Use /status slash command
```

## Code Conventions

### TDD Approach
Write tests first, then implementation. Use `/implement <feature>` slash command.

### Import Style
```python
from __future__ import annotations
from typing import TYPE_CHECKING, Sequence
if TYPE_CHECKING:
    from calibre_semantic.core.types import SomeType
```

### Protocol-Based Design
Use Python Protocols for abstractions. See `core/types.py` for examples.

## Do NOT

- **Modify Calibre source** except approved files (see Key Files section)
- **Commit secrets** or API keys
- **Push to main/feature branches** without explicit permission
- **Break the embedding provider protocol** - existing implementations depend on it
- **Auto-index by default** - respect user resources (see ADR-002)

## Phase 3 Notes

Phase 3 adds semantic search to the main Calibre library (cross-book search) with **metadata-aware filtering**.

**Key ADRs:**
- [ADR-005](docs/decisions/005-vector-index-strategies.md): ChromaDB with HNSW for library search
- [ADR-006](docs/decisions/006-hybrid-metadata-filtering.md): Hybrid query architecture
- [ADR-007](docs/decisions/007-library-ui-integration.md): Library UI integration strategy
- [ADR-008](docs/decisions/008-background-indexing.md): Background indexing architecture

**Hybrid Query Architecture** (per ADR-006):
1. Filter books by metadata in Calibre DB (authors, tags, custom columns)
2. Semantic search within matching books via ChromaDB

**Progress:**
- ✅ **ChromaDB Integration** - Provider implemented (`providers/vectordb/chromadb.py`), 19 tests passing
- ✅ **Library Integration API** - `calibre_semantic/library.py` with hybrid search orchestration
- ✅ **MetadataFilterBuilder** - Fluent API for Calibre search syntax
- ✅ **Library UI** - Search dialog and profile manager (per ADR-007)
- ✅ **Index Actions** - Bulk indexing with progress, clear index

**Remaining:**
- Right-click context menu integration
- Book covers in search results
- Saved filter presets

**Calibre Metadata Available:**
- Built-in: `authors`, `tags`, `series`, `publisher`, `languages`, `rating`, `pubdate`, `formats`
- Custom columns: Any user-defined `#column` (enumeration, text, bool, rating, datetime)

Follow the same minimal modification approach as Phase 2 (per ADR-007). Prefer adding new files over modifying existing Calibre code where possible.

## Maintenance Protocol

### Automated Compliance Checks

Run these before major commits:

```bash
# Protocol/Implementation sync + ADR compliance
cd semantic-search && python -m pytest tests/test_protocol_compliance.py -v

# Full test suite
python -m pytest tests/ -v
```

The compliance tests verify:
- Protocol signatures match implementation signatures
- ADR-002: `index_on_add` defaults to `False`
- All BaseVectorStore methods exist in VectorStore Protocol

### Documentation Sync Points

These files must stay synchronized:

| Files | What to sync |
|-------|--------------|
| CLAUDE.md ↔ ROADMAP.md | Current Phase must match |
| DESIGN.md ↔ actual code | Package structure must match |
| ARCHITECTURE.md | Must reflect fork approach (not plugin) |
| ADRs ↔ code | Implementation must follow decisions |

### When to Update Documentation

| Event | Action |
|-------|--------|
| Complete ROADMAP milestone | Update ROADMAP.md checkboxes, CLAUDE.md phase |
| Change phase | Update BOTH CLAUDE.md AND ROADMAP.md |
| Make design decision | Create ADR in `docs/decisions/` |
| Add/remove module | Update DESIGN.md package structure |
| Modify Protocol | Run compliance tests, update if needed |

### Before Each Phase Change Checklist

```
1. [ ] Run compliance tests: pytest tests/test_protocol_compliance.py -v
2. [ ] Run full test suite: pytest tests/ -v
3. [ ] Update ROADMAP.md phase status
4. [ ] Update CLAUDE.md "Current Phase" to match ROADMAP.md
5. [ ] Update CLAUDE.md "Last Updated" date
6. [ ] Verify DESIGN.md package structure matches reality
7. [ ] Commit with descriptive message
```

### Slash Commands

| Command | Purpose |
|---------|---------|
| `/status` | Show roadmap progress and test status |
| `/test` | Run the semantic-search test suite |
| `/review` | Check for documentation drift and implementation mismatches |
| `/implement <feature>` | TDD implementation workflow |
| `/sync-upstream` | Sync with upstream Calibre |

## Key Files

| File | Purpose |
|------|---------|
| `semantic-search/calibre_semantic/core/types.py` | Core types and protocols |
| `semantic-search/calibre_semantic/core/chunking.py` | Text chunking strategies |
| `semantic-search/calibre_semantic/search.py` | Main SemanticSearchEngine |
| `semantic-search/calibre_semantic/providers/embeddings/calibre_ai.py` | Calibre AI adapter |
| `semantic-search/calibre_semantic/viewer.py` | Viewer integration API |
| `src/calibre/gui2/viewer/search.py` | Viewer search (Phase 2) |
| `src/calibre/ai/google/backend.py` | Google AI backend (embed()) |

### Phase 3 Target Files (Library Search UI)
Per [ADR-007](docs/decisions/007-library-ui-integration.md):

| File | Purpose | Status |
|------|---------|--------|
| `semantic-search/calibre_semantic/providers/vectordb/chromadb.py` | ChromaDB vector store | ✅ Complete |
| `semantic-search/calibre_semantic/library.py` | Library integration API | ✅ Complete |
| `src/calibre/gui2/actions/semantic_search.py` | NEW: Menu action | ✅ Complete |
| `src/calibre/gui2/semantic_search/__init__.py` | NEW: Package | ✅ Complete |
| `src/calibre/gui2/semantic_search/dialog.py` | NEW: Search dialog | ✅ Complete |
| `src/calibre/gui2/semantic_search/profile_manager.py` | NEW: Profile manager | ✅ Complete |
| `src/calibre/customize/builtins.py` | MODIFY: Register action | ✅ Complete |
| `src/calibre/gui2/library/views.py` | MODIFY: Context menu | ⏳ Planned |

## Branch Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Tracks upstream Calibre |
| `feature/semantic-search` | Our semantic search development |
| `claude/*` | Claude Code working branches |

## Testing Notes

- 254+ tests currently passing (includes compliance + viewer + ChromaDB tests)
- 19 new tests for ChromaDB provider (ADR-006 compliance)
- 18 tests skipped (require optional dependencies)
- Use `python -m pytest` (not bare `pytest`) to ensure imports work
- See [KI-001, KI-002](docs/ISSUES.md) for skipped test details

## Dependencies

**Core (required):**
- numpy

**Phase 3 (library search):**
- chromadb (primary vector store with HNSW indexing and metadata filtering)

**Optional:**
- sentence-transformers (local embeddings)
- sqlite-vec (lightweight vector storage, used in Phase 2 viewer)
- google-generativeai (Gemini embeddings via Calibre AI)
- openai (OpenAI embeddings via Calibre AI)

**For Windows Build:**
Add to Calibre's `pyproject.toml`: `numpy`, `chromadb`
(openai SDK not needed - Calibre's AI module uses urllib directly)
