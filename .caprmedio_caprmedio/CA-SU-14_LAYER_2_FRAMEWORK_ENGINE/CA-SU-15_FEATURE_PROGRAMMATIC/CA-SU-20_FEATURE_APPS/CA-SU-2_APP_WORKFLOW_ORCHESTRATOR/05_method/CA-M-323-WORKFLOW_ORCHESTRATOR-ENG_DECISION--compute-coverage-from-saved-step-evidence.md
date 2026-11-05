---
atom_id: CA-M-323
ref_id: CA-M-323
role: Method
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Active
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-27 19:59:42 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run.Coverage
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
form: Eng Decision
tier: 3
container:
  scope_unit: CA-SU-2
carrier_destination:
  file:
    name: CA-M-323-WORKFLOW_ORCHESTRATOR-ENG_DECISION--compute-coverage-from-saved-step-evidence.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/05_method
---
# Summary

Compute coverage from saved Step evidence

## Scope

RMED Atoms Base Revise execution in WORKFLOW_ORCHESTRATOR.

## Claim

the Coverage Gate **must** derive its accounting from the frozen request **and** saved results without another semantic Atom evaluation.

## Details

- compare gather identities, ordered paths **and** frozen source/rule observations.
- check every required slot for concluded status **and** evidence; retain coverage gaps **and** blockers.
- use existing finding-disposition **and** completion predicates for fix coverage.
- record the gate once per phase in the existing Run state, Journal **and** full report; recovery reuses the same evidence rather than replaying completed effects.
- run gates as durable DBOS Steps; keep coverage interruption distinct from scheduler failure.
