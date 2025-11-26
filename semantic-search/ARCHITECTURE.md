# Semantic Search Integration Architecture

## Overview

This document outlines how `calibre-semantic` integrates with Calibre for different use cases.

## Architecture Decision

We use a **layered approach** with clear separation:

```
┌─────────────────────────────────────────────────────────────────┐
│                        Use Cases                                 │
├─────────────────┬─────────────────┬─────────────────────────────┤
│  MCP Server     │  Calibre Plugin │  Viewer Integration         │
│  (standalone)   │  (installable)  │  (requires modification)    │
├─────────────────┴─────────────────┴─────────────────────────────┤
│                   calibre-semantic (core library)                │
│    ┌──────────────┬───────────────┬──────────────────────┐      │
│    │  Embeddings  │  Vector Store │  Search Engine       │      │
│    └──────────────┴───────────────┴──────────────────────┘      │
└─────────────────────────────────────────────────────────────────┘
```

## Component Breakdown

### 1. Core Library (`calibre-semantic`)

**Repository:** Standalone package, published to PyPI

**Structure:**
```
calibre-semantic/
├── calibre_semantic/
│   ├── core/           # Types, protocols, factories
│   ├── providers/      # Embedding & vector store implementations
│   ├── search.py       # SemanticSearchEngine
│   └── mcp/            # MCP server implementation
├── tests/
├── pyproject.toml
└── README.md
```

**Dependencies:** numpy, optional providers (sentence-transformers, sqlite-vec, etc.)

**NO Calibre dependency** - can be used independently.

### 2. Calibre Plugin (`calibre-semantic-plugin`)

**Distribution:** ZIP file, installable via Calibre's plugin manager

**Capabilities:**
- Cross-library semantic search dialog
- Background indexing of books
- Configuration UI for embedding models
- Integration with library view (navigate to results)

**Structure:**
```
calibre-semantic-plugin/
├── __init__.py          # InterfaceActionBase plugin
├── ui.py                # Qt dialogs
├── config.py            # Configuration
└── plugin-import-name-calibre_semantic_plugin.txt
```

**Bundled:** Includes `calibre-semantic` library or requires separate install.

### 3. Viewer Integration (Optional Fork)

**Approach:** Patches to Calibre's viewer for native semantic search

**Modified Files:**
```
src/calibre/gui2/viewer/search.py  # Add semantic search mode
src/calibre/gui2/viewer/ui.py      # UI adjustments
```

**Distribution Options:**
1. **Patch files** - Users apply to their Calibre install
2. **Forked release** - Separate Calibre build
3. **Upstream PR** - Submit to Calibre (unlikely to be accepted)

## Repository Strategy

### Option A: Monorepo (Recommended for Development)

```
semantic-calibre/
├── packages/
│   ├── calibre-semantic/        # Core library
│   ├── calibre-semantic-plugin/ # Calibre plugin
│   └── calibre-patches/         # Viewer patches
├── docs/
└── scripts/
```

**Pros:** Easy cross-package development, single CI/CD
**Cons:** More complex release process

### Option B: Separate Repos (Recommended for Distribution)

```
github.com/loganrooks/calibre-semantic         # Core library
github.com/loganrooks/calibre-semantic-plugin  # Plugin
github.com/loganrooks/calibre                  # Fork (if needed)
```

**Pros:** Clear separation, independent releases
**Cons:** More repos to manage

## Integration Points with Calibre

### Cross-Library Search (Plugin)

```python
# Plugin accesses Calibre's database
from calibre.library import db
from calibre_semantic import SemanticSearchEngine

class SemanticSearchAction(InterfaceActionBase):
    def search(self, query):
        # Get database
        library_db = self.gui.current_db

        # Use our engine
        engine = SemanticSearchEngine(config)
        results = engine.search(query)

        # Navigate to result in Calibre
        self.gui.library_view.select_rows([r.book_id for r in results])
```

### Viewer In-Book Search (Modification)

```python
# Modified search.py in Calibre viewer
class SearchPanel:
    def setup_ui(self):
        # Existing modes
        self.query_type.addItem('Normal')
        self.query_type.addItem('Regex')

        # NEW: Semantic mode
        self.query_type.addItem('Semantic')

    def run_searches(self):
        if self.mode == 'semantic':
            # Use calibre-semantic for search
            from calibre_semantic.viewer import ViewerSemanticSearch
            searcher = ViewerSemanticSearch(self.book_path)
            return searcher.search(self.query)
```

### MCP Server (Standalone)

```python
# Completely independent of Calibre
from calibre_semantic import SemanticSearchEngine
from calibre_semantic.mcp import MCPServer

engine = SemanticSearchEngine(config)
server = MCPServer(engine)
server.run()  # Listens on stdin/stdout
```

## Recommended Path Forward

### Phase 1: Core Library (Current)
- [x] Embedding provider abstraction
- [x] Vector store abstraction
- [ ] Chunking strategies
- [ ] SemanticSearchEngine
- [ ] MCP server

### Phase 2: Calibre Plugin
- [ ] Plugin skeleton
- [ ] Background indexer
- [ ] Search dialog UI
- [ ] Configuration panel

### Phase 3: Viewer Integration (Optional)
- [ ] Assess if native viewer integration is needed
- [ ] Create patch for search.py
- [ ] Test with various book formats
- [ ] Document installation process

## Decision: What About the Calibre Fork?

**Current state:** We have a full Calibre clone in the repo.

**Recommendation:**
1. Move `calibre-semantic` to its own location (not nested in Calibre)
2. Keep Calibre fork minimal - only for viewer patches if needed
3. Focus on plugin approach first (covers 80% of use cases)

**Rationale:**
- Most users want cross-library search (plugin handles this)
- Viewer integration is nice-to-have, not essential
- Maintaining a Calibre fork is significant overhead
- Plugin approach allows users to stay on official Calibre releases
