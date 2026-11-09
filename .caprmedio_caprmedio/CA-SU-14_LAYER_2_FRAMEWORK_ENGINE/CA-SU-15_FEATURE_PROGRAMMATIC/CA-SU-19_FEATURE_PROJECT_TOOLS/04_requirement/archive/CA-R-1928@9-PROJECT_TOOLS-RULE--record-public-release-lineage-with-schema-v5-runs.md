---
atom_id: CA-R-1928@9
ref_id: CA-R-1928@9
container:
  scope_unit: CA-SU-19
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
status: Archived
version: 9
updated_at: 2026-10-27 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-1928@9-PROJECT_TOOLS-RULE--record-public-release-lineage-with-schema-v5-runs.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-19_FEATURE_PROJECT_TOOLS/04_requirement/archive
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
---
# Summary

Record public-release lineage with schema-v5 Runs

## Scope

the Journal evidence of one public-release execution.

## Claim

**the Operator** **must** record actual Workflow, Step, and Action Runs with schema-v5 parentage and attach each Tool-call input, result, effect, and report reference to its parent Step and Action evidence.

## Details

This Claim introduces no Tool Run type and no independent Journal schema. Preview, rejection, or absent recording evidence does not manufacture a Run or a successful public effect.
