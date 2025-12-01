# Semantic Calibre - Project Context

> **Current Phase:** 2 - Viewer Integration
> **Last Updated:** 2025-12-01

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

**Key Design Decisions:**
- [ADR-001](docs/decisions/001-embedding-profiles.md): Embedding Profiles (not single model)
- [ADR-002](docs/decisions/002-on-demand-indexing.md): On-demand indexing (not auto-index)
- [ADR-003](docs/decisions/003-calibre-ai-integration.md): Integrate with Calibre's AI module
- [ADR-004](docs/decisions/004-minimal-viewer-modification.md): Minimal Calibre source changes

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

- **Modify Calibre source** except `src/calibre/gui2/viewer/search.py` and `src/calibre/ai/*/backend.py`
- **Commit secrets** or API keys
- **Push to main/feature branches** without explicit permission
- **Break the embedding provider protocol** - existing implementations depend on it
- **Auto-index by default** - respect user resources (see ADR-002)

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
| `src/calibre/ai/google/backend.py` | Google AI backend (add embed() here) |

## Branch Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Tracks upstream Calibre |
| `feature/semantic-search` | Our semantic search development |
| `claude/*` | Claude Code working branches |

## Testing Notes

- 234+ tests currently passing (includes compliance + viewer tests)
- 18 tests skipped (require optional dependencies)
- 1 test failing (pytest-asyncio configuration)
- Use `python -m pytest` (not bare `pytest`) to ensure imports work
- See [KI-001, KI-002](docs/ISSUES.md) for skipped test details

## Dependencies

**Core (required):**
- numpy

**Optional:**
- sentence-transformers (local embeddings)
- sqlite-vec (persistent vector storage)
- google-generativeai (Gemini embeddings via Calibre AI)
- openai (OpenAI embeddings via Calibre AI)
