---
atom_id: CA-R-1965
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Node/Continuant/Projection/Type: Direct Relation Registry"
relations:
  child_of:
  - CA-R-1746
version: 3
updated_at: "2026-10-19 15:54:12 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1965-CORE_META_MODEL--define-entity-continuant-projection-type-direct-relation-registry.md
  source_atom_id: CA-R-1965
  source_atom_revision: 3
  source_sha256: 5e101e8380239d2a3d466defd0057ac908952ae3809bc622a916007e9e64699b
  original_relations_sha256: cf9cb3753811b7df14cb3d6471a1dbb7c105ba4c7887af180d314140d5f5514f
---
# Summary

Define Entity/Continuant/Projection/Type: Direct Relation Registry

## Scope

Direct Relation Registry Projections.

## Claim

a Direct Relation Registry **means** a non-authoritative Projection of admitted Relation Kinds and their governing metadata, grouped by owning graph kind and traceable to their governing sources.

## Details

CA-M-120 specifies compilation of this Projection. CA-R-806 supplies required Relation Kind metadata, CA-R-1246 its graph ownership and CA-R-1437 its source-authority distinction. These rules support the kind but do not provide its R definition. This draft adds no registry workflow or independently authored authority.
