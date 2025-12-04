# Semantic Calibre Roadmap

> **Last Updated:** 2025-12-03
> **Current Phase:** 3 - Library Search UI (In Progress)

## Vision

Enable semantic (meaning-based) search across Calibre e-book libraries, allowing users to find books and passages by concept rather than exact keywords.

**Key Design Principles:**
- Integrate with Calibre's existing AI system (don't duplicate configuration)
- On-demand indexing (respect user resources) - [ADR-002](docs/decisions/002-on-demand-indexing.md)
- Embedding profiles (support multiple providers/models) - [ADR-001](docs/decisions/001-embedding-profiles.md)
- Minimal fork divergence (easy upstream sync) - [ADR-004](docs/decisions/004-minimal-viewer-modification.md)

See [docs/ISSUES.md](docs/ISSUES.md) for design decisions and [docs/decisions/](docs/decisions/) for ADRs.

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

## Phase 2: Viewer Integration ✅

**Goal:** Add semantic search mode to Calibre's e-book viewer (in-book search).

**Status:** Complete

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

### Deferred to Future Release
- [ ] **Passage Highlighting with Score Gradient**
  - Highlight relevant passages with color intensity based on score
  - Requires JavaScript modification in viewer bundle (higher upstream sync risk)
  - Score already passed to JS via `for_js` - infrastructure ready

---

## Phase 3: Library Search UI 🔄

**Goal:** Add semantic search to the main Calibre library interface (cross-book search) with metadata filtering.

**Status:** In Progress

**Key ADRs:**
- [ADR-005](docs/decisions/005-vector-index-strategies.md): ChromaDB with HNSW for library search
- [ADR-006](docs/decisions/006-hybrid-metadata-filtering.md): Hybrid query architecture
- [ADR-007](docs/decisions/007-library-ui-integration.md): Library UI integration strategy
- [ADR-008](docs/decisions/008-background-indexing.md): Background indexing architecture

### Vector Store Migration
- [x] **ChromaDB Integration** ✅
  - ChromaDB provider implemented (`providers/vectordb/chromadb.py`)
  - Profile-based collections with HNSW indexing
  - ADR-006 hybrid query support (filter_book_ids parameter)
  - Metadata storage/reconstruction for TextChunk
  - 19 tests passing
- [ ] **Migration Path**
  - Keep sqlite-vec for viewer (lightweight, per-book)
  - ChromaDB for library-wide search
  - No migration needed - different use cases

### Metadata-Aware Search
- [x] **Hybrid Query Implementation** ✅ - [ADR-006](docs/decisions/006-hybrid-metadata-filtering.md)
  - `MetadataFilterBuilder`: Translate UI filters to Calibre search syntax
  - `LibrarySearchEngine`: Two-step hybrid query orchestration
  - Support all built-in fields: authors, tags, series, publisher, language, rating, pubdate
  - Support custom columns: `#tradition`, `#course`, `#reading_status`, etc.
  - 45 new tests for library integration

- [x] **Library Integration API** ✅ (`calibre_semantic/library.py`)
  - `MetadataFilterBuilder`: Fluent API for building Calibre queries
  - `LibrarySearchEngine`: Orchestrates Calibre DB + ChromaDB hybrid search
  - `IndexingJob`: Background indexing per ADR-008
  - `IndexingResults`: Batch indexing outcomes tracking
  - 299 total tests passing

- [x] **Filter UI Components** ✅
  - MetadataFilterPanel widget (authors, tags, series inputs)
  - Filter builder integration with LibrarySearchEngine
  - Clear filters functionality

### Library UI - [ADR-007](docs/decisions/007-library-ui-integration.md)
- [x] **Embedding Library Manager** ✅ (`gui2/semantic_search/profile_manager.py`)
  - View profiles with statistics
  - Index selected books from library view
  - Index all books in library
  - Clear index per profile

- [x] **Search Dialog** ✅ (`gui2/semantic_search/dialog.py`)
  - Qt-based search interface with HistoryLineEdit
  - Profile selector dropdown
  - Metadata filter panel (authors, tags, series)
  - Result list with book title, authors, and similarity score
  - Result preview with chunk text
  - Navigation to results in library view (double-click to open)

- [x] **Index Actions** ✅
  - "Manage Index..." button opens profile manager
  - Bulk indexing with progress bar
  - Index from library selection or all books
  - Clear index functionality

- [x] **UI Polish** ✅
  - Menu action with "Add to Semantic Index" for selected books
  - Book covers displayed in search results (60x80 thumbnails)
  - Saved filter presets with save/delete functionality
  - [ ] Quick filters for common queries (deferred)

---

## Phase 4: Advanced Features (Future)

### 4.1: Deferred Items from Earlier Phases
- [ ] **OpenAI Embedding Support** (from Phase 1.5)
  - Add `embed()` to `src/calibre/ai/openai/backend.py`
  - Support text-embedding-3-small, text-embedding-3-large models
  - Configurable dimensions (256, 1536, 3072)

- [ ] **Advanced Index Strategies** - [ADR-005](docs/decisions/005-vector-index-strategies.md)
  - FAISS backend for IVF (very large collections >1M chunks)
  - Quantization for memory-constrained systems
  - Note: ChromaDB HNSW handles most use cases well

- [ ] **Passage Highlighting with Score Gradient** (from Phase 2)
  - Highlight relevant passages with color intensity based on score
  - Requires JavaScript modification in viewer bundle
  - Score already passed to JS via `for_js` - infrastructure ready

- [ ] **Phase 3 UI Polish**
  - Right-click context menu "Add to Semantic Index"
  - Book covers in search results
  - Saved filter presets
  - Quick filters for common queries

### 4.2: Advanced Index Strategies
Per [ADR-005](docs/decisions/005-vector-index-strategies.md):

- [ ] **FAISS Backend** (for very large collections >1M chunks)
  - IVF (Inverted File Index) for faster search
  - Product Quantization for memory efficiency
  - Note: ChromaDB HNSW handles most use cases well

- [ ] **Incremental Indexing**
  - Detect changed book content
  - Only re-embed modified sections
  - Track content hashes per chunk

- [ ] **Model Migration Tools**
  - Detect embedding model changes
  - Batch re-index with new model
  - Parallel old/new index during transition

### 4.3: Semantic Recommendations
- [ ] **Similar Books**
  - "Books similar to this" button in library view
  - Aggregate embeddings to book-level representation
  - Configurable similarity threshold

- [ ] **Similar Passages**
  - "More like this passage" in viewer
  - Find related passages across library
  - Cluster visualization

- [ ] **Reading Lists**
  - Generate reading lists from semantic clusters
  - Thematic grouping of books
  - "If you liked X, try Y" recommendations

### 4.4: Cross-Language Search
- [ ] **Multi-lingual Embedding Models**
  - Support models like `paraphrase-multilingual-MiniLM-L12-v2`
  - Search in English, find results in German/French/etc.
  - Language detection per chunk

- [ ] **Translation-Aware Search**
  - Identify translated editions
  - Link semantically equivalent passages across languages

### 4.5: Hybrid Search Enhancements
- [ ] **Full-Text + Semantic Fusion**
  - Combine BM25/FTS scores with semantic scores
  - Configurable weight balance
  - Re-ranking strategies (RRF, linear combination)

- [ ] **Semantic Tag Suggestions**
  - Suggest tags based on content similarity
  - Integrate with Calibre's Tag Browser
  - Auto-categorization based on existing tagged books

- [ ] **Custom Chunking per Genre**
  - Poetry: sentence-level chunks
  - Technical: section-level with code blocks
  - Fiction: paragraph-level with chapter awareness

### 4.6: Analytics & Tracking
- [ ] **Cost Tracking**
  - Show embedding costs before indexing
  - Track cumulative API costs per provider
  - Budget alerts and limits

- [ ] **Search Analytics**
  - Search history with saved searches
  - Query refinement suggestions
  - Popular search patterns

- [ ] **Index Statistics Dashboard**
  - Books indexed per profile
  - Embedding dimensions and storage usage
  - Index health monitoring

### 4.7: Sync & Backup
- [ ] **Export/Import Embeddings**
  - Export embeddings for backup
  - Import to new installation
  - Profile migration between libraries

- [ ] **Cloud Sync** (Long-term)
  - Sync embeddings across devices
  - Shared library search
  - Collaborative filtering

### 4.8: Performance Optimizations
- [ ] **Caching Layer**
  - Query result caching
  - Embedding cache for repeated content
  - LRU eviction for memory management

- [ ] **Async Indexing Improvements**
  - Background indexing daemon
  - Priority queue for user-requested books
  - Pause/resume indexing

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
4. ~~**Viewer integration**~~ ✅ Complete (Phase 2)
5. **Library Search UI** (Phase 3 - cross-book search) 🔄 In Progress
   - ✅ ChromaDB vector store provider
   - Next: MetadataFilterBuilder and Hybrid Query
   - Next: Library UI (search dialog, profile manager)

### Documentation
- [docs/ISSUES.md](docs/ISSUES.md) - Design decisions and known issues
- [docs/CALIBRE_AI.md](docs/CALIBRE_AI.md) - Calibre AI integration guide
- [semantic-search/DESIGN.md](semantic-search/DESIGN.md) - Library design
- [semantic-search/ARCHITECTURE.md](semantic-search/ARCHITECTURE.md) - Architecture details

### Architecture Decision Records (ADRs)
| ADR | Title | Phase |
|-----|-------|-------|
| [001](docs/decisions/001-embedding-profiles.md) | Embedding Profiles | 1.5 |
| [002](docs/decisions/002-on-demand-indexing.md) | On-Demand Indexing | 1.5 |
| [003](docs/decisions/003-calibre-ai-integration.md) | Calibre AI Integration | 1.5 |
| [004](docs/decisions/004-minimal-viewer-modification.md) | Minimal Viewer Modification | 2 |
| [005](docs/decisions/005-vector-index-strategies.md) | Vector Index Strategies | 2/3 |
| [006](docs/decisions/006-hybrid-metadata-filtering.md) | Hybrid Metadata Filtering | 3 |
| [007](docs/decisions/007-library-ui-integration.md) | Library UI Integration | 3 |
| [008](docs/decisions/008-background-indexing.md) | Background Indexing | 3 |
