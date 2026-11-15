# Review Record: PP-001 against QC-PP-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-019 |
| CrossReference | [PP-001], [QC-PP-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial review record; verdict Go (autonomous, not independent) | pending |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / education
- Language reviewer: none (the stand-in reads English and knows the education domain)
- Mode: autonomous, not independent (AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Planning Assumptions give the start date 2026-10-28, the end date 2026-11-30 and the window 2026-11-16 to 2026-11-23 of the baseline; the Business Case constraints give the one-week window of the baseline. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | The Gateway Schedule lists the eight gateways once each with document, decision date and owner; every document exists, including MIL-008. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | The decision dates of MIL-001 to MIL-007 equal the Target Dates of their milestone documents (read for this review, MIL-007 as an example: 2026-11-30); MIL-008 decides on 2026-11-23, which is its Target Date and inside the window of the Business Case. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage maps every In Scope item of BC-001 to a gateway; a row for the baseline item was added in this change. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Dependencies state the chain MIL-001 to MIL-008; it is acyclic. The dates of MIL-004 to MIL-007 are later than the start of MIL-008 because those milestones were finished early; this is stated in the Planning Assumptions, and MIL-008 depends only on the merge of MIL-007. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | Dependencies state that a No-Go is fixed and re-reviewed, that later dates move by the same amount and that S01 decides a move of the end date; the baseline adds a CI risk with the rule of three failed rounds. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | Owner S01 is a stakeholder ID of SA-001, and GOV-001 does not name another role for the owner; no invented role names are used. |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Each planning assumption names its source (a Business Case section, the Stakeholder Analysis or a decision of S01); the early finish of the first seven gateways is recorded. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Plan Risks give impact and mitigation for each of the four risks; the CI risk of MIL-008 traces to success criterion 8 of BC-001. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open Issues list the earlier points and add the milestone link of the baseline, the removed publish workflow, the screenshot folder, the domain of the unchanged documents and the live-service rule; no remaining statement contradicts another. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | The main deliverable of MIL-008 names the same items as its Deliverable section; the rows of MIL-001 to MIL-007 match their milestone documents (read for this review). |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | The Stories column says `none (technical tasks)` for every gateway; the Business Case has no use cases or user stories in scope, so no gateway delivers one. |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | The Gantt bars use the dates of the schedule table and the dependency line is the same chain as the schedule order. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Each gateway links its milestone on the git host (264 to 270 exist; the milestone of MIL-008 is linked after the sync). |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | PP-001 is the only Project Plan; its Version History records each change in its own row and only the latest row is Accepted. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | The Metadata table has `Language | en` and `Domain | education`; neither is a placeholder. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code and `education` is a row of the domain list of docs/artifact-registry.md. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | The prose and the table cells are English; only file names, commands and IDs are code. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | The registry gives the register `IT Executive English` for this type; the text is written for that reader. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No Domain Dictionary exists in this project, so there is no list of PO terms to compare with. The terms milestone, gateway, baseline and token are used in one meaning each in the added text, found by reading. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, section headings, IDs and statuses are the framework's English ones. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No file `<name>.<language>.md` exists beside the document. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | The `Domain` row changed from `it` to `education` in this version (the language `en` is unchanged). The Version History row records the change and this review covers it. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The stand-in reads English and knows the education domain and checked the terms; the check is autonomous and not independent. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations added by this change are spelled out where they are first used (SQA, QC, CI, PO) or are established names (README). |

## Overall Verdict

Go — every Mandatory criterion of QC-PP-001 and QC-LANG-001 passes; the domain of the unchanged documents, the removed publish workflow and the screenshot folder are recorded as Open Issues. Review of the whole document after the edits of this change.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| No open action | S01 | 2026-11-23 |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
