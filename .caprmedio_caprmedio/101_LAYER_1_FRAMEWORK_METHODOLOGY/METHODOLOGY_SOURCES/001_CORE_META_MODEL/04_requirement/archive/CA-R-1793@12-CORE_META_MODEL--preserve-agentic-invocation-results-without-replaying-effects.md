---
subjects:
  governs: Subject/Graph Node/Domain/Occurrent/Execution/Step Run
  depends_on:
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action/Execution Kind'
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run.Execution Context
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/History/Journal
version: 12
updated_at: 2026-10-26 05:59:45 +0400
relations: {}
atom_id: CA-R-1793@12
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
