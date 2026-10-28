"""@file
@brief Tests of the command line with a fake source and injected input and output.
"""

from conftest import FakeChartSource

from musical_time_machine.constants import CHART_SIZE, DATE_PROMPT
from musical_time_machine.domain.errors import ChartParseError, ChartUnavailableError
from musical_time_machine.domain.song import Song
from musical_time_machine.presentation.cli import main


def _run(answer: str, source: FakeChartSource) -> tuple[int, list[str], list[str]]:
    prompts: list[str] = []
    lines: list[str] = []

    def read(prompt: str) -> str:
        prompts.append(prompt)
        return answer

    code = main([], source=source, read=read, write=lines.append)
    return code, lines, prompts


def test_main_prints_numbered_songs_and_returns_zero() -> None:
    songs = [Song(f"Title {n}", f"Artist {n}") for n in range(1, CHART_SIZE + 1)]

    code, lines, prompts = _run("2026-04-18", FakeChartSource(songs))

    assert code == 0
    assert prompts == [DATE_PROMPT]
    assert len(lines) == CHART_SIZE
    assert lines[0] == "1. Title 1 - Artist 1"
    assert lines[-1] == "100. Title 100 - Artist 100"


def test_main_returns_one_with_message_for_invalid_date() -> None:
    source = FakeChartSource([Song("x", "y")])

    code, lines, _ = _run("18/04/2026", source)

    assert code == 1
    assert len(lines) == 1
    assert "YYYY-MM-DD" in lines[0]
    assert source.requested == []


def test_main_returns_one_when_chart_unavailable() -> None:
    code, lines, _ = _run("2026-04-18", FakeChartSource(error=ChartUnavailableError("404")))

    assert code == 1
    assert lines == ["404"]


def test_main_returns_one_when_chart_has_no_songs() -> None:
    code, lines, _ = _run("2026-04-18", FakeChartSource(error=ChartParseError("empty")))

    assert code == 1
    assert lines == ["empty"]
