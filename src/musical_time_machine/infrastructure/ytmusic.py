"""@file
@brief YouTube Music (ytmusicapi) as a music service.
"""

import logging
from collections.abc import Callable
from pathlib import Path
from typing import Any, Protocol

from ytmusicapi import YTMusic
from ytmusicapi.exceptions import YTMusicError, YTMusicServerError

from musical_time_machine.constants import (
    AUTH_HTTP_CODES,
    BROWSER_FILE_MISSING_REASON,
    BROWSER_FILE_NAME,
    BROWSER_RENEWAL_MESSAGE,
    PLAYLIST_CREATION_FAILED_MESSAGE,
    SEARCH_FILTER,
    SEARCH_LIMIT,
    SONG_ADD_FAILED_MESSAGE,
    SONG_SEARCH_FAILED_MESSAGE,
    STATUS_SUCCEEDED,
)
from musical_time_machine.domain.errors import (
    AuthenticationError,
    BrowserFileMissingError,
    PlaylistCreationError,
    SongAddError,
    SongSearchError,
)
from musical_time_machine.domain.playlist import Playlist

_logger = logging.getLogger(__name__)

## ytmusicapi errors plus the parsing errors a stale or malformed headers file causes.
_CLIENT_ERRORS = (YTMusicError, KeyError, ValueError)


class YTMusicLike(Protocol):
    """@brief The part of the ytmusicapi client this adapter uses."""

    def get_library_playlists(
        self,
        limit: int | None = ...,
    ) -> list[dict[str, Any]]:  # ytmusicapi returns untyped JSON dictionaries
        """@brief List the library playlists as raw dictionaries."""
        ...

    def create_playlist(
        self,
        title: str,
        description: str,
        privacy_status: str = ...,
    ) -> str | dict[str, Any]:  # the id on success, an error dictionary on failure
        """@brief Create a playlist; returns its id or an error dictionary."""
        ...

    def search(
        self,
        query: str,
        filter: str | None = ...,
        limit: int = ...,
    ) -> list[dict[str, Any]]:  # ytmusicapi returns untyped JSON dictionaries
        """@brief Search YouTube Music; returns the raw results."""
        ...

    def add_playlist_items(
        self,
        playlistId: str,  # noqa: N803 - must match the ytmusicapi parameter names
        videoIds: list[str] | None = ...,  # noqa: N803
        duplicates: bool = ...,
    ) -> str | dict[str, Any]:  # a status dictionary, or the raw answer on failure
        """@brief Add videos to a playlist; returns the status answer."""
        ...


class YouTubeMusicService:
    """@brief MusicService backed by ytmusicapi and a browser headers file."""

    def __init__(
        self,
        browser_file: Path = Path(BROWSER_FILE_NAME),
        client_factory: Callable[[str], YTMusicLike] = YTMusic,
    ) -> None:
        """@brief Create the service; the network is not touched until first use.

        @param browser_file File with the browser request headers.
        @param client_factory Builds a client from the path of the browser file.
        """
        self._browser_file = browser_file
        self._client_factory = client_factory
        self._client: YTMusicLike | None = None

    def library_playlists(self) -> list[Playlist]:
        """@brief Get every playlist in the user's library.

        @return The playlists of the library.
        @throws BrowserFileMissingError when the browser file does not exist.
        @throws AuthenticationError when YouTube Music rejects the headers.
        """
        client = self._connect()
        try:
            raw = client.get_library_playlists(limit=None)
            return [
                Playlist(playlist_id=item["playlistId"], title=item["title"])
                for item in raw
                if item.get("playlistId") and item.get("title")
            ]
        except _CLIENT_ERRORS as error:
            raise self._rejected(error) from error

    def create_playlist(self, title: str, description: str, privacy: str) -> str:
        """@brief Create a playlist in the user's library.

        @param title Playlist title.
        @param description Playlist description.
        @param privacy Privacy status, for example "PRIVATE".
        @return The identifier of the new playlist.
        @throws BrowserFileMissingError when the browser file does not exist.
        @throws AuthenticationError when YouTube Music rejects the headers.
        @throws PlaylistCreationError when YouTube Music answers without a playlist id.
        """
        client = self._connect()
        try:
            result = client.create_playlist(title, description, privacy_status=privacy)
        except _CLIENT_ERRORS as error:
            raise self._rejected(error) from error
        if not isinstance(result, str):
            raise PlaylistCreationError(PLAYLIST_CREATION_FAILED_MESSAGE.format(reason=result))
        return result

    def search_song(self, title: str, artist: str) -> str | None:
        """@brief Find the top song result for a title and artist.

        @param title Song title.
        @param artist Performing artist.
        @return The video id of the first song result, or None when nothing was found.
        @throws BrowserFileMissingError when the browser file does not exist.
        @throws AuthenticationError when YouTube Music rejects the headers.
        @throws SongSearchError when the search fails.
        """
        client = self._connect()
        try:
            results = client.search(f"{title} {artist}", filter=SEARCH_FILTER, limit=SEARCH_LIMIT)
        except _CLIENT_ERRORS as error:
            raise self._failure(error, SongSearchError, SONG_SEARCH_FAILED_MESSAGE) from error
        for result in results:
            video_id = result.get("videoId")
            if video_id:
                return str(video_id)
        return None

    def add_song(self, playlist_id: str, video_id: str) -> None:
        """@brief Add a song to a playlist, without duplicates.

        @param playlist_id Identifier of the playlist.
        @param video_id Video id of the song.
        @throws BrowserFileMissingError when the browser file does not exist.
        @throws AuthenticationError when YouTube Music rejects the headers.
        @throws SongAddError when YouTube Music does not confirm the addition.
        """
        client = self._connect()
        try:
            answer = client.add_playlist_items(playlist_id, [video_id], duplicates=False)
        except _CLIENT_ERRORS as error:
            raise self._failure(error, SongAddError, SONG_ADD_FAILED_MESSAGE) from error
        status = answer.get("status") if isinstance(answer, dict) else None
        if status != STATUS_SUCCEEDED:
            raise SongAddError(SONG_ADD_FAILED_MESSAGE.format(reason=answer))

    def _failure(
        self,
        error: Exception,
        song_error: type[SongSearchError] | type[SongAddError],
        template: str,
    ) -> AuthenticationError | SongSearchError | SongAddError:
        # A server error is a failure of this song; a 401/403 or a parse error is a rejected login.
        is_server_error = isinstance(error, YTMusicServerError)
        if is_server_error and not any(code in str(error) for code in AUTH_HTTP_CODES):
            return song_error(template.format(reason=error))
        return self._rejected(error)

    def _connect(self) -> YTMusicLike:
        if self._client is not None:
            return self._client
        if not self._browser_file.is_file():
            reason = BROWSER_FILE_MISSING_REASON.format(file=self._browser_file)
            raise BrowserFileMissingError(self._renewal(reason))
        try:
            self._client = self._client_factory(str(self._browser_file))
        except _CLIENT_ERRORS as error:
            raise self._rejected(error) from error
        return self._client

    def _rejected(self, error: Exception) -> AuthenticationError:
        _logger.debug("YouTube Music rejected the login", exc_info=error)
        return AuthenticationError(self._renewal(str(error)))

    def _renewal(self, reason: str) -> str:
        return BROWSER_RENEWAL_MESSAGE.format(reason=reason, file=self._browser_file)
