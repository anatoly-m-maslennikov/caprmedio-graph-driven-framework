---
atom_id: CA-R-1995
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Rule
  depends_on:
  - Entity
  - Entity/Node
  - Entity/Relation
relations: {}
version: 2
updated_at: "2026-10-19 22:01:16 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1995-CORE_META_MODEL-CORE--define-entity-graph-rule.md
  source_atom_id: CA-R-1995
  source_atom_revision: 2
  source_sha256: 8b0761a6f3b5704a06087b3050028f9f8d09127cf001805f88613f4596f63478
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Entity/Graph Rule

## Scope

Graph-model conditions in the Entity model.

## Claim

a Graph Rule **means** a condition or constraint on the graph model, concerning Nodes, Relations, their properties, endpoints or cardinality.

## Details

An ordinary RMED instruction is not automatically a Graph Rule. The model has Type, Applies To, Condition and optional Default Value properties. Each rule has exactly one Graph Rule Type. CA-M-394 governs formal YAML authoring and the readable Summary; CA-D-637 declares the separate operative YAML block and the approved whitelist schema. This definition does not select unspecified whitelist combinations, unknown Relation Type handling, blacklist precedence, concrete defaults or override policies.
