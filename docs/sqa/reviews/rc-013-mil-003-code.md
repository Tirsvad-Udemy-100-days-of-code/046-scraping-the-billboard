# Review of the code of MIL-003

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [MIL-003], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [2cb7e16] |

---

## Artifact Under Review

- Instance reviewed: [MIL-003] (the code of its pull request, `src/` and `tests/`)
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | snake_case modules and functions, PascalCase classes (Song, BakeboardChartSource), UPPER_SNAKE constants. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (parse_chart_date, ChartUnavailableError). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | ruff format and ruff check report no finding. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function is annotated including -> None; ruff does not flag it and the code was read. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare except; requests errors are translated with raise ... from. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; no shadowed builtins (the CLI parameter `read`/`write` do not shadow builtins). |
| 7 | Files, locks and connections are managed with context managers | N-A | No files or connections are opened by the code; requests.get is a one-shot call. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Doxygen comments on all public items; doxygen has 0 warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | logging is used for the skipped-row warning; user-facing output goes through the injected writer; nothing secret is logged. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists; all tasks are technical (BC-001 scope); the layers follow the clean-architecture skill. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 31 tests, 96 % coverage, no network: a stored page and fake sources; names state the behaviour. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | No Any in the source. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | requests and beautifulsoup4 are used by infrastructure; ytmusicapi is used from MIL-004 (declared now by the accepted plan). |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Selectors, messages and the date format are defined once in constants.py; the date is parsed in one function. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | domain imports nothing; application imports domain; infrastructure imports application and domain; presentation is the composition root. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | ChartSource is a narrow Protocol; the CLI depends on it, the Bakeboard source is injected. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | src layers and tests/unit/<layer> plus tests/integration exist. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | File names are English snake_case. |

## Overall Verdict

Go — every Mandatory criterion passes or does not apply; no blocking finding.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[MIL-003]: ../../milestones/mil-003-step-1-scrape-billboard.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[2cb7e16]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/commit/2cb7e1679843ef1cd17fb612048162f661684417
