"""@file
@brief Tests of the command line with a fake source and injected input and output.
"""

from pathlib import Path

from conftest import FakeChartSource, FakeMusicService

from musical_time_machine.constants import CHART_SIZE, DATE_PROMPT
from musical_time_machine.domain.errors import (
    BrowserFileMissingError,
    ChartParseError,
    ChartUnavailableError,
    PlaylistCreationError,
)
from musical_time_machine.domain.playlist import Playlist
from musical_time_machine.domain.song import Song
from musical_time_machine.presentation.cli import main


def _run(answer: str, source: FakeChartSource) -> tuple[int, list[str], list[str]]:
    prompts: list[str] = []
    lines: list[str] = []

    def read(prompt: str) -> str:
        prompts.append(prompt)
        return answer

    code = main(["--list-only"], source=source, read=read, write=lines.append)
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


def test_main_check_login_prints_playlist_count() -> None:
    lines: list[str] = []
    service = FakeMusicService([Playlist("a", "A"), Playlist("b", "B"), Playlist("c", "C")])

    code = main(["--check-login"], music_service=service, write=lines.append)

    assert code == 0
    assert lines == ["Found 3 playlists in your library."]


def test_main_check_login_returns_one_when_browser_file_missing() -> None:
    lines: list[str] = []
    service = FakeMusicService(error=BrowserFileMissingError("browser.json was not found."))

    code = main(["--check-login"], music_service=service, write=lines.append)

    assert code == 1
    assert lines == ["browser.json was not found."]


def test_main_check_login_with_missing_real_file_returns_one(tmp_path: Path) -> None:
    lines: list[str] = []
    argv = ["--check-login", "--browser-file", str(tmp_path / "none.json")]

    code = main(argv, write=lines.append)

    assert code == 1
    assert "ytmusicapi browser" in lines[0]


def test_main_list_only_does_not_use_the_music_service() -> None:
    lines: list[str] = []
    service = FakeMusicService(error=BrowserFileMissingError("must not be called"))

    code = main(
        ["--list-only"],
        source=FakeChartSource([Song("T", "A")]),
        music_service=service,
        read=lambda _prompt: "2026-04-18",
        write=lines.append,
    )

    assert code == 0
    assert lines == ["1. T - A"]


def _create(answer: str, service: FakeMusicService) -> tuple[int, list[str]]:
    lines: list[str] = []
    code = main(
        ["--create-playlist"],
        music_service=service,
        read=lambda _prompt: answer,
        write=lines.append,
    )
    return code, lines


def test_main_create_playlist_reports_creation() -> None:
    service = FakeMusicService()

    code, lines = _create("2026-04-18", service)

    assert code == 0
    assert lines == ['Created playlist "2026-04-18 Billboard 100".']
    assert len(service.created) == 1


def test_main_create_playlist_reports_existing_playlist() -> None:
    service = FakeMusicService([Playlist("a", "2026-04-18 Billboard 100")])

    code, lines = _create("2026-04-18", service)

    assert code == 0
    assert lines == ['Playlist "2026-04-18 Billboard 100" already exists; nothing was created.']
    assert service.created == []


def test_main_create_playlist_returns_one_for_invalid_date() -> None:
    service = FakeMusicService()

    code, lines = _create("nope", service)

    assert code == 1
    assert "YYYY-MM-DD" in lines[0]
    assert service.created == []


def test_main_create_playlist_returns_one_on_domain_error() -> None:
    code, lines = _create("2026-04-18", FakeMusicService(error=PlaylistCreationError("failed")))

    assert code == 1
    assert lines == ["failed"]


def _full(
    source: FakeChartSource, service: FakeMusicService, answer: str = "2026-04-18"
) -> tuple[int, list[str], list[float]]:
    lines: list[str] = []
    pauses: list[float] = []
    code = main(
        [],
        source=source,
        music_service=service,
        read=lambda _prompt: answer,
        write=lines.append,
        pause=pauses.append,
    )
    return code, lines, pauses


def test_main_full_run_adds_songs_and_prints_summary_with_skipped() -> None:
    source = FakeChartSource([Song("One", "A"), Song("Two", "B"), Song("Three", "C")])
    service = FakeMusicService(video_ids={"One": "v1", "Three": "v3"})

    code, lines, pauses = _full(source, service)

    assert code == 0
    assert lines == [
        'Added 2 of 3 songs to "2026-04-18 Billboard 100"; skipped 1.',
        "Skipped: Two - B",
    ]
    assert len(service.created) == 1
    assert len(pauses) == 2


def test_main_full_run_without_skips_prints_only_summary() -> None:
    code, lines, _ = _full(FakeChartSource([Song("One", "A")]), FakeMusicService())

    assert code == 0
    assert lines == ['Added 1 of 1 songs to "2026-04-18 Billboard 100"; skipped 0.']


def test_main_full_run_returns_one_for_invalid_date() -> None:
    code, lines, _ = _full(FakeChartSource([Song("x", "y")]), FakeMusicService(), "nope")

    assert code == 1
    assert "YYYY-MM-DD" in lines[0]


def test_main_full_run_returns_one_on_login_error() -> None:
    service = FakeMusicService(error=BrowserFileMissingError("browser.json was not found."))

    code, lines, _ = _full(FakeChartSource([Song("x", "y")]), service)

    assert code == 1
    assert lines == ["browser.json was not found."]
