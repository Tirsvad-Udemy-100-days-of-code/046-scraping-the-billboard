"""@file
@brief Bakeboard Hot 100 clone as a chart source.
"""

import logging
from collections.abc import Callable
from datetime import date

import requests
from bs4 import BeautifulSoup

from musical_time_machine.constants import (
    BASE_URL,
    CHART_PARSE_MESSAGE,
    CHART_UNAVAILABLE_MESSAGE,
    DATE_FORMAT,
    REQUEST_HEADERS,
    REQUEST_TIMEOUT_SECONDS,
    SELECTOR_ARTIST,
    SELECTOR_ROW,
    SELECTOR_TITLE,
)
from musical_time_machine.domain.errors import ChartParseError, ChartUnavailableError
from musical_time_machine.domain.song import Song

_logger = logging.getLogger(__name__)


def parse_chart(html: str) -> list[Song]:
    """@brief Extract the songs from a chart page.

    @param html The page markup.
    @return The songs in page order.
    @throws ChartParseError when the page holds no songs.
    """
    soup = BeautifulSoup(html, "html.parser")
    songs: list[Song] = []
    for row in soup.select(SELECTOR_ROW):
        title = row.select_one(SELECTOR_TITLE)
        artist = row.select_one(SELECTOR_ARTIST)
        if title is None or artist is None:
            _logger.warning("Skipping a chart row without title or artist")
            continue
        songs.append(Song(title=title.get_text(strip=True), artist=artist.get_text(strip=True)))
    if not songs:
        raise ChartParseError("No songs found on the chart page")
    return songs


def fetch_page(url: str) -> str:
    """@brief Download a page over HTTP.

    @param url Address of the page.
    @return The page markup.
    @throws requests.RequestException when the request fails or answers with an HTTP error.
    """
    response = requests.get(url, headers=REQUEST_HEADERS, timeout=REQUEST_TIMEOUT_SECONDS)
    response.raise_for_status()
    return response.text


class BakeboardChartSource:
    """@brief ChartSource that scrapes the Bakeboard site."""

    def __init__(self, fetch: Callable[[str], str] = fetch_page) -> None:
        """@brief Create the source.

        @param fetch Function that downloads a URL; replaced in tests.
        """
        self._fetch = fetch

    def songs_for(self, chart_date: date) -> list[Song]:
        """@brief Get the songs of the chart of a date.

        @param chart_date Date of the chart.
        @return The songs in chart order.
        @throws ChartUnavailableError when the page cannot be fetched.
        @throws ChartParseError when the page holds no songs.
        """
        stamp = chart_date.strftime(DATE_FORMAT)
        try:
            html = self._fetch(f"{BASE_URL}{stamp}/")
        except requests.RequestException as error:
            raise ChartUnavailableError(CHART_UNAVAILABLE_MESSAGE.format(reason=error)) from error
        try:
            return parse_chart(html)
        except ChartParseError as error:
            raise ChartParseError(CHART_PARSE_MESSAGE.format(date=stamp)) from error
