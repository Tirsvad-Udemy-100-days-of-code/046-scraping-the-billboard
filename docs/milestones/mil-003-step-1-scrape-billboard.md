# Milestone 3: Step 1 - Scrape the Billboard Hot 100

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [MIL-002] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [01e016e] |

---

## Purpose

Decide that lecture step 1 works: a date goes in and a list of 100 songs comes out.

## Deliverable

A command that asks for a date in YYYY-MM-DD format, fetches the Bakeboard page with a User-Agent header, and prints the song titles and artists, with tests and a step 1 screenshot.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The scraper test returns 100 songs from a stored copy of the 2026-04-18 page | 100 titles and 100 artists | Any other count |
| 2 | An invalid date format is rejected with a clear message | Test passes | Test fails |
| 3 | A live run for 2026-04-18 prints 100 titles | 100 lines in the screenshot | Fewer lines |
| 4 | The step 1 screenshot is in README and wiki sources | File exists and is referenced | Missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | Its pull request is merged before this milestone starts |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] O1; success criterion 1 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (the AI acts as stand-in) |

## Target Date

2026-11-12 — inside the Business Case window 2026-10-28 to 2026-11-30; branch `mil-003-step-1-scrape-billboard`.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Prompt for and validate the date | Add the date prompt and a validator for YYYY-MM-DD that returns a `datetime.date` or raises a domain error, so the rest of the program only sees valid dates. | No | BC-001 O1 |
| 2 | Implement scrape_titles | Implement `scrape_titles` (and artist extraction) with `requests` and `BeautifulSoup`, with the User-Agent header from `constants.py`, raising a clear error when no song is found. Keep the HTTP fetch behind a port so tests do not use the network. | No | BC-001 O1 |
| 3 | Store a Bakeboard fixture page and test the scraper | Save a copy of the 2026-04-18 chart page under `tests/fixtures/` and write tests for the 100 songs result, the empty-page error and the date validation. | No | BC-001 O1 |
| 4 | Capture the step 1 screenshot | Run the program for 2026-04-18 in a terminal and capture a screenshot of the Bakeboard page and of the printed list; check that it shows no personal data. A GUI is not tested; the screenshot is taken from a terminal run. | No | BC-001 O5 |
| 5 | Document step 1 in README | Add the step 1 section with the screenshot and the command to run it. | No | BC-001 O5 |
| 6 | Open the step 1 pull request | Commit on branch `mil-003-step-1-scrape-billboard`, review against `qc-programming-python`, push and open the pull request that closes this milestone's issues. | No | BC-001 |

---

[BC-001]: ../business-case.md
[MIL-002]: ./mil-002-project-scaffold.md
[01e016e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/commit/01e016e15dd93cface4f4ae9e9e99919e0aace2b
