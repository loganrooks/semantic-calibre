"""Content extraction utilities for calibre-semantic.

This package provides extractors for various e-book formats:
- EPUB (primary format)
- PDF (planned)
- MOBI/AZW (planned)
"""

from calibre_semantic.extraction.epub import EPUBExtractor, EPUBError

__all__ = [
    "EPUBExtractor",
    "EPUBError",
]
