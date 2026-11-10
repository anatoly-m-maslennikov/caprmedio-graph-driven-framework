---
atom_id: CA-R-1813
ref_id: CA-R-1813
container:
  scope_unit: CA-SU-20
role: Requirement
form: Rule
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Recovery"
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Dynamic Testing"
tier: 3
status: Archived
version: 12
updated_at: 2026-10-27 20:00:03 +0400
carrier_destination:
  file:
    name: CA-R-1813@12-APPS-RULE--recover-agent-execution-without-repeating-edits.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement/archive
current_scope_unit: APPS
author: Anatoly Maslennikov
---
# Summary

Recover Agent execution without repeating edits

## Scope

WORKFLOW_ORCHESTRATOR's initial local execution capability.

## Claim

WORKFLOW_ORCHESTRATOR **must** recover interrupted execution **without** replaying a completed Atom edit.

## Details

- use a stable dispatch identity for each selected Atom **and** phase.
- retain accepted Agent output before source effects. admit reports through the existing coordination Tool.
- before applying an accepted edit, compare the current source with the saved before **and** after hashes: apply the before case, acknowledge the after case, **and** block any other case.
- a worker loss **during** unacknowledged Agent execution leaves execution uncertain; require explicit recovery rather than silently launching another effectful session.
- transport retry does **not** grant semantic repair permission. replay recorded completed outputs rather than rerunning completed checks.
