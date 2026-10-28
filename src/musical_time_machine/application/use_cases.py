"""@file
@brief Use cases of the Musical Time Machine.
"""

from dataclasses import dataclass
from datetime import date

from musical_time_machine.application.ports import ChartSource, MusicService
from musical_time_machine.constants import PLAYLIST_PRIVACY
from musical_time_machine.domain.playlist import playlist_description, playlist_name
from musical_time_machine.domain.song import Song


@dataclass(frozen=True, slots=True)
class PlaylistResult:
    """@brief Outcome of create_playlist.

    @param playlist_id Identifier of the new or the existing playlist.
    @param title Playlist title.
    @param created True when a playlist was made, False when it already existed.
    """

    playlist_id: str
    title: str
    created: bool


def scrape_songs(chart_date: date, source: ChartSource) -> list[Song]:
    """@brief Get the songs of the chart of a date.

    @param chart_date Date of the chart.
    @param source Where the chart comes from.
    @return The songs in chart order.
    """
    return source.songs_for(chart_date)


def scrape_titles(chart_date: date, source: ChartSource) -> list[str]:
    """@brief Get the song titles of the chart of a date.

    @param chart_date Date of the chart.
    @param source Where the chart comes from.
    @return The titles in chart order.
    """
    return [song.title for song in scrape_songs(chart_date, source)]


def count_library_playlists(service: MusicService) -> int:
    """@brief Count the playlists in the user's library.

    @param service The music service to ask.
    @return The number of playlists.
    """
    return len(service.library_playlists())


def create_playlist(chart_date: date, service: MusicService) -> PlaylistResult:
    """@brief Create the private playlist of a chart date unless it already exists.

    @param chart_date Date of the chart.
    @param service The music service to ask.
    @return The new playlist, or the existing one with the same title.
    """
    title = playlist_name(chart_date)
    for playlist in service.library_playlists():
        if playlist.title == title:
            return PlaylistResult(playlist.playlist_id, title, created=False)
    playlist_id = service.create_playlist(title, playlist_description(chart_date), PLAYLIST_PRIVACY)
    return PlaylistResult(playlist_id, title, created=True)
