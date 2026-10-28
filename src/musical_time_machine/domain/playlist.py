"""@file
@brief The Playlist value object.
"""

from dataclasses import dataclass
from datetime import date

from musical_time_machine.constants import (
    DATE_FORMAT,
    PLAYLIST_DESCRIPTION_TEMPLATE,
    PLAYLIST_NAME_TEMPLATE,
)


@dataclass(frozen=True, slots=True)
class Playlist:
    """@brief One playlist of the user's library.

    @param playlist_id Identifier given by the music service.
    @param title Playlist title.
    """

    playlist_id: str
    title: str


def playlist_name(chart_date: date) -> str:
    """@brief Get the title of the playlist for a chart date.

    @param chart_date Date of the chart.
    @return The title, for example "2026-04-18 Billboard 100".
    """
    return PLAYLIST_NAME_TEMPLATE.format(date=chart_date.strftime(DATE_FORMAT))


def playlist_description(chart_date: date) -> str:
    """@brief Get the description of the playlist for a chart date.

    @param chart_date Date of the chart.
    @return The description text.
    """
    return PLAYLIST_DESCRIPTION_TEMPLATE.format(date=chart_date.strftime(DATE_FORMAT))
