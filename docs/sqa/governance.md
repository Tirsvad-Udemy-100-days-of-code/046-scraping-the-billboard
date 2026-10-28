# Governance / ARB Workflow

## Metadata
| Key | Value |
| --- | --- |
| ID | GOV-001 |
| CrossReference | [BC-001], [SA-001], [TM-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [01e016e] |

---

## Purpose

Defines how this project applies Quality Criteria (QC) checklists to its artifact instances, producing SQA Review Records and Go/No-Go decisions. It serves the Business Case ([BC-001]) objective O5 (documentation) and success criterion 6, and the stakeholder concern CN-002 of [SA-001] that nothing unreviewed or secret reaches the repository.

## ARB Review Workflow

1. **Submission** — the artifact owner (S01) submits an instance for review, identifying its type's QC checklist (`framework/qc/*/qc-*.md`).
2. **QC Checklist Review** — the Responsible reviewer (S01, or the AI as stand-in for S01 in autonomous mode) applies the checklist criterion by criterion.
3. **Review Record** — the Responsible reviewer documents the outcome as an SQA Review Record (`RC-*` under `docs/sqa/reviews/`).
4. **Go/No-Go Decision** — the Accountable role for the artifact category (S01) decides; contested or cross-cutting cases escalate to the ARB Chair (S01).
5. **Sign-off** — S01 signs off. On **Go**, the artifact's `## Version History` gets an `Accepted` row (the previous row becomes `Deprecated`). On **Go-with-conditions**, status stays `Proposed` until the Action Items are closed. On **No-Go**, the artifact returns to its owner (S01). A blocking finding (a `Fail` on a Mandatory criterion, or an open security finding rated High or Critical) always gives **No-Go**, unless a valid risk exception covers it.
6. **Traceability Update** — S01 (or the stand-in) updates the Traceability Matrix ([TM-001]) with the instance and its `RC-*` reference.

A criterion that only a person can confirm stays `Pending` until S01 confirms it by name and date; the author's or a stand-in's own assessment never closes it, and `Pending` allows `Go-with-conditions` at most. A risk exception names the finding, an owner, an approver who is neither the author nor the owner, an expiry date and the compensating controls; an expired exception blocks again. This project has one person, so a risk exception is approved by S01 in chat only, never by the stand-in.

## RACI by Artifact Category

| Artifact Category | Responsible (runs the review) | Accountable (Go/No-Go owner) | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Strategic (Stakeholder Analysis, Business Case) | S01 | S01 | S02 | S03 |
| Process/Business (Project Plan, Milestones/Gateways) | S01 | S01 | S02 | S03 |
| Governance and traceability (Governance, Traceability Matrix) | S01 | S01 | S02 | S03 |
| Source code and tests | S01 | S01 | S02 | S03 |

Cross-cutting escalations and disputed verdicts are Accountable to the ARB Chair (S01), overriding the category-level Accountable role. Requirements and modeling artifacts (use cases, domain model and similar) are not in scope: all tasks are technical tasks (see [BC-001], Scope).

## Escalation Rules

- A **No-Go** verdict, or any disagreement between the Responsible reviewer and the category's Accountable owner, escalates to the ARB Chair (S01).
- A reviewer may not review an instance they authored. The one exception is autonomous mode: the AI may act as stand-in for a reviewer or an Accountable role, recorded as `AI as stand-in for S01` and `Mode: autonomous, not independent`; S01's acceptance of the plan is the authorisation for it. The named alternate for a review that S01 authored is S01 reading it again in the run summary.
- Repeated No-Go verdicts (2 or more) on the same artifact type trigger a review of the corresponding `QC-*` checklist itself.

## Cadence

- Reviews are triggered per artifact instance as it is produced or revised.
- QC checklists are reviewed annually (framework level, outside this project).

Process artifacts relied on: [TM-001] (traceability) and `framework/process/review-checklist-process.md` (review procedure).

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[TM-001]: ./traceability-matrix.md
[01e016e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/commit/01e016e15dd93cface4f4ae9e9e99919e0aace2b
