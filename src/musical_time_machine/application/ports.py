"""@file
@brief Ports the use cases need from the outside world.
"""

from datetime import date
from typing import Protocol

from musical_time_machine.domain.playlist import Playlist
from musical_time_machine.domain.song import Song


class ChartSource(Protocol):
    """@brief Supplies the songs of one chart."""

    def songs_for(self, chart_date: date) -> list[Song]:
        """@brief Get the songs of the chart of a date.

        @param chart_date Date of the chart.
        @return The songs in chart order.
        """
        ...


class MusicService(Protocol):
    """@brief The user's music streaming account."""

    def library_playlists(self) -> list[Playlist]:
        """@brief Get every playlist in the user's library.

        @return The playlists of the library.
        """
        ...

    def create_playlist(self, title: str, description: str, privacy: str) -> str:
        """@brief Create a playlist in the user's library.

        @param title Playlist title.
        @param description Playlist description.
        @param privacy Privacy status, for example "PRIVATE".
        @return The identifier of the new playlist.
        """
        ...

    def search_song(self, title: str, artist: str) -> str | None:
        """@brief Find a song.

        @param title Song title.
        @param artist Performing artist.
        @return The video id of the top song result, or None when nothing was found.
        """
        ...

    def add_song(self, playlist_id: str, video_id: str) -> None:
        """@brief Add a song to a playlist.

        @param playlist_id Identifier of the playlist.
        @param video_id Video id of the song.
        """
        ...
