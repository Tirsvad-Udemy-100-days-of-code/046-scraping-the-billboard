# Milestone 1: Planning baseline

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [01e016e] |

---

## Purpose

Decide that the planning baseline (Business Case, Stakeholder Analysis, Project Plan, milestones, governance, traceability) is complete and reviewed, so that code may be planned.

## Deliverable

Accepted `BC-001`, `SA-001`, `PP-001`, all `MIL-*`, `GOV-001` and `TM-001`, each with a `Go` review record, and a repository on the git host with description and topics.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `BC-001`, `SA-001` and `MIL-001` to `MIL-007` have a review record and are `Accepted` | All rows `Accepted` | Any row `Proposed` or `Rejected` |
| 2 | `PP-001` is `Accepted` | Row `Accepted` | Row `Proposed` |
| 3 | The repository description and at least 5 topics are set on the git host | API response shows both | Either is empty |
| 4 | `bash framework/scripts/check-plan.sh` and `check-languages.sh` report no finding | Exit code 0 | Exit code not 0 |

## Dependencies

| Depends on | Reason |
| --- | --- |
| none | First milestone |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] O6; success criteria 6 and 7 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (the AI acts as stand-in) |

## Target Date

2026-11-02 — inside the Business Case window 2026-10-28 to 2026-11-30; branch `mil-001-planning-baseline`.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write governance and traceability matrix | Create `GOV-001` (RACI with S01 as the only approver, AI as recorded stand-in) and `TM-001` linking each stakeholder concern to its milestone, so the review records have an escalation path and a matrix to update. | No | BC-001 |
| 2 | Review baseline artifacts | Review `BC-001`, `SA-001`, `PP-001` and the milestones against their QC checklists and `QC-LANG-001`, write the `RC-*` records and set the rows `Accepted` on a `Go`. Language criteria 3, 5 and 9 need S01 to confirm them. | No | BC-001 |
| 3 | Set repository description and topics | Set the description and topics (python, web-scraping, beautifulsoup, ytmusicapi, youtube-music, billboard, udemy, 100-days-of-code) through the git host API with the token from `.env`. The token is only used from the shell and is never stored in the project. | No | BC-001 O6 |
| 4 | Open the baseline pull request | Commit on branch `mil-001-planning-baseline`, resolve the pending commit links, push and open the pull request that closes this milestone's issues. | No | BC-001 |

---

[BC-001]: ../business-case.md
[01e016e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/commit/01e016e15dd93cface4f4ae9e9e99919e0aace2b
