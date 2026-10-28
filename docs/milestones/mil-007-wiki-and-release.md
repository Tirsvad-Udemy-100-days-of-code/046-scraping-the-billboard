# Milestone 7: Wiki and release

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-007 |
| CrossReference | [BC-001], [MIL-006] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [01e016e] |

---

## Purpose

Decide that the project is finished: the wiki explains what was learned in each lecture step in three languages and the repository is ready to share.

## Deliverable

Wiki pages in `docs/wiki/` in English, Danish and Bahasa Malaysia with the four step screenshots, the publish workflow, the Doxygen build, and a final run summary.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Every English wiki page has a `-da` and a `-ms` page | Same page set in all three | Page missing |
| 2 | Each language has the four step screenshots and a what-we-learned section per step | 4 images and 4 sections each | Any missing |
| 3 | `_Sidebar.md` lists all three languages | Present | Absent |
| 4 | `doxygen Doxyfile` runs without warnings | 0 warnings | Warnings |
| 5 | The full test suite passes | Exit code 0 | Failures |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-006] | Its pull request is merged before this milestone starts |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] O5; success criterion 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (the AI acts as stand-in) |

## Target Date

2026-11-30 — inside the Business Case window 2026-10-28 to 2026-11-30; branch `mil-007-wiki-and-release`.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the English wiki | Write `Home`, one page per lecture step (what the step teaches: HTTP headers and parsing, cookie authentication, idempotent creation, error tolerant loops) and `_Sidebar` in `docs/wiki/`, in English as the authoritative text. | No | BC-001 O5 |
| 2 | Translate the wiki to Danish | Write every page again as `<Page>-da.md` with the language line and the same page set; code, commands and file names stay in English. | No | BC-001 O5 |
| 3 | Translate the wiki to Bahasa Malaysia | Write every page again as `<Page>-ms.md` with the language line and the same page set; code, commands and file names stay in English. | No | BC-001 O5 |
| 4 | Add step screenshots to the wiki and README | Copy the four step screenshots to `docs/wiki/images/` and reference them from README and from each language of the wiki. | No | BC-001 O5 |
| 5 | Install the wiki publish workflow | Copy `framework/templates/ci/publish-wiki.yml` to the CI folder of the host so the wiki is published on merge. | No | BC-001 O5 |
| 6 | Run Doxygen and the full check | Run `doxygen Doxyfile`, the full pytest suite and the framework check scripts, and fix findings. | No | BC-001 O5 |
| 7 | Open the release pull request and write the run summary | Commit on branch `mil-007-wiki-and-release`, push and open the pull request; give S01 the summary of merged pull requests, review records and stand-in decisions. | No | BC-001 |

---

[BC-001]: ../business-case.md
[MIL-006]: ./mil-006-step-4-search-and-add-songs.md
[01e016e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/commit/01e016e15dd93cface4f4ae9e9e99919e0aace2b
