"""@file
@brief Command line entry point and composition root.
"""

from collections.abc import Callable

from musical_time_machine.application.ports import ChartSource
from musical_time_machine.application.use_cases import scrape_songs
from musical_time_machine.constants import DATE_PROMPT, EXIT_FAILURE, EXIT_OK, SONG_LINE_TEMPLATE
from musical_time_machine.domain.chart_date import parse_chart_date
from musical_time_machine.domain.errors import MusicalTimeMachineError
from musical_time_machine.infrastructure.bakeboard import BakeboardChartSource


def main(
    argv: list[str] | None = None,
    *,
    source: ChartSource | None = None,
    read: Callable[[str], str] = input,
    write: Callable[[str], None] = print,
) -> int:
    """@brief Ask for a date and print the songs of that chart.

    @param argv Command line arguments; unused, kept for the entry point contract.
    @param source Chart source; the Bakeboard site when omitted.
    @param read Function that prompts and returns the user's answer.
    @param write Function that shows one line to the user.
    @return Process exit code: 0 on success, 1 when a domain error stopped the run.
    """
    del argv
    chart_source = source if source is not None else BakeboardChartSource()
    try:
        chart_date = parse_chart_date(read(DATE_PROMPT))
        songs = scrape_songs(chart_date, chart_source)
    except MusicalTimeMachineError as error:
        write(str(error))
        return EXIT_FAILURE
    for position, song in enumerate(songs, start=1):
        write(SONG_LINE_TEMPLATE.format(position=position, title=song.title, artist=song.artist))
    return EXIT_OK
