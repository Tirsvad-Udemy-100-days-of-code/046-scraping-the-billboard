"""@file
@brief Shared fixtures: the stored Bakeboard page and a fake chart source.
"""

from datetime import date
from pathlib import Path

import pytest

from musical_time_machine.domain.playlist import Playlist
from musical_time_machine.domain.song import Song

FIXTURE_PAGE = Path(__file__).parent / "fixtures" / "bakeboard-2026-04-18.html"


@pytest.fixture
def chart_html() -> str:
    """@brief The stored 2026-04-18 chart page."""
    return FIXTURE_PAGE.read_text(encoding="utf-8")


class FakeChartSource:
    """@brief ChartSource returning fixed songs, or raising a given error."""

    def __init__(self, songs: list[Song] | None = None, error: Exception | None = None) -> None:
        self._songs = songs or []
        self._error = error
        self.requested: list[date] = []

    def songs_for(self, chart_date: date) -> list[Song]:
        self.requested.append(chart_date)
        if self._error is not None:
            raise self._error
        return self._songs


class FakeMusicService:
    """@brief MusicService returning fixed playlists, or raising a given error."""

    def __init__(
        self, playlists: list[Playlist] | None = None, error: Exception | None = None
    ) -> None:
        self._playlists = list(playlists or [])
        self._error = error
        self.created: list[tuple[str, str, str]] = []

    def create_playlist(self, title: str, description: str, privacy: str) -> str:
        if self._error is not None:
            raise self._error
        self.created.append((title, description, privacy))
        playlist_id = f"new-{len(self._playlists) + 1}"
        self._playlists.append(Playlist(playlist_id, title))
        return playlist_id

    def library_playlists(self) -> list[Playlist]:
        if self._error is not None:
            raise self._error
        return self._playlists
