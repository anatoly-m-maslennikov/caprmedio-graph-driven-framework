---
atom_id: CA-D-577@16-draft
ref_id: CA-D-577@16-draft
container:
  scope_unit: CA-SU-2
role: Delivery
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Data
    Validation
  dependencies:
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Recovery
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect
    Authorization
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Serialization
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code
tier: 5
relations:
  delivery_for:
  - CA-R-1883
  - CA-M-340
  - CA-O-164
status: Draft
version: 16
updated_at: 2026-11-09 05:58:14 +0400
carrier_destination:
  file:
    name: CA-D-577@16-draft-WORKFLOW_ORCHESTRATOR-ENG_DECISION--carry-typed-release-recovery-requests.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/07_delivery/draft
current_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
---

## Summary

carry typed Release recovery requests

## Claim

### Prose Claim

the Release recovery request Carrier **must** contain only the typed operation, existing Run ID and sealed request identity needed to reopen an existing frozen Release Run.

## Details

### Scope

the WORKFLOW_ORCHESTRATOR request and retained-state Carriers for recovering one frozen **Release Version** Workflow Run.

- request schema: `operation: recover_selected_release`, `run_id` and `request_identity`. No arbitrary execution object, definition selection, Action payload, source path, permission grant, executor choice or effect instruction is admitted.
- the request is retained with the existing frozen selected request, dispatch intent, typed Release checkpoint, Action progress and result references in that Run's configured orchestrator state directory.
- canonical Workflow, Step and Action starts, recovered pending events, effects and terminal facts remain schema-v5 Work Journal records. The request Carrier, queue and DBOS state are transport and observation records, not a second Run Journal.
- the request response reports the same Run ID, operation disposition, canonical Journal references and blocked or pending reason where applicable. It does not claim a new Run, completion or recovered effect without exact canonical evidence.
- a separate read-only observation Carrier contains only `operation: recover_selected_release_status`, the same existing `run_id` and one returned recovery transport handle. It reads that exact DBOS handle and verifies its Release-recovery workflow binding and frozen Run identity; it neither queues, starts nor records a Run. Canonical Journal state remains separately reported and no prior canonical scheduler result is presented as recovery output.
