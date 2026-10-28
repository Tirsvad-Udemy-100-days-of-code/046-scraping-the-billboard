"""@file
@brief Tests of the Bakeboard page parser.
"""

import pytest

from musical_time_machine.constants import CHART_SIZE
from musical_time_machine.domain.errors import ChartParseError
from musical_time_machine.infrastructure.bakeboard import parse_chart


def test_parse_chart_returns_one_hundred_songs_from_fixture(chart_html: str) -> None:
    songs = parse_chart(chart_html)

    assert len(songs) == CHART_SIZE
    assert all(song.title and song.artist for song in songs)


def test_parse_chart_strips_whitespace_and_keeps_order(chart_html: str) -> None:
    first = parse_chart(chart_html)[0]

    assert first.title == "Choosin' Texas"
    assert first.artist == "Ella Langley"


def test_parse_chart_raises_for_page_without_songs() -> None:
    with pytest.raises(ChartParseError):
        parse_chart("<html><body><p>nothing</p></body></html>")


def test_parse_chart_raises_for_empty_text() -> None:
    with pytest.raises(ChartParseError):
        parse_chart("")


def test_parse_chart_skips_row_without_artist() -> None:
    html = (
        '<div class="chart-entry"><h3 class="chart-entry__title">Lonely</h3></div>'
        '<div class="chart-entry"><h3 class="chart-entry__title"> A </h3>'
        '<span class="chart-entry__artist"> B </span></div>'
    )

    songs = parse_chart(html)

    assert [(s.title, s.artist) for s in songs] == [("A", "B")]
