---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Tier
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit
  - Entity/Object/Continuant/Governing Objects/Atom.Tier
version: 9
updated_at: 2026-10-29 22:26:57 +0400
relations: {}
atom_id: CA-R-2131@9
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
type: Rule
tier: 2
status: Archived
author: Anatoly Maslennikov
---
## Summary

Admit Numeric Tiers in Non-Project Scope Units

## Claim scope

ordinary Atoms owned by non-Project Scope Units.

## Claim

a non-Project Scope Unit **must** admit an integer Tier **>=0** for every ordinary Atom it owns. Higher integer Tiers remain admissible without an upper bound and may be assigned or raised when required by the approved governing-relation ordering.

This range rule imposes no Content-Role or Type-to-Tier restriction.
