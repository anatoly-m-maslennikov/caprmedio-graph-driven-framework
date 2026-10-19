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
---
# Summary

Define Entity/Graph Rule

## Scope

Graph-model conditions in the Entity model.

## Claim

a Graph Rule **means** a condition or constraint on the graph model, concerning Nodes, Relations, their properties, endpoints or cardinality.

## Details

An ordinary RMED instruction is not automatically a Graph Rule. The model has Type, Applies To, Condition and optional Default Value properties. Each rule has exactly one Graph Rule Type. CA-M-394 governs formal YAML authoring and the readable Summary; CA-D-637 declares the separate operative YAML block and the approved whitelist schema. This definition does not select unspecified whitelist combinations, unknown Relation Type handling, blacklist precedence, concrete defaults or override policies.
