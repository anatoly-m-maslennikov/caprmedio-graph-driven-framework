---
atom_id: CA-R-1928
content_role: Requirement
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
version: 9
updated_at: 2026-10-27 20:00:05 +0400
relations: {}
tier: 3
type: Rule
---
# Summary

Record public-release lineage with schema-v5 Runs

## Scope

the Journal evidence of one public-release execution.

## Claim

**the Operator** **must** record actual Workflow, Step, and Action Runs with schema-v5 parentage and attach each Tool-call input, result, effect, and report reference to its parent Step and Action evidence.

## Details

This Claim introduces no Tool Run type and no independent Journal schema. Preview, rejection, or absent recording evidence does not manufacture a Run or a successful public effect.
