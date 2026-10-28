# Milestone 2: Project scaffold

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [MIL-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide that the repository can be installed, tested and documented by a participant who has never seen it.

## Deliverable

A project skeleton with `pyproject.toml`, `.gitignore`, `constants.py`, `Doxyfile`, a passing smoke test, and a `README.md` from the framework template with `.venv` instructions.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m venv .venv`, `python -m pip install --upgrade pip` and `python -m pip install -e .[dev]` succeed on Python 3.13 | All three succeed | Any fails |
| 2 | `python -m pytest` passes | Exit code 0 | Failures |
| 3 | `bash framework/scripts/check-readme.sh` reports no finding | Exit code 0 | Findings |
| 4 | `.env` and `browser.json` are ignored by git | `git check-ignore` lists both | Either is tracked |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | Its pull request is merged before this milestone starts |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] O5; success criteria 2 and 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (the AI acts as stand-in) |

## Target Date

2026-11-06 — inside the Business Case window 2026-10-28 to 2026-11-30; branch `mil-002-project-scaffold`.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create pyproject and package layout | Add `pyproject.toml` (Python 3.13 or later, runtime dependencies `requests`, `beautifulsoup4`, `ytmusicapi`, optional `dev` extra with pytest) and the `src/` layers `domain`, `application`, `infrastructure`, `presentation` and `tests/` folders, following the framework's Python layout. | No | BC-001 O5 |
| 2 | Add constants module | Create `constants.py` holding the Bakeboard base URL, the CSS selectors, the User-Agent header, the playlist name pattern, the `browser.json` file name and the search filter, so no magic value is in the code. | No | BC-001 O1 |
| 3 | Add Python .gitignore and secret rules | Keep the Python `.gitignore` and ensure `.env`, `browser.json`, `.venv/` and Doxygen output are ignored. | No | BC-001 O5 |
| 4 | Add Doxyfile | Add a `Doxyfile` that documents `src/` from the Doxygen comments, with output to an ignored folder. | No | BC-001 O5 |
| 5 | Write README from the framework template | Write `README.md` from `framework/templates/README-template.md`: create and use `.venv`, `python -m pip install --upgrade pip`, run, test, and the reason for each dependency. | No | BC-001 O5 |
| 6 | Add smoke test and pytest configuration | Add the pytest configuration in `pyproject.toml` and one smoke test that imports the package, so the test command is proven before real code arrives. | No | BC-001 O5 |
| 7 | Open the scaffold pull request | Commit on branch `mil-002-project-scaffold`, run the code review against `qc-programming-python`, push and open the pull request that closes this milestone's issues. | No | BC-001 |

---

[BC-001]: ../business-case.md
[MIL-001]: ./mil-001-planning-baseline.md
