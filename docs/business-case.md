# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [PP-001], [MIL-008] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [01e016e] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added objective 7, success criterion 8, a scope item, an out-of-scope item, a risk and constraints for the baseline milestone MIL-008; set the domain to education; reviewed in autonomous mode, not independent | [e7fe610] |

---

## Executive Summary

Course participants of the Udemy "100 Days of Code" bootcamp (day 46, "Musical Time Machine") need a worked, runnable solution to the assignment: pick a date, scrape the Billboard Hot 100 chart of that date, and build a private YouTube Music playlist from it. This project delivers that solution as a small, readable Python 3.13 command line application with tests, documentation and a trilingual wiki (English, Danish, Bahasa Malaysia), so that fellow participants (S02) and repository viewers (S03) can read, run and learn from it.

## Methodological and Standards Foundation

The project follows the software quality assurance (SQA) and quality control (QC) framework mounted at `framework/` (plan-first gate, review against QC checklists). Design artifacts, where needed, follow Larman's *Applying UML and Patterns*. Quality is stated with the ISO/IEC (International Organization for Standardization and International Electrotechnical Commission) 25010:2023 characteristics. The code follows the `clean-architecture` and `coding-conventions` skills of the framework.

## Problem Statement

- The assignment gives instructions in prose only; participants who get stuck on scraping, on the `ytmusicapi` browser authentication or on the playlist calls have no tested reference.
- The Billboard site can change or add a paywall at any time, so a reference must also work against the course's clone site, Bakeboard.
- Shared solutions are often a single untested script with no instructions to run it.

## Business Opportunity

A documented, tested and screenshot-illustrated solution makes the assignment repeatable for other participants, and shows a clean way to structure a small scraping and API project. It is a portfolio item for S01.

## Objectives

1. O1: Deliver an application that asks for a date (YYYY-MM-DD) and scrapes the 100 song titles and artists of that date from Bakeboard into a Python list.
2. O2: Authenticate to YouTube Music with `ytmusicapi` using a `browser.json` file and verify the connection by counting the library playlists.
3. O3: Create a private playlist named `{date} Billboard 100`, without creating a duplicate when it already exists.
4. O4: Search each song and add the top song result to the playlist, skipping failures without stopping.
5. O5: Provide automated tests, a README with setup, run and test instructions, a Doxygen configuration and a wiki in English, Danish and Bahasa Malaysia, with a screenshot for each lecture step.
6. O6: Publish the repository with a description and topics.
7. O7: Bring the finished project to the common baseline of the framework: the adopted framework release, a wiki that follows the framework's page and language-line rules, licence and project URL metadata, a README that lists only the documents of the repository, and review records for every changed document ([MIL-008]).

## Scope

### In Scope

- Python application in `src/`, tests in `tests/`, documents in `docs/`.
- Scraping of the Bakeboard clone site (`https://appbrewery.github.io/bakeboard-hot-100/`); the base URL is a constant so the real Billboard URL can be configured.
- YouTube Music authentication, playlist creation and song search through `ytmusicapi`.
- `pyproject.toml`, `.venv` instructions, `constants.py`, pytest tests, Doxygen comments and `Doxyfile`, `README.md` from the framework template.
- Wiki pages in en, da and ms, with a screenshot for each of the four lecture steps.
- Repository description and topics on the git host.
- The baseline milestone [MIL-008]: the framework release, the wiki in the framework's shape (language line first on each page, screenshots in `docs/images/`), the README without the private framework files in its appendix, licence and project URL metadata, `.editorconfig`, `.env.example` and review records. It changes no behaviour of the program.

### Out of Scope

- Spotify (the course path chosen is YouTube Music).
- Automating the creation of `browser.json`; it is a manual step of S01 and contains personal session cookies.
- A graphical user interface.
- Using the git host tokens in `.env` inside the application or its tests.
- Any change to `src/` or `tests/` in the baseline milestone [MIL-008]. No chart is scraped from a live site and no YouTube Music call is made in that milestone; the tests use a stored chart page and a fake music service.

## Expected Benefits

### Tangible Benefits

- A runnable solution with a passing automated test suite.
- A README and a wiki in three languages that another participant can follow without help.

### Intangible Benefits

- Better understanding of HTTP headers, HTML parsing and cookie-based API authentication.
- A clearer repository for viewers (S03).

## Strategic Alignment

The project supports S01's goal of completing the bootcamp with portfolio-quality work, and the course community's habit of sharing and comparing solutions (S02, S03).

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Songs scraped for a valid Bakeboard date | 100 titles with artists | Automated test on a stored copy of the page, plus one run against the live site |
| 2 | Automated tests | All pass; line coverage of `src/` at least 85 % | `python -m pytest` |
| 3 | Duplicate playlist | 0 duplicates after two runs with the same date | Test with a fake YouTube Music client |
| 4 | A failing song | Run continues and reports the skipped count | Test with a fake client that raises for one song |
| 5 | Runtime dependencies | At most 3: `requests`, `beautifulsoup4`, `ytmusicapi` | `pyproject.toml` |
| 6 | Documentation | README with setup, run and test sections; wiki pages in en, da, ms with 4 step screenshots each | File check in the milestone review |
| 7 | Repository metadata | Description and at least 5 topics set | Git host API response |
| 8 | The baseline milestone is done (objective 7) | Every wiki page starts with its language line, the screenshots are in `docs/images/`, `framework/scripts/check-readme.sh`, `check-languages.sh` and `check-editorconfig.sh` exit with code 0, `python -m pytest` passes, 100 % of the continuous integration (CI) checks of the pull request of [MIL-008] pass | Files in `docs/wiki/` and `docs/images/`, the script exit codes and the pull request status on the git host |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The Bakeboard or Billboard page markup changes | Scraper returns no songs | Selectors are constants; the scraper raises a clear error on an empty result; tests use a stored page |
| `browser.json` is missing or its cookies have expired | Steps 2 to 4 cannot be run live | README documents how to renew it; the live steps are marked as needing S01; automated tests use a fake client |
| Personal cookies or tokens are committed | Account takeover | `browser.json` and `.env` are in `.gitignore`; the app and tests never read `.env` |
| `ytmusicapi` changes its interface | Playlist code breaks | The library is behind a port (an interface) and its version is bounded in `pyproject.toml` |
| Screenshots show personal data | Privacy loss | Screenshots are taken of terminal output and public pages, and checked before commit |
| The documents of the baseline milestone [MIL-008] change documents that were accepted earlier, and the AI stand-in for S01 reviews them | A defect is missed because the review is not independent | Every review record of the baseline says `Mode: autonomous, not independent`, `src/` and `tests/` are not changed, the tests run before and after, and the end-of-run summary lists the reviews for challenge |

## Assumptions

- S01 has a Google account and Firefox, and will create `browser.json` by hand as the lecture describes.
- Python 3.13 or later is installed.
- The git host repository exists under the owner given by the `origin` remote, and the `GITEA_TOKEN` in `.env` may write to it.
- Reviews are done by the AI as stand-in for S01, as the autonomous mode of `AGENTS.md` allows.

## Constraints

- Python 3.13 or later, a `venv` named `.venv`, pytest, constants in `constants.py`, configuration in `pyproject.toml`.
- Folder structure `src/`, `tests/`, `docs/`; Doxygen comments in the source.
- Runtime dependencies only where needed.
- One branch and one pull request per milestone, to keep track of the steps.
- Planned window: 2026-10-28 to 2026-11-30. The baseline milestone [MIL-008] starts 2026-11-16 and is finished within one week, by 2026-11-23, inside that window. For that milestone only, an AI stand-in for S01 reviews and accepts the changed documents.
- The Product Owner's language is English and the wiki is written in en, da and ms. The PO domain is education (it was IT until [MIL-008]; the documents that [MIL-008] does not change keep the domain `it`, see the Open Issues of [PP-001]).

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About 25 hours of S01's and AI time over five weeks; no licence or hosting cost | A reusable reference solution, a portfolio piece and a three-language learning wiki. The assessment is qualitative because the project has no revenue; its value is learning and sharing. |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Completes the assignment; decides, builds and reviews |
| S02 | Reads and runs the code and compares solutions |
| S03 | Browses the repository for ideas |

## Recommendation

Proceed — the scope is small, the dependencies are few and the result is useful to all three stakeholders.

---

[SA-001]: ./stakeholder-analysis.md
[01e016e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/commit/01e016e15dd93cface4f4ae9e9e99919e0aace2b
[PP-001]: ./project-plan.md
[MIL-008]: ./milestones/mil-008-framework-baseline.md
[e7fe610]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/commit/e7fe610b57cf2b96a58fb349ef0d9a14c3530481
