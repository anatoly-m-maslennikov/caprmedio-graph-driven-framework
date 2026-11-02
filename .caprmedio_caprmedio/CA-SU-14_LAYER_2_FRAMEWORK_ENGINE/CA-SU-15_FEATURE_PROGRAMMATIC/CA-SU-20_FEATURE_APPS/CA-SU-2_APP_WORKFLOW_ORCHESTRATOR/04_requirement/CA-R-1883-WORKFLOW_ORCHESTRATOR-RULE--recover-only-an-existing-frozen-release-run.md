---
atom_id: CA-R-1883
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Active
author: Anatoly Maslennikov
version: 15
updated_at: 2026-10-27 20:00:05 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Recovery
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Action Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
relations: {}
tier: 3
type: Rule
---
# Summary

recover only an existing frozen Release Run

## Scope

an interrupted **Release Version** Workflow Run already admitted under **CA-O-164**.

## Claim

WORKFLOW_ORCHESTRATOR **must** admit Release recovery only for **=1** existing frozen Release Workflow Run whose exact request identity, source freshness, current permission and canonical Work Journal evidence remain valid.

## Details

- recovery is a distinct operation, not an `enqueue`, `enqueue_selected`, redispatch or new Release request.
- recovery binds the requested Run ID and its sealed request identity to the existing frozen Release request, exact Workflow, Step and Action definitions, current source and route-bound Operator authorization.
- recovery can reconcile and append only an exact sealed pending Journal event through the shared recorder. It cannot accept arbitrary payload data, select another Run, create a new start, replace a terminal fact or invent a receipt.
- an unresolved in-progress or uncertain effect, changed binding, stale source, revoked permission, missing proof or conflict blocks continuation for Operator resolution. Recovery does not replay that effect.
- queue, DBOS and client transport state can carry recovery delivery and observation. The canonical Work Journal remains the historical authority for actual Runs, starts, effects and terminal facts.
