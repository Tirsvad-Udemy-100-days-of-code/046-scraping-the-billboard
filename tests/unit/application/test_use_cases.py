"""@file
@brief Tests of the scrape use cases with a fake chart source.
"""

from datetime import date

import pytest
from conftest import FakeChartSource

from musical_time_machine.application.use_cases import scrape_songs, scrape_titles
from musical_time_machine.domain.errors import ChartUnavailableError
from musical_time_machine.domain.song import Song

SONGS = [Song("One", "A"), Song("Two", "B")]


def test_scrape_songs_returns_source_songs_for_the_date() -> None:
    source = FakeChartSource(SONGS)

    assert scrape_songs(date(2026, 4, 18), source) == SONGS
    assert source.requested == [date(2026, 4, 18)]


def test_scrape_titles_returns_titles_in_order() -> None:
    assert scrape_titles(date(2026, 4, 18), FakeChartSource(SONGS)) == ["One", "Two"]


def test_scrape_titles_propagates_source_error() -> None:
    source = FakeChartSource(error=ChartUnavailableError("down"))

    with pytest.raises(ChartUnavailableError):
        scrape_titles(date(2026, 4, 18), source)
