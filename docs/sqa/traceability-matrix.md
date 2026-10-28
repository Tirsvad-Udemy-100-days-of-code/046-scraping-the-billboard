# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [GOV-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [01e016e] |

---

## Purpose

Tracks backward and forward links between artifact instances so that the traceability of concerns to milestones is measurable. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [SA-001] | SA | en | it | - | [BC-001] | [RC-002] |
| [BC-001] | BC | en | it | [SA-001] | [PP-001], [MIL-001] | [RC-001] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001] | [RC-003] |
| [GOV-001] | GOV | en | it | [BC-001], [SA-001] | [TM-001] | [RC-004] |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | [MIL-002] | [RC-005] |
| [MIL-002] | MIL | en | it | [MIL-001] | [MIL-003] | [RC-006], [RC-012] |
| [MIL-003] | MIL | en | it | [MIL-002] | [MIL-004] | [RC-007], [RC-013] |
| [MIL-004] | MIL | en | it | [MIL-003] | [MIL-005] | [RC-008], [RC-014] |
| [MIL-005] | MIL | en | it | [MIL-004] | [MIL-006] | [RC-009] |
| [MIL-006] | MIL | en | it | [MIL-005] | [MIL-007] | [RC-010] |
| [MIL-007] | MIL | en | it | [MIL-006] | - | [RC-011] |
| [TM-001] | TM | - | - | [BC-001] | - | - |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-003], [MIL-004], [MIL-005], [MIL-006] | - | - | Covered |
| CN-002 | [MIL-002] (ignore rules), [MIL-004] | - | - | Covered |
| CN-003 | [MIL-003], [MIL-006] | - | - | Covered |
| CN-004 | [MIL-002], [MIL-004] | - | - | Covered |
| CN-005 | [MIL-001] | - | - | Covered |
| CN-006 | [MIL-002] | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| 1 | [BC-001], [PP-001] | None found | [RC-001] | Closed | - |

## Coverage Notes

- No design artifacts (use cases, domain model, DCD, ERD, test plan) exist: all tasks are technical tasks; `-` in Upstream means foundational, in Downstream that nothing is built on it yet, in Last Reviewed that no `RC-*` exists yet.
- Concern coverage will be rechecked when code exists (MIL-003 to MIL-007).

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[GOV-001]: ./governance.md
[MIL-001]: ../milestones/mil-001-planning-baseline.md
[MIL-002]: ../milestones/mil-002-project-scaffold.md
[MIL-003]: ../milestones/mil-003-step-1-scrape-billboard.md
[MIL-004]: ../milestones/mil-004-step-2-youtube-music-auth.md
[MIL-005]: ../milestones/mil-005-step-3-create-playlist.md
[MIL-006]: ../milestones/mil-006-step-4-search-and-add-songs.md
[MIL-007]: ../milestones/mil-007-wiki-and-release.md
[RC-001]: ./reviews/rc-001-bc.md
[RC-002]: ./reviews/rc-002-sa.md
[RC-003]: ./reviews/rc-003-pp.md
[RC-004]: ./reviews/rc-004-gov.md
[RC-005]: ./reviews/rc-005-mil-001.md
[RC-006]: ./reviews/rc-006-mil-002.md
[RC-007]: ./reviews/rc-007-mil-003.md
[RC-008]: ./reviews/rc-008-mil-004.md
[RC-009]: ./reviews/rc-009-mil-005.md
[RC-010]: ./reviews/rc-010-mil-006.md
[RC-011]: ./reviews/rc-011-mil-007.md
[01e016e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/commit/01e016e15dd93cface4f4ae9e9e99919e0aace2b
[RC-012]: ./reviews/rc-012-mil-002-code.md
[RC-013]: ./reviews/rc-013-mil-003-code.md
[RC-014]: ./reviews/rc-014-mil-004-code.md
