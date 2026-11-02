---
subjects:
  governs: "Entity/Node/Continuant/Projection/Type: Entities Graph"
  depends_on:
    ["Entity/Node/Continuant/Projection", "Entity", "Relation Kind", "Entity/Relation", "CAPRMEDIO Graph"]
version: 10
updated_at: "2026-10-19 15:53:05 +0400"
relations: {}
atom_id: "CA-R-1438"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1438-CORE_META_MODEL-CORE--define-entities-graph.md
  source_atom_id: CA-R-1438
  source_atom_revision: 10
  source_sha256: 1ef2f26423324cc5b28bbce2a09befee2d22b58dd24f1a967d474f0c8cf5733f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Entities Graph

## Scope

the Entities Graph Type value under Projection.

## Claim

Entities Graph **means** the Type value under Projection whose instances are derived CAPRMEDIO Graphs with native Entity nodes **and** edges representing Relations admitted for that graph kind by their governing authority. their represented facts retain their appropriate source authority under CA-R-1746.

admitted external graph **or** source references under CA-R-1472 do **not** become native Entity nodes merely by being referenced. those references retain their own endpoint classes **and** graph-qualified Relation authority.

## Details
