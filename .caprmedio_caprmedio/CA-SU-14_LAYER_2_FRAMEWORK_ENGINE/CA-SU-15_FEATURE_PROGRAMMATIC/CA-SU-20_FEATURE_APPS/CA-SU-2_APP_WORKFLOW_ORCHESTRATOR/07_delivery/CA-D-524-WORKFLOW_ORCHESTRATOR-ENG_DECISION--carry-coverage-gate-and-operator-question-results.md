---
atom_id: CA-D-524
content_role: Delivery
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Active
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-27 19:59:26 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run.Coverage
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
type: Eng Decision
tier: 3
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
