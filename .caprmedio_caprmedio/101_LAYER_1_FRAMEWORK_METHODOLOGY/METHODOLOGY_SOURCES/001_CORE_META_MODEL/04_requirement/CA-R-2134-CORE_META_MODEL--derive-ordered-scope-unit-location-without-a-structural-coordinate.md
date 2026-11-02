---
subjects:
  active: Scope Unit.Path
  passive:
  - Scope Unit
  - Scope Unit.Path
  - Scope Unit.Local Order
  - 'Entity/Object/Continuant/Structural Unit/Scope Unit/Type: Ordered'
version: 10
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-2530
  - CA-R-2529
atom_id: CA-R-2134
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 2
status: Active
role: Requirement
form: Rule
---
## Summary

Derive Ordered Scope Unit Location Without a Structural Coordinate

## Claim scope

derived location of an Ordered Scope Unit.

## Claim

An Ordered Scope Unit's readable location **must** be derived from its authoritative Structural Path and applicable Local Order. CAPRMEDIO **must not** author or persist a Structural Coordinate property, and no displayed location or navigation token may establish parentage, sibling order, ownership, or Atom authority. Local Order remains the position among ordered siblings with one direct parent; ancestry remains the parent-chain fact.
