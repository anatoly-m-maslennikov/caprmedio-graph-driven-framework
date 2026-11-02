---
subjects:
  governs: Entity/Object/Continuant/Actor/AI Agent
  depends_on:
  - Entity/Object/Continuant/Actor/AI Agent
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Concern'
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - Entity/Aspect/Engineering/Execution Control/Effect Authorization
  - Entity/Aspect/Engineering/Execution Control/Decision Confidence
version: 23
updated_at: 2026-10-29 07:17:17 +0400
relations:
  child_of:
  - CA-R-846
  - CA-R-2158
atom_id: CA-R-1561@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Let AI Agents resolve Concerns under bounded authority

## Scope

AI Agent resolution of Concerns under active delegated authority.

## Claim

an identified AI Agent **may** resolve a Concern from active Atoms **when** its active Operator delegation permits **every** required action **and** resolution confidence meets the configured semantic-resolution threshold; the resolution **may** create **or** change Atoms **in** other Content Roles **only** within that same delegated authority.

## Details
