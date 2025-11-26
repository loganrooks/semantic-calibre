# Fork Maintenance Guide

This repository is a fork of [Calibre](https://github.com/kovidgoyal/calibre) with semantic search capabilities added.

## Repository Structure

```
semantic-calibre/
├── src/calibre/                    # Calibre source (synced with upstream)
│   └── gui2/viewer/search.py       # Modified for semantic search
├── semantic-search/                # Our semantic search library
│   └── calibre_semantic/
├── recipes/                        # Calibre recipes (from upstream)
└── ...                             # Other Calibre files
```

## Branch Strategy

| Branch | Purpose | Tracks |
|--------|---------|--------|
| `main` | Latest upstream Calibre | `upstream/master` |
| `feature/semantic-search` | Our semantic search work | Development branch |
| `release/*` | Stable releases | Tagged versions |

## Remotes

```bash
# View remotes
git remote -v

# origin = our fork (loganrooks/semantic-calibre)
# upstream = official Calibre (kovidgoyal/calibre)
```

## Syncing with Upstream Calibre

### Regular Sync (Weekly/Monthly)

```bash
# 1. Fetch latest from upstream
git fetch upstream

# 2. Update main branch
git checkout main
git merge upstream/master
git push origin main

# 3. Rebase feature branch onto updated main
git checkout feature/semantic-search
git rebase main

# 4. Force push feature branch (if needed)
git push origin feature/semantic-search --force-with-lease
```

### Handling Conflicts

If conflicts occur during rebase (likely in `src/calibre/gui2/viewer/search.py`):

```bash
# 1. Git will pause at the conflict
# 2. Edit the conflicted files to resolve
# 3. Stage resolved files
git add <resolved-files>

# 4. Continue rebase
git rebase --continue

# 5. If things go wrong, abort and try again
git rebase --abort
```

### Checking for Conflicts Before Rebasing

```bash
# Dry-run to see what would conflict
git checkout feature/semantic-search
git rebase --dry-run main 2>&1 | grep -i conflict
```

## Making Changes to Calibre Code

### Our Modifications

We modify these Calibre files:

1. **`src/calibre/gui2/viewer/search.py`** - Add semantic search mode
2. **`src/calibre/gui2/viewer/ui.py`** - Minor UI adjustments (if needed)

### Best Practices

1. **Keep changes minimal** - Less code = fewer conflicts
2. **Isolate our code** - Put logic in `calibre_semantic`, call from Calibre
3. **Mark changes clearly** - Use comments like `# SEMANTIC-SEARCH: added`
4. **Don't modify unrelated files** - Only touch what's necessary

### Example: Adding to search.py

```python
# In src/calibre/gui2/viewer/search.py

# SEMANTIC-SEARCH: Import our library
try:
    from calibre_semantic.viewer import ViewerSemanticSearch
    SEMANTIC_AVAILABLE = True
except ImportError:
    SEMANTIC_AVAILABLE = False

# SEMANTIC-SEARCH: Add search mode (in SearchInput.setup_ui)
if SEMANTIC_AVAILABLE:
    qt.addItem(_('Semantic'), 'semantic')
```

## Release Process

### Creating a Release

```bash
# 1. Ensure main is up to date
git checkout main
git pull upstream master
git push origin main

# 2. Merge feature branch into release branch
git checkout -b release/v1.0.0 main
git merge feature/semantic-search

# 3. Tag and push
git tag -a v1.0.0-semantic -m "Calibre with Semantic Search v1.0.0"
git push origin release/v1.0.0 --tags
```

### Version Naming

Our releases follow: `v{calibre-version}-semantic-{our-version}`

Example: `v8.15.0-semantic-1.0.0` = Calibre 8.15.0 + our semantic search v1.0.0

## Testing After Sync

After syncing with upstream, always verify:

```bash
# 1. Run our tests
cd semantic-search
python -m pytest tests/ -v

# 2. Verify Calibre builds (if you have the build environment)
python setup.py build

# 3. Test viewer search manually
calibre-debug -g  # Opens Calibre in debug mode
```

## Troubleshooting

### "Divergent branches" Error

```bash
# If main diverged from upstream
git checkout main
git reset --hard upstream/master
git push origin main --force-with-lease
```

### Rebase Conflicts Too Complex

```bash
# Alternative: Create fresh branch and cherry-pick
git checkout -b feature/semantic-search-v2 main
git cherry-pick <our-commit-hashes>
```

### Finding Our Commits

```bash
# List only our commits (not upstream)
git log --oneline main..feature/semantic-search
```

## CI/CD Considerations

For automated builds:

1. **Nightly sync** - Fetch upstream, attempt rebase, alert on conflicts
2. **Test matrix** - Run tests on both latest Calibre and last stable
3. **Build artifacts** - Generate installable packages for each platform
