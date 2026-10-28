# Milestone 6: Step 4 - Search and add songs

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001], [MIL-005] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [01e016e] |

---

## Purpose

Decide that lecture step 4 works: every found song is added to the playlist and a failure never stops the run.

## Deliverable

An `add_songs` use case that searches with the song filter and adds the top result, skips failures and reports counts, with tests and a step 4 screenshot.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The test adds the top result for each of 3 fake songs | 3 items added | Other count |
| 2 | A song whose search raises an error is skipped and the run continues | Remaining songs added; skipped count 1 | Run stops |
| 3 | A live run adds songs to the playlist | Screenshot shows the filled playlist | Missing |
| 4 | The final report shows added and skipped counts | Both counts printed | Not printed |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-005] | Its pull request is merged before this milestone starts |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] O4; success criterion 4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (the AI acts as stand-in) |

## Target Date

2026-11-25 — inside the Business Case window 2026-10-28 to 2026-11-30; branch `mil-006-step-4-search-and-add-songs`.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement song search | Implement the search with `yt.search(query, filter='songs')` using title and artist, returning the first result's `videoId` or none. | No | BC-001 O4 |
| 2 | Implement add_songs with graceful skipping | Implement `add_songs` that calls `add_playlist_items` for each found song inside a try/except, collects the skipped songs and returns the counts. Add a short pause between calls if the live run needs it. | No | BC-001 O4 |
| 3 | Test search and skipping | Write tests with the fake client for the add path, the not found path and the error path. | No | BC-001 O4 |
| 4 | Wire the full program in the composition root | Connect prompt, scrape, authenticate, create playlist and add songs in the presentation layer's entry point, with `python -m` as the run command. | No | BC-001 O1 |
| 5 | Capture the step 4 screenshot | Needs S01's `browser.json`. Run the whole program and capture the playlist with its songs; if the file is missing the run stops and reports it. | No | BC-001 O5 |
| 6 | Open the step 4 pull request | Commit on branch `mil-006-step-4-search-and-add-songs`, review against `qc-programming-python`, push and open the pull request that closes this milestone's issues. | No | BC-001 |

---

[BC-001]: ../business-case.md
[MIL-005]: ./mil-005-step-3-create-playlist.md
[01e016e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/commit/01e016e15dd93cface4f4ae9e9e99919e0aace2b
