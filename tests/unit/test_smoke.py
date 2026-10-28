"""@file
@brief Smoke test: the package imports and its constants are sane.
"""

import musical_time_machine
from musical_time_machine import constants


def test_package_imports() -> None:
    """@brief The package and its layers can be imported."""
    from musical_time_machine import application, domain, infrastructure, presentation

    assert all(
        m is not None
        for m in (musical_time_machine, domain, application, infrastructure, presentation)
    )


def test_chart_size_is_one_hundred() -> None:
    """@brief The Hot 100 has 100 entries."""
    assert constants.CHART_SIZE == 100


def test_playlist_name_template_formats_date() -> None:
    """@brief The playlist name template accepts a chart date."""
    assert constants.PLAYLIST_NAME_TEMPLATE.format(date="2026-04-18") == "2026-04-18 Billboard 100"
