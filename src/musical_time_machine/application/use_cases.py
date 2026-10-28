"""@file
@brief Use cases of the Musical Time Machine.
"""

from datetime import date

from musical_time_machine.application.ports import ChartSource, MusicService
from musical_time_machine.domain.song import Song


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
