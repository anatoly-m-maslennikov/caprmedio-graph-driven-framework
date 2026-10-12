---
atom_id: CA-P-1848
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 17
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 11
updated_at: "2026-10-12 03:32:38 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on:
    - "Project"
    - "Plan"
    - "AI Agent"
    - "Operator"
    - "Framework Instance Settings"
    - "Framework Package"
    - "Methodology Source"
    - "Applicable Methodology"
    - "Project Structure"
    - "Requirement"
    - "Method"
    - "Delivery"
    - "Workflow"
    - "Action"
    - "Journal"
    - "Workflow Run"
    - "Carrier"
    - "Scope Unit"
    - "Atom"
    - "Projection"
    - "Status"
    - "Content Role"
    - "Project Settings"
    - "Evaluation"
    - "Tool"
    - "Version"
relations: {}
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

## Definition of Done

The Epic is Done only when both updated workflow implementations and their intended tests are complete, the Local release has actually copied and compiled active Methodology, preserved configuration, installed the reusable package and Project runtime/Skill, and demonstrated Docker MCP operation. Public release must produce the requested description/history format, push to amm/dev and create or update its PR to main without merging. Before marking completion, record actual evidence for each in-scope decomposing Plan and report remaining manual issues. Do not claim a release or PR that was not executed.
