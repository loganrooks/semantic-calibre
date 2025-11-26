"""Tests for EPUB content extraction.

Tests validate:
- EPUB parsing and spine extraction
- HTML to text conversion
- Chapter title detection
- Error handling for malformed EPUBs
"""

from __future__ import annotations

import io
import zipfile
from pathlib import Path
from typing import Iterator

import pytest


# =============================================================================
# Test EPUB Creation Fixtures
# =============================================================================


def create_test_epub(content_files: dict[str, str], spine_order: list[str] | None = None) -> bytes:
    """Create a minimal valid EPUB file in memory.

    Args:
        content_files: Dict mapping filenames to HTML content
        spine_order: Optional order of spine items (defaults to sorted keys)

    Returns:
        EPUB file as bytes
    """
    if spine_order is None:
        spine_order = sorted(content_files.keys())

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Mimetype (must be first, uncompressed)
        zf.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)

        # Container XML
        container_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>'''
        zf.writestr('META-INF/container.xml', container_xml)

        # Build manifest and spine
        manifest_items = []
        spine_items = []
        for i, filename in enumerate(spine_order):
            item_id = f"item{i}"
            manifest_items.append(
                f'<item id="{item_id}" href="{filename}" media-type="application/xhtml+xml"/>'
            )
            spine_items.append(f'<itemref idref="{item_id}"/>')

        # OPF content
        opf_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="uid">test-book-001</dc:identifier>
    <dc:title>Test Book</dc:title>
    <dc:creator>Test Author</dc:creator>
    <dc:language>en</dc:language>
  </metadata>
  <manifest>
    {"".join(manifest_items)}
  </manifest>
  <spine>
    {"".join(spine_items)}
  </spine>
</package>'''
        zf.writestr('OEBPS/content.opf', opf_content)

        # Content files
        for filename, content in content_files.items():
            zf.writestr(f'OEBPS/{filename}', content)

    return buffer.getvalue()


@pytest.fixture
def simple_epub() -> bytes:
    """Create a simple test EPUB with two chapters."""
    content_files = {
        'chapter1.xhtml': '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>Chapter 1</title></head>
<body>
<h1>Introduction</h1>
<p>This is the first paragraph about machine learning.</p>
<p>Neural networks are fascinating.</p>
</body>
</html>''',
        'chapter2.xhtml': '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>Chapter 2</title></head>
<body>
<h1>Deep Learning</h1>
<p>Deep learning uses multiple layers.</p>
<p>Transformers revolutionized NLP.</p>
</body>
</html>''',
    }
    return create_test_epub(content_files)


@pytest.fixture
def epub_with_nested_html() -> bytes:
    """EPUB with complex nested HTML structure."""
    content_files = {
        'chapter1.xhtml': '''<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<body>
<div class="chapter">
  <h1>Complex Chapter</h1>
  <div class="section">
    <h2>Section 1</h2>
    <p>First paragraph with <strong>bold</strong> and <em>italic</em> text.</p>
    <ul>
      <li>List item one</li>
      <li>List item two</li>
    </ul>
  </div>
  <div class="section">
    <h2>Section 2</h2>
    <blockquote>
      <p>A famous quote here.</p>
    </blockquote>
  </div>
</div>
</body>
</html>''',
    }
    return create_test_epub(content_files)


# =============================================================================
# EPUBExtractor Tests
# =============================================================================


class TestEPUBExtractor:
    """Tests for EPUBExtractor class."""

    def test_can_open_epub_from_bytes(self, simple_epub: bytes) -> None:
        """Should open EPUB from bytes."""
        from calibre_semantic.extraction.epub import EPUBExtractor

        extractor = EPUBExtractor(simple_epub)
        assert extractor is not None

    def test_can_open_epub_from_path(self, simple_epub: bytes, tmp_path: Path) -> None:
        """Should open EPUB from file path."""
        from calibre_semantic.extraction.epub import EPUBExtractor

        epub_path = tmp_path / "test.epub"
        epub_path.write_bytes(simple_epub)

        extractor = EPUBExtractor(epub_path)
        assert extractor is not None

    def test_extracts_metadata(self, simple_epub: bytes) -> None:
        """Should extract book metadata."""
        from calibre_semantic.extraction.epub import EPUBExtractor

        extractor = EPUBExtractor(simple_epub)
        metadata = extractor.get_metadata()

        assert metadata['title'] == 'Test Book'
        assert metadata['creator'] == 'Test Author'
        assert metadata['language'] == 'en'

    def test_lists_spine_items(self, simple_epub: bytes) -> None:
        """Should list all spine items in order."""
        from calibre_semantic.extraction.epub import EPUBExtractor

        extractor = EPUBExtractor(simple_epub)
        spine = extractor.get_spine()

        assert len(spine) == 2
        assert spine[0]['href'] == 'chapter1.xhtml'
        assert spine[1]['href'] == 'chapter2.xhtml'

    def test_extracts_text_from_spine_item(self, simple_epub: bytes) -> None:
        """Should extract plain text from a spine item."""
        from calibre_semantic.extraction.epub import EPUBExtractor

        extractor = EPUBExtractor(simple_epub)
        text = extractor.extract_text(0)

        assert 'Introduction' in text
        assert 'machine learning' in text
        assert 'Neural networks' in text
        # HTML tags should be stripped
        assert '<p>' not in text
        assert '<h1>' not in text

    def test_extracts_chapter_title(self, simple_epub: bytes) -> None:
        """Should detect chapter titles from headings."""
        from calibre_semantic.extraction.epub import EPUBExtractor

        extractor = EPUBExtractor(simple_epub)
        title = extractor.get_chapter_title(0)

        assert title == 'Introduction'

    def test_iterates_all_content(self, simple_epub: bytes) -> None:
        """Should iterate over all spine items with text."""
        from calibre_semantic.extraction.epub import EPUBExtractor

        extractor = EPUBExtractor(simple_epub)
        items = list(extractor.iter_content())

        assert len(items) == 2
        # Each item should have spine_index, spine_name, text, chapter_title
        assert items[0]['spine_index'] == 0
        assert items[0]['spine_name'] == 'chapter1.xhtml'
        assert 'machine learning' in items[0]['text']
        assert items[0]['chapter_title'] == 'Introduction'

        assert items[1]['spine_index'] == 1
        assert items[1]['spine_name'] == 'chapter2.xhtml'
        assert 'Deep learning' in items[1]['text']


class TestHTMLToText:
    """Tests for HTML to text conversion."""

    def test_strips_html_tags(self, epub_with_nested_html: bytes) -> None:
        """Should remove all HTML tags."""
        from calibre_semantic.extraction.epub import EPUBExtractor

        extractor = EPUBExtractor(epub_with_nested_html)
        text = extractor.extract_text(0)

        assert '<div>' not in text
        assert '<p>' not in text
        assert '<strong>' not in text

    def test_preserves_text_content(self, epub_with_nested_html: bytes) -> None:
        """Should preserve all text content."""
        from calibre_semantic.extraction.epub import EPUBExtractor

        extractor = EPUBExtractor(epub_with_nested_html)
        text = extractor.extract_text(0)

        assert 'Complex Chapter' in text
        assert 'bold' in text
        assert 'italic' in text
        assert 'List item one' in text
        assert 'A famous quote here' in text

    def test_adds_spacing_between_blocks(self, epub_with_nested_html: bytes) -> None:
        """Should add proper spacing between block elements."""
        from calibre_semantic.extraction.epub import EPUBExtractor

        extractor = EPUBExtractor(epub_with_nested_html)
        text = extractor.extract_text(0)

        # Paragraphs should be separated
        # Check that words from different paragraphs aren't concatenated
        assert 'text.List' not in text  # Should have space/newline between


class TestEPUBErrorHandling:
    """Tests for error handling with malformed EPUBs."""

    def test_raises_on_invalid_zip(self) -> None:
        """Should raise error for invalid ZIP file."""
        from calibre_semantic.extraction.epub import EPUBExtractor, EPUBError

        with pytest.raises(EPUBError, match="Invalid EPUB"):
            EPUBExtractor(b"not a zip file")

    def test_raises_on_missing_container(self) -> None:
        """Should raise error if container.xml is missing."""
        from calibre_semantic.extraction.epub import EPUBExtractor, EPUBError

        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, 'w') as zf:
            zf.writestr('mimetype', 'application/epub+zip')

        with pytest.raises(EPUBError, match="container.xml"):
            EPUBExtractor(buffer.getvalue())

    def test_raises_on_missing_opf(self) -> None:
        """Should raise error if OPF file is missing."""
        from calibre_semantic.extraction.epub import EPUBExtractor, EPUBError

        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, 'w') as zf:
            zf.writestr('mimetype', 'application/epub+zip')
            zf.writestr('META-INF/container.xml', '''<?xml version="1.0"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>''')

        with pytest.raises(EPUBError, match="OPF"):
            EPUBExtractor(buffer.getvalue())

    def test_handles_missing_spine_item_gracefully(self, simple_epub: bytes) -> None:
        """Should handle request for non-existent spine item."""
        from calibre_semantic.extraction.epub import EPUBExtractor

        extractor = EPUBExtractor(simple_epub)

        # Requesting beyond spine length
        with pytest.raises(IndexError):
            extractor.extract_text(99)


class TestSpineItemContent:
    """Tests for individual spine item handling."""

    def test_preserves_spine_order(self) -> None:
        """Should preserve the exact spine order from OPF."""
        from calibre_semantic.extraction.epub import EPUBExtractor

        # Create EPUB with specific spine order
        content_files = {
            'intro.xhtml': '<html><body><p>Intro</p></body></html>',
            'chapter1.xhtml': '<html><body><p>Chapter 1</p></body></html>',
            'appendix.xhtml': '<html><body><p>Appendix</p></body></html>',
        }
        # Spine order different from alphabetical
        spine_order = ['intro.xhtml', 'chapter1.xhtml', 'appendix.xhtml']
        epub_bytes = create_test_epub(content_files, spine_order)

        extractor = EPUBExtractor(epub_bytes)
        spine = extractor.get_spine()

        assert spine[0]['href'] == 'intro.xhtml'
        assert spine[1]['href'] == 'chapter1.xhtml'
        assert spine[2]['href'] == 'appendix.xhtml'

    def test_handles_empty_spine_item(self) -> None:
        """Should handle spine items with no text content."""
        from calibre_semantic.extraction.epub import EPUBExtractor

        content_files = {
            'empty.xhtml': '''<?xml version="1.0"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<body></body>
</html>''',
        }
        epub_bytes = create_test_epub(content_files)

        extractor = EPUBExtractor(epub_bytes)
        text = extractor.extract_text(0)

        assert text.strip() == ''
