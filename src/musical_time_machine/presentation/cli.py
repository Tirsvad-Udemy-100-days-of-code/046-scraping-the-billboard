"""@file
@brief Command line entry point and composition root.
"""

import argparse
from collections.abc import Callable
from pathlib import Path

from musical_time_machine.application.ports import ChartSource, MusicService
from musical_time_machine.application.use_cases import count_library_playlists, scrape_songs
from musical_time_machine.constants import (
    BROWSER_FILE_FLAG,
    BROWSER_FILE_HELP,
    BROWSER_FILE_NAME,
    CHECK_LOGIN_FLAG,
    CHECK_LOGIN_HELP,
    DATE_PROMPT,
    EXIT_FAILURE,
    EXIT_OK,
    PLAYLIST_COUNT_MESSAGE,
    SONG_LINE_TEMPLATE,
)
from musical_time_machine.domain.chart_date import parse_chart_date
from musical_time_machine.domain.errors import MusicalTimeMachineError
from musical_time_machine.infrastructure.bakeboard import BakeboardChartSource
from musical_time_machine.infrastructure.ytmusic import YouTubeMusicService


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="musical_time_machine")
    parser.add_argument(CHECK_LOGIN_FLAG, action="store_true", help=CHECK_LOGIN_HELP)
    parser.add_argument(
        BROWSER_FILE_FLAG, type=Path, default=Path(BROWSER_FILE_NAME), help=BROWSER_FILE_HELP
    )
    return parser.parse_args(argv)


def _check_login(service: MusicService, write: Callable[[str], None]) -> int:
    try:
        count = count_library_playlists(service)
    except MusicalTimeMachineError as error:
        write(str(error))
        return EXIT_FAILURE
    write(PLAYLIST_COUNT_MESSAGE.format(count=count))
    return EXIT_OK


def main(
    argv: list[str] | None = None,
    *,
    source: ChartSource | None = None,
    music_service: MusicService | None = None,
    read: Callable[[str], str] = input,
    write: Callable[[str], None] = print,
) -> int:
    """@brief Ask for a date and print the songs of that chart, or check the YouTube Music login.

    @param argv Command line arguments: `--check-login` and `--browser-file PATH`.
    @param source Chart source; the Bakeboard site when omitted.
    @param music_service Music service for `--check-login`; YouTube Music when omitted.
    @param read Function that prompts and returns the user's answer.
    @param write Function that shows one line to the user.
    @return Process exit code: 0 on success, 1 when a domain error stopped the run.
    """
    args = _parse_args(argv)
    if args.check_login:
        service = music_service or YouTubeMusicService(browser_file=args.browser_file)
        return _check_login(service, write)
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
