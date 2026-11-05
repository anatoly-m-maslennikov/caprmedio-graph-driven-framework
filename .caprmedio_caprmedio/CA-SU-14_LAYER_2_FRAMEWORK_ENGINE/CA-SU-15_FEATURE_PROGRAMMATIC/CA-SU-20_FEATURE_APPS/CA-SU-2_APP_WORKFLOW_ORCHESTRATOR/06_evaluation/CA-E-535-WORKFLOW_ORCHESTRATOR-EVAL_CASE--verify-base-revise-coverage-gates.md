---
atom_id: CA-E-535
ref_id: CA-E-535
container:
  scope_unit: CA-SU-2
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run.Coverage
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
status: Active
version: 9
updated_at: 2026-10-27 19:59:37 +0400
carrier_destination:
  file:
    name: CA-E-535-WORKFLOW_ORCHESTRATOR-EVAL_CASE--verify-base-revise-coverage-gates.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/06_evaluation
current_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
---
# Summary

Verify Base Revise coverage gates

## Scope

RMED Atoms Base Revise execution in WORKFLOW_ORCHESTRATOR.

## Claim

the Coverage Gate Evaluation **must** verify complete **and** incomplete phase accounting without semantic rechecks.

## Details

- complete gather/check/fix permits completion with **`=3`** saved gate results.
- missing selection, evidence, check result, finding disposition **or** recording receipt prevents continuation **and** exposes missing work **and** an Operator question.
- initial failed checks with full evidence are covered; blocked **or** pending checks are **not** covered.
- verify no extra Agent dispatch for gates, no retry loop **and** no source write **after** a check-coverage failure.
- test real DBOS scheduling with mock Agents **before** a bounded live run.
