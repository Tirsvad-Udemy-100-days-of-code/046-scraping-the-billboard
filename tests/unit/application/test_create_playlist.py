"""@file
@brief Tests of the create_playlist use case.
"""

from datetime import date

import pytest
from conftest import FakeMusicService

from musical_time_machine.application.use_cases import create_playlist
from musical_time_machine.domain.errors import AuthenticationError
from musical_time_machine.domain.playlist import Playlist

TITLE = "2026-04-18 Billboard 100"


def test_create_playlist_creates_one_private_playlist() -> None:
    service = FakeMusicService()

    result = create_playlist(date(2026, 4, 18), service)

    assert result.created is True
    assert result.title == TITLE
    assert len(service.created) == 1
    title, description, privacy = service.created[0]
    assert (title, privacy) == (TITLE, "PRIVATE")
    assert "2026-04-18" in description
    assert result.playlist_id == service.library_playlists()[0].playlist_id


def test_create_playlist_twice_for_same_date_creates_no_duplicate() -> None:
    service = FakeMusicService()
    first = create_playlist(date(2026, 4, 18), service)

    second = create_playlist(date(2026, 4, 18), service)

    assert second.created is False
    assert second.playlist_id == first.playlist_id
    assert len(service.created) == 1
    assert len(service.library_playlists()) == 1


def test_create_playlist_for_other_date_creates_second_playlist() -> None:
    service = FakeMusicService()
    create_playlist(date(2026, 4, 18), service)

    result = create_playlist(date(2026, 4, 19), service)

    assert result.created is True
    assert len(service.library_playlists()) == 2


def test_create_playlist_returns_existing_playlist_of_library() -> None:
    service = FakeMusicService([Playlist("x", "Other"), Playlist("abc", TITLE)])

    result = create_playlist(date(2026, 4, 18), service)

    assert (result.playlist_id, result.created) == ("abc", False)
    assert service.created == []


def test_create_playlist_propagates_authentication_error() -> None:
    with pytest.raises(AuthenticationError):
        create_playlist(date(2026, 4, 18), FakeMusicService(error=AuthenticationError("no")))
