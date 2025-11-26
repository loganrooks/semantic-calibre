---
description: Run the semantic-search test suite
allowed-tools: Bash(python:*), Bash(cd:*)
argument-hint: [optional: test file or -k filter]
---

Run the semantic-search test suite.

```bash
cd /home/user/semantic-calibre/semantic-search && python -m pytest tests/ $ARGUMENTS -v
```

If a specific test file or filter is provided, use that. Otherwise run all tests.

Report:
1. Total tests passed/failed/skipped
2. Any failures with brief explanation
3. Suggestions for fixing failures if any
