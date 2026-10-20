---
subjects:
  governs: "Graph of Graphs"
  depends_on:
    ["CAPRMEDIO Graph", "Entity/Node/Continuant/Projection", "Entity/Relation", "Relation Kind", "Single Source of Truth"]
version: 9
updated_at: "2026-10-19 15:52:59 +0400"
relations: {}
atom_id: "CA-R-1408"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1408-CORE_META_MODEL-CORE--define-graph-of-graphs.md
  source_atom_id: CA-R-1408
  source_atom_revision: 9
  source_sha256: 861b0e2818d83fe5b8411c503cd8e8bcf75e0dcf827ae36a70163ea25fc5c184
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Graph of Graphs

## Scope

Graph of Graphs compositions and any generated overview Artifact.

## Claim

a Graph of Graphs **means** a composition of CAPRMEDIO Graphs connected through graph-qualified typed references **or** shared source identities. secondary graphs **in** this composition remain Projections under CA-R-1471-CORE_META_MODEL-CORE-REQUIREMENT--keep-secondary-graphs-derived-from-source-authority, **and** their internal, cross-graph, **and** authoritative-source connections remain governed by CA-R-1472-CORE_META_MODEL-GENERAL-REQUIREMENT--admit-typed-secondary-graph-connections.

the composition does **not**, by itself, require another separately generated overview Artifact. **if** an overview is generated, its represented connections remain derived from the participating graphs **and** their sources **without** becoming another authority.

## Details
