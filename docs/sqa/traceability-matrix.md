# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [GOV-001], [MIL-008] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [01e016e] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added the rows of MIL-008 and its review records RC-018 to RC-021, set the domain of the changed documents to education and added the missing link definition of TM-001; reviewed in autonomous mode, not independent | pending |

---

## Purpose

Tracks backward and forward links between artifact instances so that the traceability of concerns to milestones is measurable. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [SA-001] | SA | en | it | - | [BC-001] | [RC-002] |
| [BC-001] | BC | en | education | [SA-001] | [PP-001], [MIL-001], [MIL-008] | [RC-018], [RC-001] |
| [PP-001] | PP | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-008] | [RC-019], [RC-003] |
| [GOV-001] | GOV | en | it | [BC-001], [SA-001] | [TM-001] | [RC-004] |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | [MIL-002] | [RC-005] |
| [MIL-002] | MIL | en | it | [MIL-001] | [MIL-003] | [RC-006], [RC-012] |
| [MIL-003] | MIL | en | it | [MIL-002] | [MIL-004] | [RC-007], [RC-013] |
| [MIL-004] | MIL | en | it | [MIL-003] | [MIL-005] | [RC-008], [RC-014] |
| [MIL-005] | MIL | en | it | [MIL-004] | [MIL-006] | [RC-009], [RC-015] |
| [MIL-006] | MIL | en | it | [MIL-005] | [MIL-007] | [RC-010], [RC-016] |
| [MIL-007] | MIL | en | it | [MIL-006] | [MIL-008] | [RC-011], [RC-017] |
| [MIL-008] | MIL | en | education | [BC-001], [PP-001], [MIL-007] | - | [RC-020] |
| [TM-001] | TM | - | - | [BC-001] | - | - |
| Wiki | Wiki | en, da, ms | education | [BC-001], [MIL-008] | - | [RC-021] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-003], [MIL-004], [MIL-005], [MIL-006] | - | - | Covered |
| CN-002 | [MIL-002] (ignore rules), [MIL-004], [MIL-008] (criterion 6) | - | - | Covered |
| CN-003 | [MIL-003], [MIL-006] | - | - | Covered |
| CN-004 | [MIL-002], [MIL-004], [MIL-008] (criterion 4) | - | - | Covered |
| CN-005 | [MIL-001], [MIL-008] (criterion 3) | - | - | Covered |
| CN-006 | [MIL-002], [MIL-008] (criterion 2) | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| 1 | [BC-001], [PP-001] | None found | [RC-001] | Closed | - |

## Coverage Notes

- No design artifacts (use cases, domain model, DCD, ERD, test plan) exist: all tasks are technical tasks; `-` in Upstream means foundational, in Downstream that nothing is built on it yet, in Last Reviewed that no `RC-*` exists yet.
- Concern coverage will be rechecked when code exists (MIL-003 to MIL-007).
- The domain of [BC-001], [PP-001], [MIL-008] and the wiki is `education` since [MIL-008]. The other documents keep the domain `it` they were accepted with; a change of their domain would need a new review of each (see the Open Issues of [PP-001]).
- [MIL-008] changes no source or test file. The wiki (`docs/wiki/`) is documentation, not an artifact with an ID or a Language and Domain row; it has its own review record, [RC-021].
- The wiki workflow reviewed in [RC-017] was removed in an earlier change; the wiki is published by the shared scoped workflow (see the Open Issues of [PP-001]).

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[GOV-001]: ./governance.md
[TM-001]: ./traceability-matrix.md
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
[RC-015]: ./reviews/rc-015-mil-005-code.md
[RC-016]: ./reviews/rc-016-mil-006-code.md
[RC-017]: ./reviews/rc-017-mil-007-workflow.md
[MIL-008]: ../milestones/mil-008-framework-baseline.md
[RC-018]: ./reviews/rc-018-business-case-baseline.md
[RC-019]: ./reviews/rc-019-project-plan-baseline.md
[RC-020]: ./reviews/rc-020-milestone-008.md
[RC-021]: ./reviews/rc-021-wiki.md
