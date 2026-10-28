"""@file
@brief Tests of the playlist naming rules.
"""

from datetime import date

from musical_time_machine.domain.playlist import playlist_description, playlist_name


def test_playlist_name_uses_iso_date_and_suffix() -> None:
    assert playlist_name(date(2026, 4, 18)) == "2026-04-18 Billboard 100"


def test_playlist_name_zero_pads_month_and_day() -> None:
    assert playlist_name(date(2026, 1, 5)) == "2026-01-05 Billboard 100"


def test_playlist_description_names_the_chart_date() -> None:
    assert "2026-04-18" in playlist_description(date(2026, 4, 18))
