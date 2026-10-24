---
atom_id: CA-R-1943@8
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Domain/Node/Continuant/Projection.ID
  depends_on:
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Domain/Node/Continuant/Projection/Type
  - Subject/Domain/Node/Continuant/Selection
version: 8
updated_at: 2026-10-24 00:38:25 +0400
relations:
  depends_on:
  - CA-R-1746
tier: 3
---
# Summary

Give each Projection a stable ID

## Scope

Projection identity across rebuilds.

## Claim

Every Projection has one Projection ID. The same Projection Type, named source selection and source of truth identify the same Projection and keep the same ID across rebuilds.

## Details

- A different Type, named source selection or source of truth identifies a different Projection and requires a different ID.
- Changes to source contents, source Versions, the artifacts selected by the same selection, generated content or Updated At do not change the Projection ID.
- A change to the current Scope Unit name or Carrier path alone does not change the Projection ID.
- Projection ID identifies the derived view, not any source Atom. It does not make the Projection authoritative.
