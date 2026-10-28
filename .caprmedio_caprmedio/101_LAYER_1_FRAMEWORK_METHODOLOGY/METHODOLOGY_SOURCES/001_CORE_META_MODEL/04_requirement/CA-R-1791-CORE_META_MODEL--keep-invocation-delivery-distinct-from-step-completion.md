---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action/Execution Kind'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run.Execution Context
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 13
updated_at: 2026-10-27 20:00:03 +0400
relations: {}
atom_id: CA-R-1791
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Keep Invocation delivery distinct from Step completion

## Scope

requests for participation **or** prompt delivery for an Agentic Step Invocation.

## Claim

requesting participation **or** returning a prompt **must not** itself complete a Step Run.

## Details
