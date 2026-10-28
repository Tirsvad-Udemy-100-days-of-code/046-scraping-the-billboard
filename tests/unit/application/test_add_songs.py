"""@file
@brief Tests of the add_songs and time_travel use cases with fake ports.
"""

from datetime import date

import pytest
from conftest import FakeChartSource, FakeMusicService

from musical_time_machine.application.use_cases import add_songs, time_travel
from musical_time_machine.constants import ADD_PAUSE_SECONDS
from musical_time_machine.domain.errors import (
    AuthenticationError,
    BrowserFileMissingError,
    SongAddError,
    SongSearchError,
)
from musical_time_machine.domain.song import Song

ONE = Song("One", "A")
TWO = Song("Two", "B")
THREE = Song("Three", "C")


def _no_pause(_seconds: float) -> None:
    return None


def test_add_songs_adds_every_found_song() -> None:
    service = FakeMusicService()

    result = add_songs([ONE, TWO], "pl", service, pause=_no_pause)

    assert (result.added, result.skipped) == (2, [])
    assert service.added == [("pl", "vid-One"), ("pl", "vid-Two")]
    assert service.searched == [("One", "A"), ("Two", "B")]


def test_add_songs_skips_song_not_found() -> None:
    service = FakeMusicService(video_ids={"One": "v1", "Three": "v3"})

    result = add_songs([ONE, TWO, THREE], "pl", service, pause=_no_pause)

    assert result.added == 2
    assert result.skipped == [TWO]
    assert service.added == [("pl", "v1"), ("pl", "v3")]


def test_add_songs_skips_song_whose_add_fails_and_continues() -> None:
    service = FakeMusicService(add_errors={"vid-One": SongAddError("no")})

    result = add_songs([ONE, TWO], "pl", service, pause=_no_pause)

    assert result.added == 1
    assert result.skipped == [ONE]
    assert service.added == [("pl", "vid-Two")]


def test_add_songs_skips_song_whose_search_fails_and_continues() -> None:
    service = FakeMusicService(search_errors={"One": SongSearchError("no")})

    result = add_songs([ONE, TWO], "pl", service, pause=_no_pause)

    assert (result.added, result.skipped) == (1, [ONE])


@pytest.mark.parametrize("error", [AuthenticationError("auth"), BrowserFileMissingError("gone")])
def test_add_songs_propagates_login_errors(error: Exception) -> None:
    service = FakeMusicService(search_errors={"One": error})

    with pytest.raises(type(error)):
        add_songs([ONE, TWO], "pl", service, pause=_no_pause)

    assert service.searched == [("One", "A")]


def test_add_songs_pauses_between_songs_only() -> None:
    pauses: list[float] = []

    add_songs([ONE, TWO, THREE], "pl", FakeMusicService(), pause=pauses.append)

    assert pauses == [ADD_PAUSE_SECONDS, ADD_PAUSE_SECONDS]


def test_add_songs_with_no_songs_adds_nothing() -> None:
    pauses: list[float] = []

    result = add_songs([], "pl", FakeMusicService(), pause=pauses.append)

    assert (result.added, result.skipped, pauses) == (0, [], [])


def test_time_travel_scrapes_creates_playlist_and_adds() -> None:
    source = FakeChartSource([ONE, TWO, THREE])
    service = FakeMusicService(video_ids={"One": "v1", "Three": "v3"})

    result = time_travel(date(2026, 4, 18), source, service, pause=_no_pause)

    playlist_id = result.playlist.playlist_id
    assert source.requested == [date(2026, 4, 18)]
    assert result.playlist.title == "2026-04-18 Billboard 100"
    assert result.playlist.created is True
    assert (result.added, result.skipped, result.total) == (2, [TWO], 3)
    assert service.added == [(playlist_id, "v1"), (playlist_id, "v3")]
