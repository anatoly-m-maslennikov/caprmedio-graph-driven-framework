---
atom_id: CA-R-1997
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Rule.Applies To
  depends_on:
  - Entity/Graph Rule
  - Entity/Relation
  - Entity/Node
relations: {}
version: 1
updated_at: "2026-10-19 21:55:41 +0400"
---
# Summary

Define Entity/Graph Rule.Applies To

## Scope

The applicability of a Graph Rule in the Entity model.

## Claim

Graph Rule.Applies To **means** the structured identification of the Relation Type, property or Node kind whose cases the rule governs.

## Details

For a whitelist, Applies To selects the Relation Type whose source and target endpoints are checked against the corresponding condition lists. A whitelist expresses allowed connections for that Relation Type; it does not make other Relation Types prohibited merely because a Node appears in a listed endpoint kind. This definition does not establish applicability encoding for the other Graph Rule Types.
