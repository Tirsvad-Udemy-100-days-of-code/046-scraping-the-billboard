# Milestone 4: Step 2 - YouTube Music authentication

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [MIL-003] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide that lecture step 2 works: the program can open a YouTube Music session from `browser.json` and reports the library playlists.

## Deliverable

A client adapter around `ytmusicapi` that reads `browser.json`, lists the library playlists and prints the count, a fake client for tests, instructions to create `browser.json`, and a step 2 screenshot.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The adapter test with a fake client prints `Found N playlists in your library.` | Message matches | Mismatch |
| 2 | A missing `browser.json` gives a clear message with the setup steps | Test passes | Test fails |
| 3 | A live run with S01's `browser.json` prints the playlist count | Screenshot shows the count | Error or no screenshot |
| 4 | `browser.json` is not tracked by git | `git ls-files` does not list it | Listed |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] | Its pull request is merged before this milestone starts |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] O2 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (the AI acts as stand-in) |

## Target Date

2026-11-17 — inside the Business Case window 2026-10-28 to 2026-11-30; branch `mil-004-step-2-youtube-music-auth`.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Define the music service port and fake | Define the port (an interface) for library playlists, playlist creation, search and add, and a fake implementation for tests, so no test needs the network or an account. | No | BC-001 O2 |
| 2 | Implement the ytmusicapi adapter | Implement the adapter in the infrastructure layer: `YTMusic('browser.json')`, `get_library_playlists()` and the playlist count message from the lecture. | No | BC-001 O2 |
| 3 | Handle a missing or expired browser.json | Detect a missing or rejected `browser.json` and print the steps to renew it (Firefox, Network tab, `ytmusicapi browser`) instead of a stack trace. | No | BC-001 O2 |
| 4 | Document browser.json setup | Write the Firefox header-copy steps for Windows, Linux and macOS (on macOS the `pbpaste` command feeds `ytmusicapi browser`) and the troubleshooting list from the lecture into the README. The file holds personal cookies and is never committed. | No | BC-001 O2 |
| 5 | Capture the step 2 screenshot | Needs S01's `browser.json`. Run the verify command and capture the terminal output; the playlist names must not show. If the file is missing the run stops and reports it. | No | BC-001 O5 |
| 6 | Open the step 2 pull request | Commit on branch `mil-004-step-2-youtube-music-auth`, review against `qc-programming-python`, push and open the pull request that closes this milestone's issues. | No | BC-001 |

---

[BC-001]: ../business-case.md
[MIL-003]: ./mil-003-step-1-scrape-billboard.md
