---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit.Path
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Path
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Local Order
  - 'Entity/Object/Continuant/Structural Unit/Scope Unit/Type: Ordered'
version: 8
updated_at: 2026-10-29 10:13:49 +0400
relations:
  child_of:
  - CA-R-1764
  - CA-R-1763
atom_id: CA-R-2134@8
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 2
status: Archived
author: Anatoly Maslennikov
---
## Summary

Derive Ordered Scope Unit Location Without a Structural Coordinate

## Claim scope

derived location of an Ordered Scope Unit.

## Claim

An Ordered Scope Unit's readable location **must** be derived from its authoritative Structural Path and applicable Local Order. CAPRMEDIO **must not** author or persist a Structural Coordinate property, and no displayed location or navigation token may establish parentage, sibling order, ownership, or Atom authority. Local Order remains the position among ordered siblings with one direct parent; ancestry remains the parent-chain fact.
