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

### In Progress
- [ ] **SQLite-vec Profile Integration**
  - Per-profile vector storage
  - Profile-aware search

- [ ] **SemanticSearchEngine Profile Support**
  - Profile-aware indexing
  - Profile selection for search

### Planned
- [ ] **On-Demand Indexing**
  - Remove auto-index default
  - `index_book(book_id, profile_id)` method
  - Index status checking

- [ ] **OpenAI Embedding Support**
  - Add `embed()` to `src/calibre/ai/openai/backend.py`

---

## Phase 2: Calibre Plugin

**Goal:** Create an installable Calibre plugin for cross-library semantic search.

**Status:** Planned

- [ ] **Plugin Skeleton**
  - InterfaceActionBase implementation
  - Plugin metadata and packaging

- [ ] **Embedding Library Manager UI**
  - View/create/delete profiles
  - See which books are indexed where
  - Manage books in profiles

- [ ] **Search Dialog UI**
  - Qt-based search interface
  - Profile selector
  - Result display with book covers and similarity scores
  - Navigation to results in library view

- [ ] **Index Actions**
  - Right-click "Add to Semantic Index"
  - Bulk indexing with progress
  - Optional dialog on book add

- [ ] **Configuration Panel**
  - Profile management
  - Default behaviors
  - Storage location

---

## Phase 3: Viewer Integration

**Goal:** Add semantic search mode to Calibre's e-book viewer.

**Status:** Planned

- [ ] **Viewer Search Patch**
  - Add "Semantic" to search mode dropdown
  - Profile selector (or use default)
  - Integrate with viewer's search infrastructure

- [ ] **On-Demand Book Indexing**
  - Prompt to index if not already indexed
  - Index current book with selected profile
  - Cache embeddings for reopened books

- [ ] **Result Navigation**
  - Jump to semantic matches in book
  - Highlight relevant passages
  - Show similarity scores in sidebar

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
1. **Calibre AI embedding integration** (Phase 1.5 blocker)
2. **Embedding profiles implementation** (enables multi-provider)
3. **Plugin skeleton** (enables user testing)

### Documentation
- [docs/ISSUES.md](docs/ISSUES.md) - Design decisions and known issues
- [docs/CALIBRE_AI.md](docs/CALIBRE_AI.md) - Calibre AI integration guide
- [semantic-search/DESIGN.md](semantic-search/DESIGN.md) - Library design
- [semantic-search/ARCHITECTURE.md](semantic-search/ARCHITECTURE.md) - Architecture details
