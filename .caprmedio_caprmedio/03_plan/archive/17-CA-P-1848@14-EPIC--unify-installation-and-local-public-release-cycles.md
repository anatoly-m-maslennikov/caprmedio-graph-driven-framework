---
atom_id: CA-P-1848@14
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 17
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
version: 14
updated_at: 2026-10-24 06:12:42 +0400
subjects:
  governs: CAPRMEDIO Framework Instance
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Framework Instance Settings
  - Framework Package
  - Methodology Source
  - Applicable Methodology
  - Project Structure
  - Requirement
  - Method
  - Delivery
  - Workflow
  - Action
  - Subject/Domain/Node/Continuant/History/Journal
  - Workflow Run
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Projection
  - Status
  - Content Role
  - Project Settings
  - Evaluation
  - Tool
  - Version
relations: {}
tier: 3
---
# Summary

Unify installation **and** local/public release cycles

## Objective

The caprmedio Project provides simple, tested Local and Public release workflows and a reusable Framework package with an isolated runtime for each Project.

## Details

### Current Operator-approved scope

This direct happy path replaces the earlier release-sealing design. Release hashes, snapshots, admission records, package selectors, rollback, compatibility migration and recovery machinery are not prerequisites for these workflows. Preserve existing historical records; do not replay their Runs.

There are two Operator-invoked workflows. Neither runs automatically.

### Local release

Commit **everything** in Git before **every** step below, and once more at the end. Respect Git ignore rules and secret exclusions. Stop on a failed commit or step and write an issue report for manual handling; do not continue or roll back automatically.

1. Test the tools used by this release path.
2. Clear the product contents in `101_FRAMEWORK_METHODOLOGY`, preserving configuration, then copy the active Methodology-source Atoms from the Project's declared source folders. Exclude drafts and archives; ignore `.DS_Store`. Copy the supporting files needed by the compiler.
3. Compile Applicable Methodology in the product directory.
4. Replace the installed Methodology at `.caprmedio_caprmedio/000_CAPRMEDIO_framework` with the product as-is, preserving existing configuration.
5. Copy the Engine, delivered Methodology, locked dependencies and `ca` Skill into the reusable `.caprmedio_install` package; install that package into this Project's `.caprmedio_runtime` and install the project-local `ca` Skill. Preserve runtime configuration and existing Project records.
6. Build and start the Docker runtime; verify the actual returned MCP endpoint.
7. Remove only superseded images proven to belong to this Project. Retain current, unrelated and in-use images; report anything that cannot safely be removed.

The Project's editable Atoms remain in `.caprmedio_caprmedio`; `101_FRAMEWORK_METHODOLOGY` is the product; `000_CAPRMEDIO_framework` is the installed version. Project settings, structure, Operator registry and existing runtime configuration are not replaced. Other Projects and their runtimes remain separate.

### Public release

Test the intended release tools. Use one prompt for the full PR description, including What's new and What's fixed, and its concise bullet summary for Version History. Update README as needed. Version History contains only the summary and the actual PR link. Commit everything before each step and at the end, push to `amm/dev`, and create or update the PR to `main`; do not merge.

Local numbering adds/increments the fourth numeric component. Public numbering increments the third component and removes the fourth. Neither has a digit rollover.

### Implementation and work organization

- Keep both workflows available through Project MCP.
- Local release is programmatic; Public release has one content prompt.
- Concrete release Operations are Project-local. Their helper specifications and implementation belong to PROJECT_TOOLS; do not ship Project release procedures as general Methodology.
- Reuse existing compiler, installer and startup code only where it does not reintroduce the removed release prerequisites.
- Refactor the existing release entrypoints rather than adding parallel functions or capabilities. Disable release behavior outside the steps listed here.
- Journal actual workflow/action outcomes and keep a readable report. A queued Run, mock test or historical pass is not completed live execution.
- The existing decomposing Plans retain useful implementation responsibilities. Their snapshot, admission, recovery and complete-corpus test obligations are superseded by this current scope.
- Git and live effects have one owner; independent code, tests and documentation can be delegated.
- A workflow failure records its step and error. Further handling is manual.

- Completion evidence: Both direct workflows are implemented and their intended tests passed (16 tests, 19.160 seconds). Local Run epic1848-direct-local-20261012-001 copied and compiled active Methodology, preserved configuration, installed the package/runtime/ca Skill and demonstrated Docker MCP; see .caprmedio_runtime/simple_local_release/reports/epic1848-direct-local-20261012-001.md and .caprmedio_tmp/epic1848/direct-local-completion.md. Public Run epic1848-direct-public-20261012-001 completed for version 0.4.3, pushed to amm/dev and created PR 27 with complete notes and the actual Version History link. Final authority review resolved R-1922/R-1924 and retired O-198; unused legacy release code remains deferred outside this direct path.
- Public evidence: Run epic1848-direct-public-20261012-001 completed for 0.4.3; PR https://github.com/anatoly-m-maslennikov/caprmedio-graph-driven-framework/pull/27. Journal started Event 803fbb4b-8b3a-4a2a-9839-a65251d46e02; completed Event 8bdb213a-13be-4f26-9c87-0a44dfc30b34.

- Public completion receipt: .caprmedio_tmp/epic1848/direct-public-completion.md.

- No-merge correction verified: new Public PRs are created Draft and an existing open PR is converted to Draft before editing. Five focused Public tests passed; PR 27's earlier external bot merge remains recorded rather than rolled back.

## Definition of Done

The Epic is Done only when both updated workflow implementations and their intended tests are complete, the Local release has actually copied and compiled active Methodology, preserved configuration, installed the reusable package and Project runtime/Skill, and demonstrated Docker MCP operation. Public release must produce the requested description/history format, push to amm/dev and create or update its PR to main without merging. Before marking completion, record actual evidence for each in-scope decomposing Plan and report remaining manual issues. Do not claim a release or PR that was not executed.
