---
atom_id: CA-R-1943
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Node/Projection.ID"
  depends_on: ["Entity/Continuant/Node/Projection", "Entity/Continuant/Node/Projection/Type", "Entity/Continuant/Node/Selection"]
version: 4
updated_at: "2026-10-18 03:34:00 +0400"
relations:
  depends_on: [CA-R-1746]
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1943-CORE_META_MODEL-REQUIREMENT--give-each-projection-a-stable-id.md
  source_atom_id: CA-R-1943
  source_atom_revision: 4
  source_sha256: 455da723aca1c90c47b1e77ad6cbd780ce97567b770c3633e8c53f3fd9539b3a
  original_relations_sha256: 70a0a6d3134f74ab4bfa350ad56597b6f4f39ada12828ed7451707ba65ea617e
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
