# Review of the publish-wiki workflow of MIL-007

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-017 |
| CrossReference | [MIL-007], [QC-WF-001], [QC-YML-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [e041fbe] |

---

## Artifact Under Review

- Instance reviewed: [MIL-007] (the workflow `.gitea/workflows/publish-wiki.yml`, task 5)
- Checklist used: [QC-WF-001] and [QC-YML-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

Workflow checklist (`QC-WF-001`):

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file meets the YAML checklist ([QC-YML-001]) | Pass | Passes the YAML checklist below. |
| 2 | The file is in `.gitea/workflows/` or `.github/workflows/` with the extension `.yml` or `.yaml`, and the same workflow does not exist in both directories | Pass | File is .gitea/workflows/publish-wiki.yml; no copy in .github/workflows. |
| 3 | The file declares `name`, `on` and `jobs`; `on` lists explicit events and, where it matters, `branches` or `paths` | Pass | name, on (push, branches main, paths docs/wiki/**) and jobs are declared. |
| 4 | A header comment states the purpose, the triggers, the inputs, the secrets it needs, what it changes outside the repository, and the decision or milestone it implements | Pass | Header states purpose, trigger, inputs, secret, outside effect and decision MIL-007. |
| 5 | Every job and step has a descriptive `name`, unique within its job | Pass | Job name `Publish wiki pages`. |
| 6 | The file passes `actionlint` (or the project's workflow validation test) and the tool version is stated | Pass | `actionlint` 1.7.12 reports no finding. |
| 7 | Every job declares `permissions` explicitly with the least access that works (`contents: read` or none by default); write access only on the job that needs it | Pass | Workflow level `permissions: contents: read`; the reusable workflow uses the wiki token secret. |
| 8 | Every action used is pinned to a full commit SHA or an exact release tag, never to a branch; a moving major tag (`@v1`) is accepted only for an action published by the same organisation under a stated release policy | Pass | `@v1` of TirSystem/git-workflows, the organization that also publishes the framework, under its release policy for the major tag (same as the framework template). |
| 9 | No secret is written in the file; a secret is read as `secrets.NAME`, passed to a step through `env:`, never placed on a command line or echoed | Pass | Only `secrets.TOKEN_FOR_GITEA_WIKI` is referenced, passed by name. |
| 10 | Untrusted text (`inputs.*`, event fields such as a title, branch name or label, step outputs derived from them) is never interpolated into a `run:` script; it is passed through `env:` and used as a quoted variable | Pass | No untrusted text is used in any script; the workflow has no run: step. |
| 11 | A trigger that gives a run secrets or a write token on code from a fork or an untrusted branch (`pull_request_target`, `workflow_run`) does not check out or execute that code | Pass | Trigger is `push` to main only; no pull_request_target or workflow_run. |
| 12 | A workflow that changes state outside the repository (release, tag, publish, sync, deploy) is started by hand or by a protected branch, and a manual run defaults to a dry run with an explicit input to apply | Pass | Started only by a push to the protected branch main; the manual trigger of the template was removed so no unplanned run changes the wiki. |
| 13 | The token the workflow uses has only the scope the job needs, and where the host's built-in token is enough it is used instead of a personal token | Pass | The token scope is write:repository for the wiki only (header). |
| 14 | Every job sets `runs-on` to an explicit label and `timeout-minutes` | N-A | The job only calls a reusable workflow; `runs-on` and `timeout-minutes` are set inside it (a calling job cannot set them). |
| 15 | `concurrency` is set where two runs would conflict: a check cancels the older run (`cancel-in-progress: true`); a publishing job queues (`cancel-in-progress: false`) | Pass | `concurrency` group publish-wiki with `cancel-in-progress: false`: publishing runs queue. |
| 16 | Triggers are filtered (`branches`, `paths`, `types`) so the workflow runs only for the changes it concerns | Pass | Filtered by branch main and paths docs/wiki/**. |
| 17 | Tools and dependencies are installed at pinned versions; a version is a workflow input with a default or a value in one place | N-A | The workflow installs no tools; the called workflow is pinned by @v1. |
| 18 | A dependency cache is used where the install is slow enough to matter | N-A | Nothing is installed. |
| 19 | A failing step names the tool, the file and the reason in its log (annotation or `::error::` line) | N-A | No step of its own. |
| 20 | A `run:` block is within the limit on embedded program text of criterion 7 of [QC-YML-001]; a longer script is a file (`tools/`, or a shared repository fetched at a pinned ref) that the step calls with one command, and the workflow passes its settings through `env:` | N-A | No run: block. |
| 21 | Logic used by more than one workflow or repository is a reusable workflow (`workflow_call`) or a composite action; each input has a `description`, a `type` and a `default` where one is sensible | N-A | This file is the caller of a reusable workflow, not a new reusable unit. |
| 22 | Every workflow feature used is verified on the instance that runs it, and the host and version are recorded; a feature the target hosts differ on is noted in the header | Pending | Not verified on the instance: the secret TOKEN_FOR_GITEA_WIKI and a runner are not set up by the author of this review; S01 verifies the first run and records the Gitea version. |
| 23 | A reusable workflow states, in its header, how a caller pins it and the script it fetches, so the workflow and its script are the same release | Pass | Header names the called workflow and its major tag. |
| 24 | A static test of the repository's workflows exists and runs on every pull request: valid YAML, required keys, explicit permissions and runner, no inline script above the limit | N-A | No static workflow test exists in this project; actionlint and yamllint were run by hand. Optional. |

YAML checklist (`QC-YML-001`):

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file parses with a safe YAML loader and has no duplicate keys in any mapping | Pass | yamllint 1.38.0 parses the file; no duplicate keys. |
| 2 | Indentation is 2 spaces everywhere, never tabs; lines end with LF; the file ends with one newline and has no trailing spaces | Pass | 2 spaces, LF, one final newline (yamllint). |
| 3 | Passes `yamllint` (or the project's YAML linter) with its configuration committed next to the code and no unexplained `disable` comments | Pass | yamllint 1.38.0 with `.yamllint` committed; no disable comments. |
| 4 | A scalar that YAML would coerce to another type is quoted: `yes`, `no`, `on`, `off`, `null`, `~`, numbers with a leading zero, versions such as `1.10`, and values that contain `: ` or ` #` | Pass | `on` is not an issue for the loader; `prune` is quoted as a string. |
| 5 | Only safe, plain types are used: no language-specific tags (`!!python/object`, `!ruby/object`) and no `!include`-style extension unless the consuming tool documents it | Pass | No tags. |
| 6 | No secret is written in the file: no password, token, key or private connection string; a secret is referenced by name and supplied by the consuming tool | Pass | No secret is written in the file. |
| 7 | Embedded program text (shell, Python, SQL, `jq`, and so on) in a value is at most five lines; a longer one is moved to a file of its own, in its own language, and the YAML calls it | Pass | No embedded program text. |
| 8 | A block of keys or values repeated in the file or across files is defined once (an anchor, a template, an include or a reusable unit the consumer supports) | Pass | Nothing repeated. |
| 9 | Anchors, aliases and merge keys (`&`, `*`, `<<`) are used only where the consuming tool is known to support them | Pass | No anchors or aliases. |
| 10 | The file validates against the schema of the consuming tool where one exists, and the schema or tool version is stated | Pass | actionlint validates the workflow schema (1.7.12). |
| 11 | A header comment states what the file is for, which tool reads it, and where its decision or design is recorded | Pass | Header states purpose, tool and the decision. |
| 12 | Key names follow the convention of the consuming tool; one case style is used within the file (kebab-case or snake_case, never mixed) | Pass | Keys follow the Gitea Actions convention (snake_case in `with`, lowercase elsewhere). |
| 13 | Multi-line strings use a block scalar (`\|` or `>`) and state the chomping indicator (`\|-`, `\|+`) where the trailing newline matters | Pass | No multi-line scalars. |
| 14 | The file name is lowercase kebab-case with one extension style (`.yml` or `.yaml`) used throughout the repository | Pass | `publish-wiki.yml`, lowercase kebab-case, `.yml`. |
| 15 | A change is exercised by a check that runs without the real target: a parse and schema test, or a dry run of the consuming tool | Pass | Exercised by actionlint and yamllint without the real target. |

## Overall Verdict

Go-with-conditions — every Mandatory criterion passes except criterion 22 of QC-WF-001, which stays `Pending`: only a first run on the Gitea instance can verify it. The workflow also only works once the organization secret `TOKEN_FOR_GITEA_WIKI` exists and a runner is registered.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Create the organization secret `TOKEN_FOR_GITEA_WIKI` and register a runner | S01 | 2026-11-30 |
| Check the first run of the workflow on the Gitea instance and record the Gitea version (criterion 22) | S01 | 2026-11-30 |

---

[MIL-007]: ../../milestones/mil-007-wiki-and-release.md
[QC-WF-001]: ../../../framework/qc/code/qc-workflow.md
[QC-YML-001]: ../../../framework/qc/code/qc-yaml.md
[e041fbe]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/commit/e041fbefa21d66d0e1a429b90168123dbdc4ff94
