# Semantic Search Integration Architecture

## Overview

This document outlines how `calibre-semantic` integrates with our Calibre fork for semantic search capabilities.

## Architecture Decision

Per [ADR-004](../docs/decisions/004-minimal-viewer-modification.md), we use **direct fork modification** with minimal changes to Calibre source code.

```
┌─────────────────────────────────────────────────────────────────┐
│                        Use Cases                                 │
├─────────────────┬─────────────────┬─────────────────────────────┤
│  MCP Server     │  Viewer Search  │  Library Search UI          │
│  (standalone)   │  (Phase 2)      │  (Phase 3)                  │
├─────────────────┴─────────────────┴─────────────────────────────┤
│                   calibre_semantic (core library)                │
│    ┌──────────────┬───────────────┬──────────────────────┐      │
│    │  Embeddings  │  Vector Store │  Search Engine       │      │
│    │  + Profiles  │  + Profiles   │  + On-demand Index   │      │
│    └──────────────┴───────────────┴──────────────────────┘      │
└─────────────────────────────────────────────────────────────────┘
```

## Component Breakdown

### 1. Core Library (`semantic-search/calibre_semantic/`)

**Location:** `semantic-search/` directory in this repository

**Structure:**
```
calibre_semantic/
├── search.py           # SemanticSearchEngine (main orchestration)
├── core/
│   ├── types.py        # Types, protocols, configuration
│   ├── embeddings.py   # Embedding provider abstraction & factory
│   ├── vectordb.py     # Vector store abstraction & factory
│   ├── chunking.py     # Document chunking strategies
│   └── profiles.py     # Embedding profiles & book index status
├── providers/
│   ├── embeddings/
│   │   ├── sentence_transformers.py  # Local models
│   │   └── calibre_ai.py             # Calibre AI adapter
│   └── vectordb/
│       ├── memory.py       # In-memory (testing)
│       └── sqlite_vec.py   # SQLite-vec (production)
├── extraction/
│   └── epub.py         # EPUB text extraction
└── mcp/
    └── server.py       # MCP protocol server
```

**NO Calibre dependency** - can be used independently.

### 2. Calibre Fork Modifications

Per ADR-004, we modify **only** these Calibre files:

| File | Purpose |
|------|---------|
| `src/calibre/gui2/viewer/search.py` | Add "Semantic" search mode to viewer |
| `src/calibre/ai/*/backend.py` | Add `embed()` functions for AI backends |

**Why minimal changes?**
- Easy to merge upstream Calibre updates
- Clear separation of concerns
- Reduces maintenance burden

### 3. Integration Points

#### Viewer In-Book Search (Phase 2)

```python
# src/calibre/gui2/viewer/search.py - Our modification

class SearchPanel:
    def setup_ui(self):
        # Existing modes
        self.query_type.addItem(_('Contains'), 'normal')
        self.query_type.addItem(_('Whole words'), 'word')
        self.query_type.addItem(_('Nearby words'), 'near')
        self.query_type.addItem(_('Regex'), 'regex')

        # NEW: Semantic mode
        self.query_type.addItem(_('Semantic'), 'semantic')

    def do_search(self, query):
        if self.mode == 'semantic':
            from calibre_semantic import search_viewer_book
            return search_viewer_book(
                book_path=self.current_book,
                query=query,
                profile_id=self.selected_profile,
            )
```

#### Library Search UI (Phase 3)

```python
# Future: Main Calibre GUI semantic search
from calibre_semantic import SemanticSearchEngine
from calibre_semantic.core.profiles import ProfileManager

class SemanticSearchDialog:
    def __init__(self, library_db):
        self.profile_manager = ProfileManager()
        self.engine = SemanticSearchEngine(
            config,
            profile_manager=self.profile_manager,
        )

    def search(self, query, profile_id):
        results = self.engine.search(query, profile_id=profile_id)
        # Display results with book covers, navigate to library view
```

#### MCP Server (Standalone)

```python
# Completely independent of Calibre
from calibre_semantic import SemanticSearchEngine
from calibre_semantic.mcp import MCPServer

engine = SemanticSearchEngine(config)
server = MCPServer(engine)
server.run()  # Listens on stdin/stdout
```

## Repository Structure

```
semantic-calibre/                    # Calibre fork root
├── src/calibre/                     # Calibre source (synced with upstream)
│   ├── ai/                          # Calibre AI module
│   │   └── google/backend.py        # Modified: add embed()
│   └── gui2/viewer/search.py        # Modified: add Semantic mode
├── semantic-search/                 # Our semantic search library
│   ├── calibre_semantic/            # Main package
│   └── tests/                       # Test suite
├── docs/
│   ├── decisions/                   # ADR files
│   ├── ISSUES.md                    # Design decisions index
│   └── CALIBRE_AI.md                # AI integration guide
├── ROADMAP.md                       # Progress tracking
├── CLAUDE.md                        # Development guide
└── FORK_MAINTENANCE.md              # Upstream sync procedures
```

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Direct fork, not plugin | Viewer integration requires source modification |
| Minimal Calibre changes | Easy upstream sync (see FORK_MAINTENANCE.md) |
| Profile-based storage | Support multiple embedding models |
| On-demand indexing | Respect user resources (ADR-002) |
| Calibre AI integration | Reuse existing AI configuration (ADR-003) |

## Development Phases

### Phase 1: Core Library ✅
- Embedding provider abstraction
- Vector store abstraction
- Chunking strategies
- SemanticSearchEngine
- MCP server

### Phase 1.5: Profiles & Integration ✅
- Embedding profiles system
- Calibre AI adapter
- On-demand indexing
- Profile-aware vector stores

### Phase 2: Viewer Integration 🚧
- Add "Semantic" search mode to viewer
- On-demand book indexing
- Result navigation
- Profile selection UI

### Phase 3: Library Search UI (Planned)
- Cross-book semantic search dialog
- Bulk indexing UI
- Profile management UI

## Sync with Upstream Calibre

See [FORK_MAINTENANCE.md](../FORK_MAINTENANCE.md) for detailed procedures.

Key principle: Keep our changes isolated to specific files so merging upstream updates is straightforward.
