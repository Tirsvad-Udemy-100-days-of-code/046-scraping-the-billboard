# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [01e016e] |

---

## Purpose

This analysis names the people who influence or are interested in the project, so later artifacts can cite them by ID for ownership and review. It uses a power/interest grid and the FURPS+ model (Functionality, Usability, Reliability, Performance, Supportability, plus design, implementation, interface and physical constraints) for concerns.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner (PO), developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | Complete the assignment with work of portfolio quality |
| S02 | Udemy coursists | Fellow participants who share and compare solutions | Udemy course community | LOW | HIGH | Keep Informed | Readable, runnable code that uses the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies they do not need |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, builds, reviews and accepts every artifact.
- **Keep Informed (S02):** no decision power, but they are the main readers; their needs set the readability and the instructions.
- **Monitor (S03):** occasional readers; the repository description, topics and README serve them.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The program does what the four lecture steps describe | Functionality |
| CN-002 | S01 | Tokens and cookies never reach the repository | Functionality (security) |
| CN-003 | S02 | Code is readable and uses the assignment's function names | Usability |
| CN-004 | S02 | The README tells how to set up the `.venv`, run and test | Usability, Supportability |
| CN-005 | S03 | The repository states clearly what it is, with a description and topics | Usability |
| CN-006 | S03 | No more runtime dependencies than needed | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| C1 | Chat with S01 | At plan acceptance and at the end of the run | Plan, run summary | MIL-001, MIL-007 |
| C2 | Pull request | One per milestone | Changes with closed issues | MIL-001 to MIL-007 |
| C3 | README and wiki | Updated in each milestone | Instructions, screenshots, lessons learned | MIL-002 to MIL-007 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| The assignment uses `requests` and `beautifulsoup4`, while S03 wants no runtime dependencies they do not need | S02, S03 | Keep the runtime to the three libraries the assignment needs (`requests`, `beautifulsoup4`, `ytmusicapi`) and state why in the README; development tools stay optional extras |
| S02 wants the assignment's flat function style, while the framework asks for layered clean architecture | S02, S01 | Keep the assignment's function names (`scrape_titles`, `create_playlist`) in the application layer and keep the layers few |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | [BC-001] O1, O2, O3, O4 |
| S01 | CN-002 | [BC-001] O2 and the out-of-scope rule on `.env` |
| S02 | CN-003, CN-004 | [BC-001] O5 |
| S03 | CN-005 | [BC-001] O6 |
| S03 | CN-006 | [BC-001] O5, success criterion 5 |

## Sign-Off

| Stakeholder | Date | Note |
| --- | --- | --- |
| S01 | [01e016e] | Accepts the plan in chat; the AI acts as stand-in for the review |

---

[BC-001]: ./business-case.md
[01e016e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/commit/01e016e15dd93cface4f4ae9e9e99919e0aace2b
