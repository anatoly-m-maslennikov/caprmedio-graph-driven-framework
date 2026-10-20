---
subjects:
  governs: "CAPRMEDIO Graph.Connectivity"
  depends_on:
    ["CAPRMEDIO Graph", "Entity/Node/Continuant/Projection", "Entity/Node/Continuant/Atom", "Structural Entity", "Entity/Node/Continuant/History/Journal", "Entity/Relation", "Relation Kind", "Relation Kind Metadata"]
version: 8
updated_at: "2026-10-19 15:53:12 +0400"
relations: {}
atom_id: "CA-R-1472"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1472-CORE_META_MODEL-GENERAL--admit-typed-secondary-graph-connections.md
  source_atom_id: CA-R-1472
  source_atom_revision: 8
  source_sha256: 75f39ab020e49c3a2ae2d31104d449a28fd410eecaa222128712795169c95b98
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Admit typed secondary graph connections

## Scope

connections represented by a secondary CAPRMEDIO Graph.

## Claim

a secondary CAPRMEDIO Graph **may** represent typed Relations between its own nodes, **to** another secondary graph **or** its nodes, **and** **to** source Atoms **or** other admitted authoritative sources.

**every** connection **must** use **`=1`** graph-qualified Relation Kind whose governing authority admits its endpoint classes, endpoint graph contexts, direction, **and** cardinality. crossing a graph boundary **must not** transfer Relation Kind ownership, import a foreign Relation Kind as native, **or** make a referenced external endpoint a native node of the receiving graph. a cross-graph reference preserves the referenced identity **without** copying its source fact into independent authority. these permissions do **not** admit concrete Relation Kinds **or** authorize inference beyond their declared rules.

## Details
