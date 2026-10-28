"""@file
@brief Use cases of the Musical Time Machine.
"""

import time
from collections.abc import Callable
from dataclasses import dataclass
from datetime import date

from musical_time_machine.application.ports import ChartSource, MusicService
from musical_time_machine.constants import ADD_PAUSE_SECONDS, PLAYLIST_PRIVACY
from musical_time_machine.domain.errors import SongAddError, SongSearchError
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


@dataclass(frozen=True, slots=True)
class AddSongsResult:
    """@brief Outcome of add_songs.

    @param added Number of songs added to the playlist.
    @param skipped Songs that were not found or could not be added.
    """

    added: int
    skipped: list[Song]


@dataclass(frozen=True, slots=True)
class TimeTravelResult:
    """@brief Outcome of time_travel.

    @param playlist The new or existing playlist.
    @param added Number of songs added.
    @param skipped Songs that were not found or could not be added.
    @param total Number of songs on the chart.
    """

    playlist: PlaylistResult
    added: int
    skipped: list[Song]
    total: int


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


def add_songs(
    songs: list[Song],
    playlist_id: str,
    service: MusicService,
    *,
    pause: Callable[[float], None] = time.sleep,
) -> AddSongsResult:
    """@brief Search every song and add the found ones to a playlist.

    A song that is not found, or whose search or add fails, is skipped and the
    run continues. Authentication errors are not caught: they stop the run.

    @param songs The songs in chart order.
    @param playlist_id Identifier of the target playlist.
    @param service The music service to ask.
    @param pause Called with the seconds to wait between two songs.
    @return The number added and the skipped songs.
    """
    added = 0
    skipped: list[Song] = []
    for index, song in enumerate(songs):
        if index > 0:
            pause(ADD_PAUSE_SECONDS)
        try:
            video_id = service.search_song(song.title, song.artist)
            if video_id is None:
                skipped.append(song)
                continue
            service.add_song(playlist_id, video_id)
        except (SongSearchError, SongAddError):
            skipped.append(song)
            continue
        added += 1
    return AddSongsResult(added, skipped)


def time_travel(
    chart_date: date,
    chart_source: ChartSource,
    service: MusicService,
    *,
    pause: Callable[[float], None] = time.sleep,
) -> TimeTravelResult:
    """@brief Scrape the chart, make its playlist and fill it.

    @param chart_date Date of the chart.
    @param chart_source Where the chart comes from.
    @param service The music service to ask.
    @param pause Called with the seconds to wait between two songs.
    @return The playlist and what was added or skipped.
    """
    songs = scrape_songs(chart_date, chart_source)
    playlist = create_playlist(chart_date, service)
    added = add_songs(songs, playlist.playlist_id, service, pause=pause)
    return TimeTravelResult(playlist, added.added, added.skipped, len(songs))
