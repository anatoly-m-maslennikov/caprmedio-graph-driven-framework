---
atom_id: CA-R-1883@4
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-24 00:38:25 +0400
subjects:
  governs: Release Version recovery request
  depends_on:
  - Release Version
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Domain/Node/Occurrent/Execution/Step Run
  - Action Run
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Permission
  - Subject/Domain/Node/Continuant/History/Journal
  - Source
  - Implementation
relations:
  relates_to:
  - CA-R-1524
  - CA-D-574
  - CA-O-164
tier: 3
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
