# ADR-003: Hybrid Calibre AI Integration

**Date:** 2025-01-26
**Status:** Accepted
**Deciders:** Project maintainers

## Context

Calibre has a built-in AI module at `src/calibre/ai/` with:
- Provider plugins (Google, OpenAI, Ollama, OpenRouter, GitHub)
- Secure API key management
- User configuration UI
- Capability detection (`AICapabilities.embedding` flag exists)

Our initial `CalibreAIAdapter` tried to import from Calibre's AI module, falling back to sentence-transformers.

### Problem Statement

- Don't want users to configure API keys in two places
- Calibre has `AICapabilities.embedding` flag but no `embed()` implementation
- `CalibreAIAdapter` attempted to import non-existent embedding code
- Inconsistent UX between "Ask AI" and semantic search configuration

## Decision

**Extend Calibre's AI backends** with `embed()` functions rather than building parallel infrastructure:

1. Add `embed()` to `src/calibre/ai/google/backend.py`
2. Add `embed()` to `src/calibre/ai/openai/backend.py`
3. Update `CalibreAIAdapter` to call these native functions
4. Fall back to sentence-transformers when Calibre AI unavailable

## Consequences

### Positive
- Users configure AI once in Calibre preferences
- Consistent UX with existing "Ask AI" feature
- Minimal fork divergence (additions, not modifications)
- Leverage Calibre's secure API key storage

### Negative
- Dependency on Calibre's AI module structure
- Need to handle standalone use (without full Calibre)
- Must track Calibre AI API changes on upstream sync

### Neutral
- Some code duplication if used standalone
- Need fallback for older Calibre versions

## Implementation Notes

Fallback chain:
```
1. Try Calibre AI (user's configured provider)
   ↓ (ImportError or not configured)
2. Try sentence-transformers (local)
   ↓ (not installed)
3. Raise RuntimeError with installation instructions
```

See [CALIBRE_AI.md](../CALIBRE_AI.md) for detailed API specifications.

## Related Decisions
- [ADR-001](001-embedding-profiles.md): Profiles include provider selection
- [ADR-004](004-minimal-viewer-modification.md): Keep Calibre changes minimal
