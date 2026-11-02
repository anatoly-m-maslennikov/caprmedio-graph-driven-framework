---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit.Path
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Parent
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Children
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
version: 8
updated_at: 2026-10-29 10:13:49 +0400
relations:
  child_of:
  - CA-R-1764
atom_id: CA-R-2133@8
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 2
status: Archived
author: Anatoly Maslennikov
---
## Summary

Derive Scope Unit Ancestry Without a Structural-Level Property

## Claim scope

authoritative Scope Unit ancestry and its optional non-authoritative readability projections.

## Claim

Scope Unit ancestry **must** be derived from the authoritative Project Structure parent declarations and their corresponding stored structural-parent relations. CAPRMEDIO **must not** author or persist a Structural Level property for a Scope Unit. A displayed ancestry depth or path segment, **when** materialized for readability, is derived from that parent chain only; it **must not** establish, replace, or override parentage, ownership, or authority, and unresolved or conflicting inputs remain unresolved.
