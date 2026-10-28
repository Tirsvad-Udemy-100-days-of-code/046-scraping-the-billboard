"""@file
@brief Integration tests of BakeboardChartSource with an injected fetch (no network).
"""

from datetime import date

import pytest
import requests

from musical_time_machine.constants import BASE_URL, CHART_SIZE
from musical_time_machine.domain.errors import ChartParseError, ChartUnavailableError
from musical_time_machine.infrastructure.bakeboard import BakeboardChartSource


def test_songs_for_requests_dated_url_and_parses_fixture(chart_html: str) -> None:
    urls: list[str] = []

    def fetch(url: str) -> str:
        urls.append(url)
        return chart_html

    songs = BakeboardChartSource(fetch).songs_for(date(2026, 4, 18))

    assert urls == [f"{BASE_URL}2026-04-18/"]
    assert len(songs) == CHART_SIZE


def test_songs_for_maps_connection_error_to_chart_unavailable() -> None:
    def fetch(url: str) -> str:
        raise requests.ConnectionError("offline")

    with pytest.raises(ChartUnavailableError):
        BakeboardChartSource(fetch).songs_for(date(2026, 4, 18))


def test_songs_for_raises_parse_error_for_empty_page_naming_the_date() -> None:
    source = BakeboardChartSource(lambda url: "<html></html>")

    with pytest.raises(ChartParseError, match="2026-04-18"):
        source.songs_for(date(2026, 4, 18))


def test_songs_for_maps_http_error_to_chart_unavailable() -> None:
    def fetch(url: str) -> str:
        raise requests.HTTPError("404 Not Found")

    with pytest.raises(ChartUnavailableError, match="404"):
        BakeboardChartSource(fetch).songs_for(date(2026, 4, 18))
