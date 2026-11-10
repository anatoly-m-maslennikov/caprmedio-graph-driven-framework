---
atom_id: CA-M-323
ref_id: CA-M-323
container:
  scope_unit: CA-SU-20
role: Method
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run.Coverage
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 4
status: Archived
version: 10
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-M-323@10-APPS-DECISION--compute-coverage-from-saved-step-evidence.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/05_method/archive
current_scope_unit: APPS
author: Anatoly Maslennikov
relations:
  method_for:
  - CA-R-1817
---

## Summary

Compute coverage from saved Step evidence

## Claim

### Prose Claim

the Coverage Gate **must** derive its accounting from the frozen request **and** saved results without another semantic Atom evaluation.

## Details

### Scope

RMED Atoms Base Revise execution in WORKFLOW_ORCHESTRATOR.

- compare gather identities, ordered paths **and** frozen source/rule observations.
- check every required slot for concluded status **and** evidence; retain coverage gaps **and** blockers.
- use existing finding-disposition **and** completion predicates for fix coverage.
- record the gate once per phase in the existing Run state, Journal **and** full report; recovery reuses the same evidence rather than replaying completed effects.
- run gates as durable DBOS Steps; keep coverage interruption distinct from scheduler failure.
