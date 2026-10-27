---
atom_id: CA-M-340
content_role: Method
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Active
author: Anatoly Maslennikov
version: 16
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Execution Control
  depends_on:
  - Subject/Graph Node/Engineering/Execution Control/Recovery
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Action Run
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Engineering/Execution Control/Effect Authorization
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Engineering/Execution Control
  - Subject/Graph Node/Implementation/Code
relations:
  method_for:
  - CA-R-1883
type: Eng Decision
tier: 4
---
# Summary

admit explicit frozen Release recovery

## Scope

the recovery path for one existing frozen **CA-O-164** Release Workflow Run.

## Claim

admit a Release recovery request by reopening the sealed Run evidence, validating the still-current admission boundary and recovering only exact pending Journal evidence before any remaining admitted continuation.

## Details

1. accept the typed recovery operation only with `operation: recover_selected_release`, the existing Release Workflow `run_id` and the sealed request identity. Reject extra authority-bearing payload fields.
2. reopen the frozen request, canonical Journal events, typed Release checkpoint and saved progress. Bind every observed Workflow, Step and Action occurrence to its declared actual Run ID and exact definition.
3. revalidate source freshness, route-bound Operator authorization and permission before continuation. Treat queue or DBOS state only as delivery state, never as a replacement for Journal history.
4. if a sealed pending event has not reached the Journal, validate its exact event identity, Run, outcome, result reference and effect references, then use the shared recorder to recover that one event. Do not create a replacement event.
5. continue only the remaining admitted work whose effects are certain and whose bindings still match. Preserve completed terminal facts. Stop with an explicit blocked or pending result whenever evidence is incomplete, stale, conflicting or uncertain.
6. observe a submitted recovery only through its returned scheduler handle, checking the DBOS workflow name and frozen Run input before exposing its transport state or result. Report that control-plane observation separately from canonical Journal state. Return a disposition for both queued and immediately terminal transport states; a successful transport does not mean that the canonical Release Run is complete.
