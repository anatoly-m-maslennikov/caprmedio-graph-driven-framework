---
atom_id: CA-R-1995@6
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph/Rule
  depends_on:
  - Subject/Graph/Relation
  - Entity/Node
relations: {}
version: 6
updated_at: 2026-10-24 01:37:42 +0400
tier: 1
type: Definition
---
# Summary

Define Entity/Graph Rule

## Scope

Graph-model conditions in the Entity model.

## Claim

a Graph Rule **means** a condition or constraint on the graph model, concerning Nodes, Relations, their properties, endpoints or cardinality.

## Details

An ordinary RMED instruction is not automatically a Graph Rule. The model has Type, Applies To, Condition and optional Default Value properties. Each rule has exactly one Graph Rule Type. CA-M-394 governs formal YAML authoring and the readable Summary; CA-D-637 declares the separate operative YAML block and the approved whitelist schema. This definition does not select unspecified whitelist combinations, unknown Relation Type handling, blacklist precedence, concrete defaults or override policies.
