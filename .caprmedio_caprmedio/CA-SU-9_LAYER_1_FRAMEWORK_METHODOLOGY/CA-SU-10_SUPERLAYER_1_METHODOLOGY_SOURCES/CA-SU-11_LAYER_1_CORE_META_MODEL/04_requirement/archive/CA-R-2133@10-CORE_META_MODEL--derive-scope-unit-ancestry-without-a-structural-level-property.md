---
subjects:
  active: Scope Unit.Path
  passive:
  - Scope Unit
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Parent
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Children
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
version: 10
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-2530
atom_id: CA-R-2133@10
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 2
status: Archived
role: Requirement
form: Rule
---
## Summary

Derive Scope Unit Ancestry Without a Structural-Level Property

## Claim scope

authoritative Scope Unit ancestry and its optional non-authoritative readability projections.

## Claim

Scope Unit ancestry **must** be derived from the authoritative Project Structure parent declarations and their corresponding stored structural-parent relations. CAPRMEDIO **must not** author or persist a Structural Level property for a Scope Unit. A displayed ancestry depth or path segment, **when** materialized for readability, is derived from that parent chain only; it **must not** establish, replace, or override parentage, ownership, or authority, and unresolved or conflicting inputs remain unresolved.
