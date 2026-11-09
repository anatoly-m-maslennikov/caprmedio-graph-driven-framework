---
atom_id: CA-E-583
ref_id: CA-E-583
container:
  scope_unit: CA-SU-27
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Recovery
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Action Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect
    Authorization
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code
tier: 6
relations:
  evaluation_for:
  - CA-R-1883
  - CA-M-340
  - CA-D-577
status: Active
version: 19
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-E-583-FRAMEWORK_DELIVERY-EVAL_CASE--verify-explicit-frozen-release-recovery.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/06_evaluation
current_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

## Summary

verify explicit frozen Release recovery

## Claim

### Prose Claim

the Evaluation **must** verify that Release recovery accepts only the exact frozen Run and preserves canonical Journal identity without replaying uncertain effects or creating extra Run facts.

## Details

### Scope

the typed recovery admission and continuation boundary for one existing **CA-O-164** Release Workflow Run.

- submit a recovery request for an existing interrupted Release Run and verify the sealed request identity, source freshness and current route-bound Operator authorization are required.
- submit a different Run ID, changed request identity, stale source, revoked permission, unknown field or arbitrary continuation payload and verify recovery blocks before an effect, start or terminal Journal event.
- recover one valid sealed pending Action event and verify the shared recorder appends its original bytes and receipt only. Verify changed Run, phase, outcome, result reference or effect reference blocks recovery.
- reopen a completed Workflow and verify it returns its original terminal result with no new Workflow, Step or Action start or terminal event.
- present an unresolved in-progress or uncertain effect and verify recovery returns blocked or pending without native effect replay. Verify queue and DBOS records do not override the canonical Journal.
- observe one queued recovery transport, then its success or failure, and verify the exact returned handle and frozen Run binding are required. Verify the original Run's cached DBOS result is reported only as canonical history, never as the recovery transport result. Also submit a recovery whose scheduler response is immediately successful, failed or canceled and verify it has a transport-only disposition, not a claim of canonical completion.
