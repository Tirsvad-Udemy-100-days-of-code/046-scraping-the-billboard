"""@file
@brief Tests of the chart date validation.
"""

from datetime import date

import pytest

from musical_time_machine.domain.chart_date import parse_chart_date
from musical_time_machine.domain.errors import InvalidChartDateError


def test_parse_chart_date_returns_date_for_valid_text() -> None:
    assert parse_chart_date("2026-04-18") == date(2026, 4, 18)


def test_parse_chart_date_accepts_leap_day_and_surrounding_whitespace() -> None:
    assert parse_chart_date(" 2024-02-29\n") == date(2024, 2, 29)


@pytest.mark.parametrize(
    "text",
    ["18-04-2026", "2026/04/18", "2026-4-8", "yesterday", "", "   "],
)
def test_parse_chart_date_rejects_bad_format(text: str) -> None:
    with pytest.raises(InvalidChartDateError):
        parse_chart_date(text)


@pytest.mark.parametrize("text", ["2026-02-30", "2025-02-29", "2026-13-01"])
def test_parse_chart_date_rejects_impossible_date(text: str) -> None:
    with pytest.raises(InvalidChartDateError):
        parse_chart_date(text)


def test_parse_chart_date_message_names_the_input_and_format() -> None:
    with pytest.raises(InvalidChartDateError, match=r"'nope'.*YYYY-MM-DD"):
        parse_chart_date("nope")
