---
atom_id: CA-R-1813@5
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-24 00:51:05 +0400
subjects:
  governs: Subject/Engineering/Tool//WORKFLOW_ORCHESTRATOR.Recovery
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Continuant/Atom
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Engineering/Workflow Orchestration/Authority and Recovery Evaluation
  - Subject/Engineering/Tool//WORKFLOW_ORCHESTRATOR.Recovery
relations:
  relates_to:
  - CA-R-1522
  - CA-R-1523
  - CA-R-1524
  - CA-O-104
tier: 3
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
