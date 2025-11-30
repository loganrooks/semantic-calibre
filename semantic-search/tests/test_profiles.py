"""Tests for EmbeddingProfile, BookIndexStatus, and ProfileManager.

Tests validate:
- Profile creation and serialization
- BookIndexStatus tracking
- ProfileManager CRUD operations
- Database persistence
"""

from __future__ import annotations

from datetime import datetime
import pytest

from calibre_semantic.core.types import (
    BookIdentifier,
    BookIndexStatus,
    EmbeddingProfile,
    IndexStatus,
    IndexStrategy,
)
from calibre_semantic.core.profiles import ProfileManager, generate_profile_id


# =============================================================================
# EmbeddingProfile Tests
# =============================================================================


class TestEmbeddingProfile:
    """Tests for EmbeddingProfile dataclass."""

    def test_create_profile(self) -> None:
        """Profile should be created with required fields."""
        profile = EmbeddingProfile(
            id="test-profile",
            name="Test Profile",
            provider="google",
            model="models/text-embedding-004",
            dimension=768,
        )

        assert profile.id == "test-profile"
        assert profile.name == "Test Profile"
        assert profile.provider == "google"
        assert profile.model == "models/text-embedding-004"
        assert profile.dimension == 768
        assert profile.index_strategy == IndexStrategy.FLAT

    def test_profile_with_all_fields(self) -> None:
        """Profile should accept all optional fields."""
        created = datetime(2025, 1, 26, 12, 0, 0)
        profile = EmbeddingProfile(
            id="full-profile",
            name="Full Profile",
            provider="openai",
            model="text-embedding-3-large",
            dimension=3072,
            index_strategy=IndexStrategy.HNSW,
            index_options={"hnsw_m": 16, "hnsw_ef": 200},
            created_at=created,
            description="A fully configured profile",
        )

        assert profile.index_strategy == IndexStrategy.HNSW
        assert profile.index_options["hnsw_m"] == 16
        assert profile.created_at == created
        assert profile.description == "A fully configured profile"

    def test_profile_model_id(self) -> None:
        """model_id property should combine provider, model, dimension."""
        profile = EmbeddingProfile(
            id="test",
            name="Test",
            provider="google",
            model="text-embedding-004",
            dimension=768,
        )

        assert profile.model_id == "google:text-embedding-004:768"

    def test_profile_to_dict(self) -> None:
        """Profile should serialize to dictionary."""
        profile = EmbeddingProfile(
            id="test-profile",
            name="Test Profile",
            provider="google",
            model="models/text-embedding-004",
            dimension=768,
        )

        data = profile.to_dict()

        assert data["id"] == "test-profile"
        assert data["name"] == "Test Profile"
        assert data["provider"] == "google"
        assert data["model"] == "models/text-embedding-004"
        assert data["dimension"] == 768
        assert data["index_strategy"] == "flat"
        assert isinstance(data["created_at"], str)

    def test_profile_from_dict(self) -> None:
        """Profile should deserialize from dictionary."""
        data = {
            "id": "test-profile",
            "name": "Test Profile",
            "provider": "google",
            "model": "models/text-embedding-004",
            "dimension": 768,
            "index_strategy": "hnsw",
            "index_options": {"m": 16},
            "created_at": "2025-01-26T12:00:00",
            "description": "Test description",
        }

        profile = EmbeddingProfile.from_dict(data)

        assert profile.id == "test-profile"
        assert profile.index_strategy == IndexStrategy.HNSW
        assert profile.index_options["m"] == 16
        assert profile.description == "Test description"

    def test_profile_roundtrip(self) -> None:
        """Profile should survive serialization roundtrip."""
        original = EmbeddingProfile(
            id="roundtrip-test",
            name="Roundtrip Test",
            provider="sentence-transformers",
            model="all-MiniLM-L6-v2",
            dimension=384,
            index_strategy=IndexStrategy.IVF,
            index_options={"nlist": 100},
            description="Testing roundtrip",
        )

        data = original.to_dict()
        restored = EmbeddingProfile.from_dict(data)

        assert restored.id == original.id
        assert restored.name == original.name
        assert restored.provider == original.provider
        assert restored.model == original.model
        assert restored.dimension == original.dimension
        assert restored.index_strategy == original.index_strategy
        assert restored.index_options == original.index_options
        assert restored.description == original.description


# =============================================================================
# BookIndexStatus Tests
# =============================================================================


class TestBookIndexStatus:
    """Tests for BookIndexStatus dataclass."""

    def test_create_status(self) -> None:
        """Status should be created with required fields."""
        book_id = BookIdentifier("lib-123", 42, "EPUB")
        status = BookIndexStatus(
            book_id=book_id,
            profile_id="test-profile",
        )

        assert status.book_id == book_id
        assert status.profile_id == "test-profile"
        assert status.status == IndexStatus.PENDING
        assert status.chunk_count == 0

    def test_status_complete(self) -> None:
        """Status should track completion details."""
        book_id = BookIdentifier("lib-123", 42, "EPUB")
        indexed_at = datetime(2025, 1, 26, 12, 0, 0)

        status = BookIndexStatus(
            book_id=book_id,
            profile_id="test-profile",
            status=IndexStatus.COMPLETE,
            indexed_at=indexed_at,
            chunk_count=150,
        )

        assert status.status == IndexStatus.COMPLETE
        assert status.indexed_at == indexed_at
        assert status.chunk_count == 150

    def test_status_failed(self) -> None:
        """Status should track failure details."""
        book_id = BookIdentifier("lib-123", 42, "EPUB")

        status = BookIndexStatus(
            book_id=book_id,
            profile_id="test-profile",
            status=IndexStatus.FAILED,
            error_message="API rate limit exceeded",
        )

        assert status.status == IndexStatus.FAILED
        assert status.error_message == "API rate limit exceeded"

    def test_status_to_dict(self) -> None:
        """Status should serialize to dictionary."""
        book_id = BookIdentifier("lib-123", 42, "EPUB")
        status = BookIndexStatus(
            book_id=book_id,
            profile_id="test-profile",
            status=IndexStatus.COMPLETE,
            chunk_count=100,
        )

        data = status.to_dict()

        assert data["book_id"] == "lib-123:42:EPUB"
        assert data["profile_id"] == "test-profile"
        assert data["status"] == "complete"
        assert data["chunk_count"] == 100

    def test_status_from_dict(self) -> None:
        """Status should deserialize from dictionary."""
        data = {
            "book_id": "lib-123:42:EPUB",
            "profile_id": "test-profile",
            "status": "indexing",
            "indexed_at": None,
            "chunk_count": 50,
            "error_message": None,
        }

        status = BookIndexStatus.from_dict(data)

        assert status.book_id.library_id == "lib-123"
        assert status.book_id.book_id == 42
        assert status.book_id.format == "EPUB"
        assert status.status == IndexStatus.INDEXING
        assert status.chunk_count == 50


# =============================================================================
# ProfileManager Tests
# =============================================================================


class TestProfileManager:
    """Tests for ProfileManager class."""

    def test_create_manager_in_memory(self) -> None:
        """Manager should work with in-memory database."""
        manager = ProfileManager()
        assert manager is not None
        manager.close()

    def test_create_profile(self) -> None:
        """Manager should create profiles."""
        manager = ProfileManager()

        profile = manager.create_profile(
            name="Test Profile",
            provider="google",
            model="text-embedding-004",
            dimension=768,
        )

        assert profile.name == "Test Profile"
        assert profile.provider == "google"
        assert profile.dimension == 768
        assert profile.id is not None

        manager.close()

    def test_create_profile_with_custom_id(self) -> None:
        """Manager should accept custom profile ID."""
        manager = ProfileManager()

        profile = manager.create_profile(
            name="Custom ID Profile",
            provider="openai",
            model="text-embedding-3-small",
            dimension=1536,
            profile_id="my-custom-id",
        )

        assert profile.id == "my-custom-id"

        manager.close()

    def test_create_duplicate_profile_raises(self) -> None:
        """Creating profile with duplicate ID should raise."""
        manager = ProfileManager()

        manager.create_profile(
            name="First",
            provider="google",
            model="test",
            dimension=768,
            profile_id="duplicate-id",
        )

        with pytest.raises(ValueError, match="already exists"):
            manager.create_profile(
                name="Second",
                provider="openai",
                model="test",
                dimension=768,
                profile_id="duplicate-id",
            )

        manager.close()

    def test_get_profile(self) -> None:
        """Manager should retrieve profiles by ID."""
        manager = ProfileManager()

        created = manager.create_profile(
            name="Retrievable",
            provider="google",
            model="text-embedding-004",
            dimension=768,
            profile_id="get-test",
        )

        retrieved = manager.get_profile("get-test")

        assert retrieved is not None
        assert retrieved.id == created.id
        assert retrieved.name == created.name

        manager.close()

    def test_get_nonexistent_profile(self) -> None:
        """Getting nonexistent profile should return None."""
        manager = ProfileManager()

        result = manager.get_profile("does-not-exist")

        assert result is None

        manager.close()

    def test_list_profiles(self) -> None:
        """Manager should list all profiles."""
        manager = ProfileManager()

        manager.create_profile("First", "google", "model1", 768)
        manager.create_profile("Second", "openai", "model2", 1536)
        manager.create_profile("Third", "local", "model3", 384)

        profiles = manager.list_profiles()

        assert len(profiles) == 3
        names = {p.name for p in profiles}
        assert names == {"First", "Second", "Third"}

        manager.close()

    def test_update_profile(self) -> None:
        """Manager should update profile mutable fields."""
        manager = ProfileManager()

        manager.create_profile(
            name="Original Name",
            provider="google",
            model="text-embedding-004",
            dimension=768,
            profile_id="update-test",
        )

        updated = manager.update_profile(
            "update-test",
            name="New Name",
            description="Added description",
        )

        assert updated is not None
        assert updated.name == "New Name"
        assert updated.description == "Added description"
        # Immutable fields unchanged
        assert updated.provider == "google"
        assert updated.dimension == 768

        manager.close()

    def test_delete_profile(self) -> None:
        """Manager should delete profiles."""
        manager = ProfileManager()

        manager.create_profile(
            name="To Delete",
            provider="google",
            model="test",
            dimension=768,
            profile_id="delete-test",
        )

        result = manager.delete_profile("delete-test")

        assert result is True
        assert manager.get_profile("delete-test") is None

        manager.close()

    def test_delete_nonexistent_profile(self) -> None:
        """Deleting nonexistent profile should return False."""
        manager = ProfileManager()

        result = manager.delete_profile("does-not-exist")

        assert result is False

        manager.close()


# =============================================================================
# Book Index Status Management Tests
# =============================================================================


class TestProfileManagerBookStatus:
    """Tests for ProfileManager book status operations."""

    def test_set_book_status(self) -> None:
        """Manager should set book status."""
        manager = ProfileManager()
        manager.create_profile("Test", "google", "model", 768, profile_id="profile-1")

        book_id = BookIdentifier("lib-1", 42, "EPUB")
        status = manager.set_book_status(
            book_id=book_id,
            profile_id="profile-1",
            status=IndexStatus.COMPLETE,
            chunk_count=150,
        )

        assert status.status == IndexStatus.COMPLETE
        assert status.chunk_count == 150
        assert status.indexed_at is not None

        manager.close()

    def test_get_book_status(self) -> None:
        """Manager should retrieve book status."""
        manager = ProfileManager()
        manager.create_profile("Test", "google", "model", 768, profile_id="profile-1")

        book_id = BookIdentifier("lib-1", 42, "EPUB")
        manager.set_book_status(book_id, "profile-1", IndexStatus.COMPLETE, 100)

        status = manager.get_book_status(book_id, "profile-1")

        assert status is not None
        assert status.status == IndexStatus.COMPLETE
        assert status.chunk_count == 100

        manager.close()

    def test_get_nonexistent_book_status(self) -> None:
        """Getting status for unindexed book should return None."""
        manager = ProfileManager()
        manager.create_profile("Test", "google", "model", 768, profile_id="profile-1")

        book_id = BookIdentifier("lib-1", 99, "EPUB")
        status = manager.get_book_status(book_id, "profile-1")

        assert status is None

        manager.close()

    def test_get_books_in_profile(self) -> None:
        """Manager should list all books in a profile."""
        manager = ProfileManager()
        manager.create_profile("Test", "google", "model", 768, profile_id="profile-1")

        book1 = BookIdentifier("lib-1", 1, "EPUB")
        book2 = BookIdentifier("lib-1", 2, "EPUB")
        book3 = BookIdentifier("lib-1", 3, "EPUB")

        manager.set_book_status(book1, "profile-1", IndexStatus.COMPLETE, 100)
        manager.set_book_status(book2, "profile-1", IndexStatus.COMPLETE, 200)
        manager.set_book_status(book3, "profile-1", IndexStatus.FAILED)

        all_books = manager.get_books_in_profile("profile-1")
        assert len(all_books) == 3

        complete_books = manager.get_books_in_profile(
            "profile-1", status=IndexStatus.COMPLETE
        )
        assert len(complete_books) == 2

        manager.close()

    def test_get_profiles_for_book(self) -> None:
        """Manager should find all profiles containing a book."""
        manager = ProfileManager()
        manager.create_profile("Profile A", "google", "model", 768, profile_id="a")
        manager.create_profile("Profile B", "openai", "model", 1536, profile_id="b")

        book_id = BookIdentifier("lib-1", 42, "EPUB")

        manager.set_book_status(book_id, "a", IndexStatus.COMPLETE, 100)
        manager.set_book_status(book_id, "b", IndexStatus.COMPLETE, 150)

        profiles = manager.get_profiles_for_book(book_id)

        assert len(profiles) == 2
        profile_ids = {p[0].id for p in profiles}
        assert profile_ids == {"a", "b"}

        manager.close()

    def test_remove_book_from_profile(self) -> None:
        """Manager should remove book from profile."""
        manager = ProfileManager()
        manager.create_profile("Test", "google", "model", 768, profile_id="profile-1")

        book_id = BookIdentifier("lib-1", 42, "EPUB")
        manager.set_book_status(book_id, "profile-1", IndexStatus.COMPLETE, 100)

        result = manager.remove_book_from_profile(book_id, "profile-1")

        assert result is True
        assert manager.get_book_status(book_id, "profile-1") is None

        manager.close()

    def test_profile_stats(self) -> None:
        """Manager should calculate profile statistics."""
        manager = ProfileManager()
        manager.create_profile("Test", "google", "model", 768, profile_id="profile-1")

        book1 = BookIdentifier("lib-1", 1, "EPUB")
        book2 = BookIdentifier("lib-1", 2, "EPUB")
        book3 = BookIdentifier("lib-1", 3, "EPUB")

        manager.set_book_status(book1, "profile-1", IndexStatus.COMPLETE, 100)
        manager.set_book_status(book2, "profile-1", IndexStatus.COMPLETE, 200)
        manager.set_book_status(book3, "profile-1", IndexStatus.FAILED)

        stats = manager.get_profile_stats("profile-1")

        assert stats["total_books"] == 3
        assert stats["indexed_books"] == 2
        assert stats["failed_books"] == 1
        assert stats["total_chunks"] == 300

        manager.close()


# =============================================================================
# Utility Function Tests
# =============================================================================


class TestUtilityFunctions:
    """Tests for utility functions."""

    def test_generate_profile_id(self) -> None:
        """Should generate unique profile IDs."""
        id1 = generate_profile_id("My Profile", "google", 768)
        id2 = generate_profile_id("My Profile", "google", 768)

        # Should contain slugified name
        assert "my-profile" in id1
        # Should contain provider
        assert "google" in id1
        # Should contain dimension
        assert "768" in id1
        # Should be unique even with same inputs
        assert id1 != id2
