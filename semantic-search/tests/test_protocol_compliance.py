"""Protocol compliance tests.

These tests verify that Protocol definitions in types.py match their
implementations. This catches drift between Protocol signatures and
actual implementation signatures.

Run with: python -m pytest tests/test_protocol_compliance.py -v
"""

from __future__ import annotations

import inspect
from typing import get_type_hints

import pytest

from calibre_semantic.core.types import EmbeddingProvider, VectorStore
from calibre_semantic.core.vectordb import BaseVectorStore
from calibre_semantic.core.embeddings import BaseEmbeddingProvider


class TestVectorStoreProtocolCompliance:
    """Verify VectorStore Protocol matches BaseVectorStore implementation."""

    def _get_method_params(self, cls, method_name: str) -> set[str]:
        """Get parameter names for a method, excluding 'self'."""
        method = getattr(cls, method_name, None)
        if method is None:
            return set()
        sig = inspect.signature(method)
        return {p for p in sig.parameters.keys() if p != "self"}

    def test_add_signature_matches(self):
        """Protocol.add() should have same params as BaseVectorStore.add()."""
        protocol_params = self._get_method_params(VectorStore, "add")
        impl_params = self._get_method_params(BaseVectorStore, "add")
        assert protocol_params == impl_params, (
            f"VectorStore.add() params {protocol_params} != "
            f"BaseVectorStore.add() params {impl_params}"
        )

    def test_remove_signature_matches(self):
        """Protocol.remove() should have same params as BaseVectorStore.remove()."""
        protocol_params = self._get_method_params(VectorStore, "remove")
        impl_params = self._get_method_params(BaseVectorStore, "remove")
        assert protocol_params == impl_params, (
            f"VectorStore.remove() params {protocol_params} != "
            f"BaseVectorStore.remove() params {impl_params}"
        )

    def test_remove_book_signature_matches(self):
        """Protocol.remove_book() should have same params as BaseVectorStore.remove_book()."""
        protocol_params = self._get_method_params(VectorStore, "remove_book")
        impl_params = self._get_method_params(BaseVectorStore, "remove_book")
        assert protocol_params == impl_params, (
            f"VectorStore.remove_book() params {protocol_params} != "
            f"BaseVectorStore.remove_book() params {impl_params}"
        )

    def test_search_signature_matches(self):
        """Protocol.search() should have same params as BaseVectorStore.search()."""
        protocol_params = self._get_method_params(VectorStore, "search")
        impl_params = self._get_method_params(BaseVectorStore, "search")
        assert protocol_params == impl_params, (
            f"VectorStore.search() params {protocol_params} != "
            f"BaseVectorStore.search() params {impl_params}"
        )

    def test_get_indexed_books_signature_matches(self):
        """Protocol.get_indexed_books() should have same params as BaseVectorStore.get_indexed_books()."""
        protocol_params = self._get_method_params(VectorStore, "get_indexed_books")
        impl_params = self._get_method_params(BaseVectorStore, "get_indexed_books")
        assert protocol_params == impl_params, (
            f"VectorStore.get_indexed_books() params {protocol_params} != "
            f"BaseVectorStore.get_indexed_books() params {impl_params}"
        )

    def test_get_chunk_count_signature_matches(self):
        """Protocol.get_chunk_count() should have same params as BaseVectorStore.get_chunk_count()."""
        protocol_params = self._get_method_params(VectorStore, "get_chunk_count")
        impl_params = self._get_method_params(BaseVectorStore, "get_chunk_count")
        assert protocol_params == impl_params, (
            f"VectorStore.get_chunk_count() params {protocol_params} != "
            f"BaseVectorStore.get_chunk_count() params {impl_params}"
        )

    def test_clear_signature_matches(self):
        """Protocol.clear() should have same params as BaseVectorStore.clear()."""
        protocol_params = self._get_method_params(VectorStore, "clear")
        impl_params = self._get_method_params(BaseVectorStore, "clear")
        assert protocol_params == impl_params, (
            f"VectorStore.clear() params {protocol_params} != "
            f"BaseVectorStore.clear() params {impl_params}"
        )

    def test_get_profiles_exists_in_protocol(self):
        """Protocol should include get_profiles() method."""
        assert hasattr(VectorStore, "get_profiles"), (
            "VectorStore Protocol missing get_profiles() method"
        )

    def test_all_base_methods_in_protocol(self):
        """All public methods in BaseVectorStore should be in VectorStore Protocol.

        Exceptions: Convenience methods that are built on top of Protocol methods
        and have default implementations don't need to be in the Protocol.
        """
        # Methods intentionally excluded from Protocol (convenience methods with defaults)
        excluded_methods = {
            "needs_reindex",  # Uses get_model_id(), has default implementation
        }

        base_methods = {
            name for name, _ in inspect.getmembers(BaseVectorStore, predicate=inspect.isfunction)
            if not name.startswith("_")
        }
        protocol_methods = {
            name for name in dir(VectorStore)
            if not name.startswith("_") and callable(getattr(VectorStore, name, None))
        }

        # Filter out inherited object methods
        protocol_methods = {m for m in protocol_methods if m not in dir(object)}

        missing = base_methods - protocol_methods - excluded_methods
        assert not missing, (
            f"BaseVectorStore methods missing from VectorStore Protocol: {missing}"
        )


class TestEmbeddingProviderProtocolCompliance:
    """Verify EmbeddingProvider Protocol matches BaseEmbeddingProvider implementation."""

    def _get_method_params(self, cls, method_name: str) -> set[str]:
        """Get parameter names for a method, excluding 'self'."""
        method = getattr(cls, method_name, None)
        if method is None:
            return set()
        sig = inspect.signature(method)
        return {p for p in sig.parameters.keys() if p != "self"}

    def test_embed_signature_matches(self):
        """Protocol.embed() should have same params as BaseEmbeddingProvider.embed()."""
        protocol_params = self._get_method_params(EmbeddingProvider, "embed")
        impl_params = self._get_method_params(BaseEmbeddingProvider, "embed")
        assert protocol_params == impl_params, (
            f"EmbeddingProvider.embed() params {protocol_params} != "
            f"BaseEmbeddingProvider.embed() params {impl_params}"
        )

    def test_embed_query_signature_matches(self):
        """Protocol.embed_query() should have same params as BaseEmbeddingProvider.embed_query()."""
        protocol_params = self._get_method_params(EmbeddingProvider, "embed_query")
        impl_params = self._get_method_params(BaseEmbeddingProvider, "embed_query")
        assert protocol_params == impl_params, (
            f"EmbeddingProvider.embed_query() params {protocol_params} != "
            f"BaseEmbeddingProvider.embed_query() params {impl_params}"
        )


class TestADRCompliance:
    """Verify implementation matches Architecture Decision Records."""

    def test_adr002_index_on_add_defaults_false(self):
        """ADR-002: index_on_add should default to False (on-demand indexing)."""
        from calibre_semantic.core.types import SemanticSearchConfig

        config = SemanticSearchConfig()
        assert config.index_on_add is False, (
            "ADR-002 violation: index_on_add should default to False, "
            f"but defaults to {config.index_on_add}"
        )

    def test_adr002_index_on_add_from_dict_defaults_false(self):
        """ADR-002: from_dict() should default index_on_add to False."""
        from calibre_semantic.core.types import SemanticSearchConfig

        config = SemanticSearchConfig.from_dict({})
        assert config.index_on_add is False, (
            "ADR-002 violation: from_dict({}) should default index_on_add to False"
        )
