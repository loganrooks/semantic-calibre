# Semantic Calibre Roadmap

> **Last Updated:** 2025-11-30
> **Current Phase:** 2 - Viewer Integration

## Vision

Enable semantic (meaning-based) search across Calibre e-book libraries, allowing users to find books and passages by concept rather than exact keywords.

**Key Design Principles:**
- Integrate with Calibre's existing AI system (don't duplicate configuration)
- On-demand indexing (respect user resources)
- Embedding profiles (support multiple providers/models)
- Minimal fork divergence (easy upstream sync)

See [docs/ISSUES.md](docs/ISSUES.md) for design decisions.

---

## Phase 1: Core Library ✅

**Goal:** Build the foundational `calibre_semantic` library with all core components.

**Status:** Complete

- [x] **Types & Protocols** (`core/types.py`)
  - BookIdentifier, TextChunk, EmbeddedChunk
  - EmbeddingProvider protocol
  - VectorStore protocol
  - Configuration dataclasses

- [x] **Embedding Providers** (`core/embeddings.py`, `providers/embeddings/`)
  - BaseEmbeddingProvider abstract class
  - SentenceTransformerProvider (local)
  - Provider registry and factory
  - CalibreAIAdapter (bridges Calibre's AI module)

- [x] **Vector Stores** (`core/vectordb.py`, `providers/vectordb/`)
  - InMemoryVectorStore (development/testing)
  - SQLiteVecStore (production persistence)
  - Store registry and factory

- [x] **Chunking Strategies** (`core/chunking.py`)
  - SemanticChunkingStrategy (respects boundaries)
  - FixedSizeChunkingStrategy (simple overlap)
  - Factory function

- [x] **SemanticSearchEngine** (`search.py`)
  - Orchestrates embedding + chunking + storage
  - Index management (add, remove, check)
  - Search with filters (book, library, score)

- [x] **Book Content Extraction** (`extraction/`)
  - EPUB text extraction (parse spine, strip HTML)
  - Location metadata for navigation

- [x] **MCP Server** (`mcp/`)
  - Expose search as MCP tools
  - Index management tools
  - Configuration for Claude Desktop

---

## Phase 1.5: Embedding Profiles & Calibre AI Integration ✅

**Goal:** Support multiple embedding providers with proper Calibre AI integration.

**Status:** Complete (OpenAI embedding support deferred)

### Completed
- [x] Design decisions documented (DD-001 through DD-005)
- [x] Calibre AI integration guide written
- [x] **Calibre AI Embedding Functions**
  - Add `embed()` to `src/calibre/ai/google/backend.py`
  - Support configurable dimensions (256, 768, 3072)
- [x] **Update CalibreAIAdapter**
  - Use native Calibre AI embedding functions
  - Proper fallback chain to sentence-transformers
- [x] **Embedding Profiles** (`core/profiles.py`)
  - `EmbeddingProfile` dataclass (provider, model, dimension, index strategy)
  - `BookIndexStatus` tracking (which books in which profiles)
  - `ProfileManager` class with CRUD operations
  - Database schema for profiles and book status
- [x] **SQLite-vec Profile Integration**
  - Per-profile vector storage with `profile_id` parameter
  - Profile-aware search isolated by namespace
  - Migration from v1 (no profile) to v2 schema
- [x] **SemanticSearchEngine Profile Support**
  - Profile-aware indexing (`index_text`, `index_book_content`, `index_epub`)
  - Profile selection for search
  - Profile listing with `get_profiles()`
  - Profile-specific clearing with `clear(profile_id)`
- [x] **On-Demand Indexing**
  - ProfileManager integration with SemanticSearchEngine
  - Index status tracking (INDEXING, COMPLETE, FAILED)
  - `get_book_index_status()` and `needs_indexing()` methods
  - Status cleared on remove_book and force_reindex

### Deferred
- [ ] **OpenAI Embedding Support**
  - Add `embed()` to `src/calibre/ai/openai/backend.py`

---

## Phase 2: Viewer Integration 🚧

**Goal:** Add semantic search mode to Calibre's e-book viewer (in-book search).

**Status:** In Progress (Core Complete)

Per [ADR-004](docs/decisions/004-minimal-viewer-modification.md), we modify only `src/calibre/gui2/viewer/search.py`.

### Completed
- [x] **Viewer Search Patch**
  - Add "Semantic" to search mode dropdown
  - Delegate to `calibre_semantic.search_viewer_book()`
  - Convert results to viewer's SearchResult format
  - Graceful fallback if library not installed

- [x] **Viewer Integration API** (`calibre_semantic/viewer.py`)
  - `search_viewer_book()` - Main search entry point
  - `is_book_indexed()` - Check indexing status
  - `index_book_for_viewer()` - Index book content
  - Auto-indexing on first search

- [x] **Result Enhancement**
  - Show similarity scores in result tooltips
  - Visual distinction for semantic results (icon)
  - User-friendly error messages for search failures

- [x] **Indexing Progress Feedback**
  - Show "Indexing for semantic search..." during first search
  - Spinner indicates background indexing

- [x] **Profile Support**
  - Profile preference (`viewer-semantic-profile`)
  - Profile passed through search chain

- [x] **Profile Selector UI**
  - Visual profile dropdown (visible in semantic mode)
  - Dynamic profile list from SemanticSearchEngine
  - Remembers last used profile

- [x] **Score Passed to JavaScript**
  - Score included in `for_js` dict for potential JS-side styling

### Remaining
- [ ] **Passage Highlighting**
  - Highlight relevant passages with gradient based on score (requires JS integration)

---

## Phase 3: Library Search UI

**Goal:** Add semantic search to the main Calibre library interface (cross-book search).

**Status:** Planned

Modifications to main Calibre GUI for library-wide search:

- [ ] **Embedding Library Manager**
  - View/create/delete profiles
  - See which books are indexed where
  - Bulk index selected books

- [ ] **Search Dialog**
  - Qt-based search interface
  - Profile selector
  - Result display with book covers and similarity scores
  - Navigation to results in library view

- [ ] **Index Actions**
  - Right-click "Add to Semantic Index"
  - Bulk indexing with progress
  - Index on book add (optional)

---

## Phase 4: Advanced Features (Future)

- [ ] **Index Strategies**
  - HNSW for large collections (via FAISS backend)
  - IVF for very large collections
  - Quantization for memory-constrained systems

- [ ] **Semantic Recommendations**
  - "Books similar to this"
  - "More like this passage"

- [ ] **Cross-language Search**
  - Search in English, find results in other languages
  - Multi-lingual embedding models

- [ ] **Cost Tracking**
  - Show embedding costs before indexing
  - Track cumulative API costs

- [ ] **Cloud Sync**
  - Sync embeddings across devices
  - Shared library search

---

## Technical Debt & Maintenance

### Known Issues
See [docs/ISSUES.md](docs/ISSUES.md) for full list.

- **KI-001:** sqlite-vec tests skipped in CI
- **KI-002:** SentenceTransformer tests require heavy dependencies
- **KI-003:** CalibreAIAdapter falls back silently

### Maintenance Tasks
- [ ] Set up CI/CD with GitHub Actions
- [ ] Add type checking with mypy
- [ ] Add code coverage reporting
- [ ] Automate upstream sync checks
- [ ] Weekly documentation review

---

## Contributing

See [CLAUDE.md](CLAUDE.md) for development conventions and [FORK_MAINTENANCE.md](FORK_MAINTENANCE.md) for working with the Calibre fork.

### Current Priorities
1. ~~**Calibre AI embedding integration**~~ ✅ Complete
2. ~~**Embedding profiles implementation**~~ ✅ Complete
3. ~~**On-demand indexing**~~ ✅ Complete
4. **Viewer integration** (Phase 2 - enables user testing)

### Documentation
- [docs/ISSUES.md](docs/ISSUES.md) - Design decisions and known issues
- [docs/CALIBRE_AI.md](docs/CALIBRE_AI.md) - Calibre AI integration guide
- [semantic-search/DESIGN.md](semantic-search/DESIGN.md) - Library design
- [semantic-search/ARCHITECTURE.md](semantic-search/ARCHITECTURE.md) - Architecture details
