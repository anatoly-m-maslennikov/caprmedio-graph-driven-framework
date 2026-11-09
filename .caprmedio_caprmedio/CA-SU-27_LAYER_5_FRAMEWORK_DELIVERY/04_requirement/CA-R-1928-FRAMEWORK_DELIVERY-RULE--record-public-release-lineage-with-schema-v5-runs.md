---
atom_id: CA-R-1928
ref_id: CA-R-1928
container:
  scope_unit: CA-SU-27
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
tier: 3
status: Active
version: 10
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-R-1928-FRAMEWORK_DELIVERY-RULE--record-public-release-lineage-with-schema-v5-runs.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/04_requirement
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
relations: {}
---

# Summary

Record public-release lineage with schema-v5 Runs

## Scope

the Journal evidence of one public-release execution.

## Claim

**the Operator** **must** record actual Workflow, Step, and Action Runs with schema-v5 parentage and attach each Tool-call input, result, effect, and report reference to its parent Step and Action evidence.

## Details

This Claim introduces no Tool Run type and no independent Journal schema. Preview, rejection, or absent recording evidence does not manufacture a Run or a successful public effect.
