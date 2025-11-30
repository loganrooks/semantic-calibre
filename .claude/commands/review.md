---
description: Review codebase for documentation drift and implementation mismatches
allowed-tools: Bash(python:*), Read, Glob, Grep
---

Perform a comprehensive review to catch documentation drift and implementation mismatches:

## 1. Protocol/Implementation Sync Check
Run the protocol compliance test:
```bash
cd semantic-search && python -m pytest tests/test_protocol_compliance.py -v
```
If this test doesn't exist yet, flag it as an issue.

## 2. Documentation Consistency
Check these files are in sync:
- **CLAUDE.md** vs **ROADMAP.md**: Current Phase should match
- **ROADMAP.md** phase status should reflect actual completion
- **DESIGN.md** package structure should match actual `calibre_semantic/` contents
- **ARCHITECTURE.md** should not reference outdated approaches (e.g., "plugin")

## 3. ADR Compliance
For each ADR in `docs/decisions/`:
- Check if implementation matches the decision
- Key ADRs to verify:
  - ADR-002: `index_on_add` should default to `False`
  - ADR-004: Only `src/calibre/gui2/viewer/search.py` should be modified

## 4. Test Count Verification
Run tests and compare count to CLAUDE.md "Testing Notes" section.

## 5. Report
Summarize findings:
- ✅ Items in sync
- ⚠️ Items needing attention
- 🔴 Critical mismatches

Provide specific file:line references for any issues found.
