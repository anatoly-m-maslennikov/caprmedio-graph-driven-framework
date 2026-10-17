---
subjects:
  governs: "Entity/Continuant/Projection/Type: Terms Graph"
  depends_on:
    ["Entity/Continuant/Projection", "Entity/Continuant/Term", "Relation Kind", "Entity/Continuant/Object/Relation", "CAPRMEDIO Graph"]
version: 14
updated_at: "2026-10-15 18:41:54 +0000"
relations: {}
atom_id: "CA-R-1335"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1335-CORE_META_MODEL-CORE-REQUIREMENT--define-terms-graph.md
  source_atom_id: CA-R-1335
  source_atom_revision: 14
  source_sha256: cc5f7db6446290fdf993c5138a5c3d17b703bee6047f5163a2d8ffe22e40ae0c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Terms Graph

## Scope

Terms Graph projections **and** their represented graph facts.

## Claim

Terms Graph **means** the Type value under Projection whose instances are derived CAPRMEDIO Graphs with native Term nodes **and** edges representing Relations admitted for that graph kind by their governing authority. their represented facts retain their appropriate source authority under CA-R-1746.

## Details

admitted external graph **or** source references under CA-R-1472 do **not** become native Term nodes merely by being referenced. those references retain their own endpoint classes **and** graph-qualified Relation authority.
