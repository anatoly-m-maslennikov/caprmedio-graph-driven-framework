---
atom_id: CA-M-340
ref_id: CA-M-340
container:
  scope_unit: CA-SU-2
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Recovery
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Action Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code
tier: 4
relations:
  method_for:
  - CA-R-1883
status: Active
version: 17
updated_at: 2026-10-27 19:59:42 +0400
carrier_destination:
  file:
    name: CA-M-340-WORKFLOW_ORCHESTRATOR-ENG_DECISION--admit-explicit-frozen-release-recovery.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/05_method
current_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
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
