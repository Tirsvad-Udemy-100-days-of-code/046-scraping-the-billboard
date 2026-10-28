"""@file
@brief YouTube Music (ytmusicapi) as a music service.
"""

import logging
from collections.abc import Callable
from pathlib import Path
from typing import Any, Protocol

from ytmusicapi import YTMusic
from ytmusicapi.exceptions import YTMusicError

from musical_time_machine.constants import (
    BROWSER_FILE_MISSING_REASON,
    BROWSER_FILE_NAME,
    BROWSER_RENEWAL_MESSAGE,
)
from musical_time_machine.domain.errors import AuthenticationError, BrowserFileMissingError
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
