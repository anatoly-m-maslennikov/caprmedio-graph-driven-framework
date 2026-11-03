---
subjects:
  active: Entity/Object/Continuant/Actor/AI Agent
  passive:
  - Entity/Object/Continuant/Actor/AI Agent
  - Atom/(.Role := Concern)
  - Atom
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - Aspects <+ Engineering <+ Execution Control <+ Effect Authorization
  - Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
version: 28
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-R-846
  - CA-R-2158
atom_id: CA-R-1561
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Let AI Agents resolve Concerns under bounded authority

## Claim scope

AI Agent resolution of Concerns under active delegated authority.

## Claim

an identified AI Agent **may** resolve a Concern from active Atoms **when** its active Operator delegation permits **every** required action **and** resolution confidence meets the configured semantic-resolution threshold; the resolution **may** create **or** change Atoms **in** other Content Roles **only** within that same delegated authority.
