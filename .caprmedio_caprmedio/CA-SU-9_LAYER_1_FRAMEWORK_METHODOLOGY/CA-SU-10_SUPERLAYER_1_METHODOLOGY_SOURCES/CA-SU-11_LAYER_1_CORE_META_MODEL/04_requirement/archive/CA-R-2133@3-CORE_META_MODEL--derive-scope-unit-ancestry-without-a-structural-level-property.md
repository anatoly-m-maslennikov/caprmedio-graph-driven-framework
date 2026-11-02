---
subjects:
  governs: Subject/Domain/Node/Continuant/Scope Unit.Path
  depends_on:
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Scope Unit.Parent
  - Subject/Domain/Node/Continuant/Scope Unit.Children
  - Subject/Domain/Node/Continuant/Project.Structure
version: 3
updated_at: 2026-10-24 10:48:25 +0400
relations:
  child_of:
  - CA-R-1764
atom_id: CA-R-2133@3
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 2
status: Archived
author: Anatoly Maslennikov
---
# Summary

Derive Scope Unit Ancestry Without a Structural-Level Property

## Scope

authoritative Scope Unit ancestry and its optional non-authoritative readability projections.

## Claim

Scope Unit ancestry **must** be derived from the authoritative Project Structure parent declarations and their corresponding stored structural-parent relations. CAPRMEDIO **must not** author or persist a Structural Level property for a Scope Unit. A displayed ancestry depth or path segment, **when** materialized for readability, is derived from that parent chain only; it **must not** establish, replace, or override parentage, ownership, or authority, and unresolved or conflicting inputs remain unresolved.

## Details
