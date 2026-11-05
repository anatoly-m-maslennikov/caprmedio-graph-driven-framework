---
atom_id: CA-D-524
ref_id: CA-D-524
role: Delivery
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Active
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-27 19:59:26 +0400
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
    name: CA-D-524-WORKFLOW_ORCHESTRATOR-ENG_DECISION--carry-coverage-gate-and-operator-question-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/07_delivery
---
# Summary

Carry coverage gate and Operator question results

## Scope

RMED Atoms Base Revise execution in WORKFLOW_ORCHESTRATOR.

## Claim

Coverage Gate results **must** carry the following evidence fields.

## Details

- phase, expected, covered, missing, coverage_percent, result **and** operator_question.
- result: covered **or** ask_operator. unknown accounting has coverage_percent=null, **not** **`=100`**.
- Run status includes coverage_gates **and** operator_question. a failed gate sets outcome=interrupted **and** leaves completed work intact.
- full reports include a Coverage Gates section; confirmed gate events use the existing shared Project Journal.
- Workflow gate Action: CA-O-118; phase substeps: CA-O-119, CA-O-120, CA-O-121.
