# Milestone 5: Step 3 - Create the playlist

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [MIL-004] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [01e016e] |

---

## Purpose

Decide that lecture step 3 works: a private playlist named `{date} Billboard 100` is created once and never duplicated.

## Deliverable

A `create_playlist` use case that returns the id of an existing or new private playlist, with tests and a step 3 screenshot.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | A first call creates one private playlist with the name `2026-04-18 Billboard 100` | Fake client holds one playlist | Zero or two |
| 2 | A second call with the same date creates no new playlist | Fake client still holds one | Two playlists |
| 3 | A live run shows the playlist in YouTube Music | Screenshot shows the playlist | Missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-004] | Its pull request is merged before this milestone starts |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] O3; success criterion 3 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (the AI acts as stand-in) |

## Target Date

2026-11-20 — inside the Business Case window 2026-10-28 to 2026-11-30; branch `mil-005-step-3-create-playlist`.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Build the playlist name and description | Build the name from the date with the constant pattern and write a short description that says the playlist was created by this program. | No | BC-001 O3 |
| 2 | Implement create_playlist without duplicates | Implement `create_playlist` with `create_playlist(title, description, privacy_status='PRIVATE')`; it first loops over `get_library_playlists()` and returns the id of a playlist with the same title. | No | BC-001 O3 |
| 3 | Test the duplicate rule | Write tests with the fake client for the first call, the second call and a different date. | No | BC-001 O3 |
| 4 | Capture the step 3 screenshot | Needs S01's `browser.json`. Run the program and capture the new playlist in the YouTube Music library; if the file is missing the run stops and reports it. | No | BC-001 O5 |
| 5 | Document step 3 in README | Add the step 3 section with the screenshot. | No | BC-001 O5 |
| 6 | Open the step 3 pull request | Commit on branch `mil-005-step-3-create-playlist`, review against `qc-programming-python`, push and open the pull request that closes this milestone's issues. | No | BC-001 |

---

[BC-001]: ../business-case.md
[MIL-004]: ./mil-004-step-2-youtube-music-auth.md
[01e016e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/commit/01e016e15dd93cface4f4ae9e9e99919e0aace2b
