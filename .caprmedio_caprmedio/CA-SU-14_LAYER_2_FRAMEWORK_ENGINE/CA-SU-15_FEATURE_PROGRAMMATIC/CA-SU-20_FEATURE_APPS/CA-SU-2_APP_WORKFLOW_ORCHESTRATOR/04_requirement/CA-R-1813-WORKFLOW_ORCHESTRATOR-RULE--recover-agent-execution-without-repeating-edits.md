---
atom_id: CA-R-1813
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Active
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-27 20:00:03 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Recovery
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Dynamic Testing
relations: {}
tier: 3
type: Rule
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
