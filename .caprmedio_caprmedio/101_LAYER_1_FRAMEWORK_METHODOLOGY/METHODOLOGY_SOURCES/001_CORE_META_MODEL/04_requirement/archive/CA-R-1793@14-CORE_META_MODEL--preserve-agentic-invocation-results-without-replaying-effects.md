---
subjects:
  governs: Entity/Object/Occurrent/Execution/Step Run
  depends_on:
  - Entity/Object/Occurrent/Execution/Step Run
  - Entity/Object/Occurrent/Execution/Workflow Run
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action.Execution Kind'
  - Entity/Object/Occurrent/Execution/Step Run.Execution Context
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/History/Journal
version: 14
updated_at: 2026-10-29 07:17:19 +0400
relations: {}
atom_id: CA-R-1793@14
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
