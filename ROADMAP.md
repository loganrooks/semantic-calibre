# Semantic Calibre Roadmap

> **Last Updated:** 2025-01-26
> **Current Phase:** 1.5 - Embedding Profiles & Calibre AI Integration

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

## Phase 1.5: Embedding Profiles & Calibre AI Integration 🚧

**Goal:** Support multiple embedding providers with proper Calibre AI integration.

**Status:** In Progress

### In Progress
- [ ] **On-Demand Indexing**
  - Remove auto-index default
  - `index_book(book_id, profile_id)` method
  - Index status checking

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

### Planned
- [ ] **OpenAI Embedding Support**
  - Add `embed()` to `src/calibre/ai/openai/backend.py`

---

## Phase 2: Viewer Integration

**Goal:** Add semantic search mode to Calibre's e-book viewer (in-book search).

**Status:** Planned

Per [ADR-004](docs/decisions/004-minimal-viewer-modification.md), we modify only `src/calibre/gui2/viewer/search.py`.

- [ ] **Viewer Search Patch**
  - Add "Semantic" to search mode dropdown
  - Delegate to `calibre_semantic.search_viewer_book()`
  - Convert results to viewer's SearchResult format

- [ ] **On-Demand Book Indexing**
  - Prompt to index if book not in selected profile
  - Index current book with selected profile
  - Show indexing progress

- [ ] **Result Navigation**
  - Jump to semantic matches in book
  - Highlight relevant passages
  - Show similarity scores in sidebar

- [ ] **Profile Selection**
  - Profile selector in viewer (or use default)
  - Remember last used profile

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
3. **On-demand indexing** (Phase 1.5 remaining item)
4. **Viewer integration** (Phase 2 - enables user testing)

### Documentation
- [docs/ISSUES.md](docs/ISSUES.md) - Design decisions and known issues
- [docs/CALIBRE_AI.md](docs/CALIBRE_AI.md) - Calibre AI integration guide
- [semantic-search/DESIGN.md](semantic-search/DESIGN.md) - Library design
- [semantic-search/ARCHITECTURE.md](semantic-search/ARCHITECTURE.md) - Architecture details
