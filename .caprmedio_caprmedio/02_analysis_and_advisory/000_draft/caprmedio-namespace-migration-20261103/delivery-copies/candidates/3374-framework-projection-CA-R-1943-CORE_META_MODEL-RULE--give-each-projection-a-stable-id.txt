---
atom_id: CA-R-1943
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Projection.ID
  passive:
  - CAPRMEDIO <+ MODEL <+ Projection
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Projection/Type
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Selection
version: 15
updated_at: 2026-11-02 00:18:22 +0400
relations:
  depends_on:
  - CA-R-2535
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1943-CORE_META_MODEL-RULE--give-each-projection-a-stable-id.md
  source_atom_id: CA-R-1943
  source_atom_revision: 15
  source_sha256: 73f26547342f5d87c5e96cc942f07fc881a99d184e8b2964fb88dc09ace9e350
  original_relations_sha256: 6878e685139e7f8ef4f489b6e750cc91c96c00e957ae6a05bdf9168f28ce7685
---
## Summary

Give each Projection a stable ID

## Claim scope

Projection identity across rebuilds.

## Claim

Every Projection has one Projection ID. The same Projection Type, named source selection and source of truth identify the same Projection and keep the same ID across rebuilds.

## Details

- A different Type, named source selection or source of truth identifies a different Projection and requires a different ID.
- Changes to source contents, source Versions, the artifacts selected by the same selection, generated content or Updated At do not change the Projection ID.
- A change to the current Scope Unit name or Carrier path alone does not change the Projection ID.
- Projection ID identifies the derived view, not any source Atom. It does not make the Projection authoritative.
