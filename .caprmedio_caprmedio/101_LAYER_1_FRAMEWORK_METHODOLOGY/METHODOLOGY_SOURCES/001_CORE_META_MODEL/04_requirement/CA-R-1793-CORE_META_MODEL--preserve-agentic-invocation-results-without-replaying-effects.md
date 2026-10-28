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
atom_id: CA-R-1793
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Preserve Agentic Invocation results **without** replaying effects

## Scope

repeated delivery **or** reconnection for an Agentic Step Invocation.

## Claim

the receiving context **must** report actual results against the identified Invocation. redelivery **or** reconnection **must not** imply permission **to** repeat already performed effects.

## Details
