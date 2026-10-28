"""@file
@brief Tests of the YouTube Music adapter with a fake client factory.
"""

from pathlib import Path
from typing import Any

import pytest
from ytmusicapi.exceptions import YTMusicServerError, YTMusicUserError

from musical_time_machine.domain.errors import (
    AuthenticationError,
    BrowserFileMissingError,
    PlaylistCreationError,
    SongAddError,
    SongSearchError,
)
from musical_time_machine.domain.playlist import Playlist
from musical_time_machine.infrastructure.ytmusic import YouTubeMusicService, YTMusicLike


class _FakeClient:
    def __init__(
        self,
        items: list[dict[str, Any]],
        error: Exception | None = None,
        created: str | dict[str, Any] = "new-id",
        results: list[dict[str, Any]] | None = None,
        added: str | dict[str, Any] = "ignored",
    ) -> None:
        self._results = results or []
        self._added = added
        self.searches: list[tuple[str, str | None, int]] = []
        self.additions: list[tuple[str, list[str] | None, bool]] = []
        self._items = items
        self._error = error
        self._created = created
        self.limits: list[int | None] = []
        self.creations: list[tuple[str, str, str]] = []

    def create_playlist(
        self, title: str, description: str, privacy_status: str = "PRIVATE"
    ) -> str | dict[str, Any]:
        self.creations.append((title, description, privacy_status))
        if self._error is not None:
            raise self._error
        return self._created

    def search(
        self, query: str, filter: str | None = None, limit: int = 20
    ) -> list[dict[str, Any]]:
        self.searches.append((query, filter, limit))
        if self._error is not None:
            raise self._error
        return self._results

    def add_playlist_items(
        self,
        playlistId: str,  # noqa: N803 - must match the ytmusicapi parameter names
        videoIds: list[str] | None = None,  # noqa: N803
        duplicates: bool = False,
    ) -> str | dict[str, Any]:
        self.additions.append((playlistId, videoIds, duplicates))
        if self._error is not None:
            raise self._error
        return self._added

    def get_library_playlists(self, limit: int | None = 25) -> list[dict[str, Any]]:
        self.limits.append(limit)
        if self._error is not None:
            raise self._error
        return self._items


def _browser_file(tmp_path: Path) -> Path:
    path = tmp_path / "browser.json"
    path.write_text("{}", encoding="utf-8")
    return path


def test_constructor_does_not_call_the_factory(tmp_path: Path) -> None:
    calls: list[str] = []

    def factory(auth: str) -> YTMusicLike:
        calls.append(auth)
        return _FakeClient([])

    YouTubeMusicService(tmp_path / "missing.json", factory)

    assert calls == []


def test_library_playlists_maps_entries_and_asks_for_all(tmp_path: Path) -> None:
    client = _FakeClient(
        [{"playlistId": "p1", "title": "One"}, {"playlistId": "p2", "title": "Two"}]
    )
    service = YouTubeMusicService(_browser_file(tmp_path), lambda _auth: client)

    assert service.library_playlists() == [Playlist("p1", "One"), Playlist("p2", "Two")]
    assert client.limits == [None]


def test_library_playlists_skips_entries_without_id_or_title(tmp_path: Path) -> None:
    client = _FakeClient(
        [{"title": "No id"}, {"playlistId": "p"}, {"playlistId": "ok", "title": "T"}]
    )
    service = YouTubeMusicService(_browser_file(tmp_path), lambda _auth: client)

    assert service.library_playlists() == [Playlist("ok", "T")]


def test_library_playlists_raises_when_browser_file_missing(tmp_path: Path) -> None:
    service = YouTubeMusicService(tmp_path / "browser.json", lambda _auth: _FakeClient([]))

    with pytest.raises(BrowserFileMissingError) as info:
        service.library_playlists()

    message = str(info.value)
    for step in ("Firefox", "music.youtube.com", "browse", "ytmusicapi browser", "pbpaste"):
        assert step in message


def test_library_playlists_raises_authentication_error_when_factory_fails(tmp_path: Path) -> None:
    def factory(_auth: str) -> YTMusicLike:
        raise YTMusicUserError("bad headers")

    service = YouTubeMusicService(_browser_file(tmp_path), factory)

    with pytest.raises(AuthenticationError, match="ytmusicapi browser") as info:
        service.library_playlists()
    assert isinstance(info.value.__cause__, YTMusicUserError)


@pytest.mark.parametrize("error", [YTMusicUserError("x"), KeyError("cookie"), ValueError("bad")])
def test_library_playlists_raises_authentication_error_when_listing_fails(
    tmp_path: Path, error: Exception
) -> None:
    client = _FakeClient([], error)
    service = YouTubeMusicService(_browser_file(tmp_path), lambda _auth: client)

    with pytest.raises(AuthenticationError):
        service.library_playlists()


def test_library_playlists_builds_the_client_once(tmp_path: Path) -> None:
    calls: list[str] = []

    def factory(auth: str) -> YTMusicLike:
        calls.append(auth)
        return _FakeClient([])

    service = YouTubeMusicService(_browser_file(tmp_path), factory)
    service.library_playlists()
    service.library_playlists()

    assert len(calls) == 1


def test_create_playlist_returns_id_and_passes_privacy(tmp_path: Path) -> None:
    client = _FakeClient([])
    service = YouTubeMusicService(_browser_file(tmp_path), lambda _auth: client)

    assert service.create_playlist("T", "D", "PRIVATE") == "new-id"
    assert client.creations == [("T", "D", "PRIVATE")]


def test_create_playlist_raises_when_result_is_not_an_id(tmp_path: Path) -> None:
    client = _FakeClient([], created={"error": "quota exceeded"})
    service = YouTubeMusicService(_browser_file(tmp_path), lambda _auth: client)

    with pytest.raises(PlaylistCreationError, match="quota exceeded"):
        service.create_playlist("T", "D", "PRIVATE")


@pytest.mark.parametrize("error", [YTMusicUserError("x"), KeyError("cookie"), ValueError("bad")])
def test_create_playlist_raises_authentication_error_when_client_fails(
    tmp_path: Path, error: Exception
) -> None:
    client = _FakeClient([], error)
    service = YouTubeMusicService(_browser_file(tmp_path), lambda _auth: client)

    with pytest.raises(AuthenticationError) as info:
        service.create_playlist("T", "D", "PRIVATE")
    assert info.value.__cause__ is error


def test_create_playlist_raises_when_browser_file_missing(tmp_path: Path) -> None:
    service = YouTubeMusicService(tmp_path / "none.json", lambda _auth: _FakeClient([]))

    with pytest.raises(BrowserFileMissingError):
        service.create_playlist("T", "D", "PRIVATE")


def _service(tmp_path: Path, client: _FakeClient) -> YouTubeMusicService:
    return YouTubeMusicService(_browser_file(tmp_path), lambda _auth: client)


def test_search_song_returns_first_video_id_and_filters_songs(tmp_path: Path) -> None:
    client = _FakeClient([], results=[{"videoId": "v1"}, {"videoId": "v2"}])

    assert _service(tmp_path, client).search_song("Title", "Artist") == "v1"
    assert client.searches == [("Title Artist", "songs", 1)]


def test_search_song_returns_none_for_no_results(tmp_path: Path) -> None:
    assert _service(tmp_path, _FakeClient([])).search_song("T", "A") is None


def test_search_song_skips_results_without_video_id(tmp_path: Path) -> None:
    client = _FakeClient([], results=[{"title": "x"}, {"videoId": "v2"}])

    assert _service(tmp_path, client).search_song("T", "A") == "v2"


def test_search_song_maps_server_error_to_song_search_error(tmp_path: Path) -> None:
    error = YTMusicServerError("Server returned HTTP 500: oops")
    service = _service(tmp_path, _FakeClient([], error))

    with pytest.raises(SongSearchError) as info:
        service.search_song("T", "A")
    assert info.value.__cause__ is error


@pytest.mark.parametrize(
    "error",
    [YTMusicServerError("Server returned HTTP 401: no"), YTMusicUserError("x"), KeyError("k")],
)
def test_search_song_keeps_login_failures_as_authentication_error(
    tmp_path: Path, error: Exception
) -> None:
    with pytest.raises(AuthenticationError):
        _service(tmp_path, _FakeClient([], error)).search_song("T", "A")


def test_add_song_sends_one_video_without_duplicates(tmp_path: Path) -> None:
    client = _FakeClient([], added={"status": "STATUS_SUCCEEDED", "playlistEditResults": []})

    _service(tmp_path, client).add_song("pl", "v1")

    assert client.additions == [("pl", ["v1"], False)]


@pytest.mark.parametrize("answer", [{"status": "STATUS_FAILED"}, {"error": "dup"}, "oops"])
def test_add_song_raises_when_status_is_not_succeeded(
    tmp_path: Path, answer: str | dict[str, Any]
) -> None:
    service = _service(tmp_path, _FakeClient([], added=answer))

    with pytest.raises(SongAddError):
        service.add_song("pl", "v1")


def test_add_song_maps_server_error_to_song_add_error(tmp_path: Path) -> None:
    error = YTMusicServerError("Server returned HTTP 400: bad")

    with pytest.raises(SongAddError) as info:
        _service(tmp_path, _FakeClient([], error)).add_song("pl", "v1")
    assert info.value.__cause__ is error


def test_add_song_keeps_login_failure_as_authentication_error(tmp_path: Path) -> None:
    with pytest.raises(AuthenticationError):
        _service(tmp_path, _FakeClient([], KeyError("cookie"))).add_song("pl", "v1")


def test_search_song_raises_when_browser_file_missing(tmp_path: Path) -> None:
    service = YouTubeMusicService(tmp_path / "none.json", lambda _auth: _FakeClient([]))

    with pytest.raises(BrowserFileMissingError):
        service.search_song("T", "A")
