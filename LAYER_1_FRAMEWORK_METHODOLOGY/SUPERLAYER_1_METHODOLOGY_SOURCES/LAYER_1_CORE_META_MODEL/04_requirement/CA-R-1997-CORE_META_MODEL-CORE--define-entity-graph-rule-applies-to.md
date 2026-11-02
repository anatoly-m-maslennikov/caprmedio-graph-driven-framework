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
version: 3
updated_at: "2026-10-20 13:46:55 +0400"
---
# Summary

Define Entity/Graph Rule.Applies To

## Scope

The applicability of a Graph Rule in the Entity model.

## Claim

Graph Rule.Applies To **means** the structured identification of the Relation Type, property or Node kind whose cases the rule governs.

## Semantics

The named Selection `Entity/Node/Continuant/Selection//Dependent Entity Occurrences` means all Entity occurrences whose governing source declarations require bearer dependence. Determine membership from those declarations, not from the presence of IS_BORNE_BY edges in a possibly incomplete view. This is a named Selection, not a Dependent Entity kind or new taxonomy branch.

## Details

For a whitelist, Applies To selects the Relation Type whose source and target endpoints are checked against the corresponding condition lists. A whitelist expresses allowed connections for that Relation Type; it does not make other Relation Types prohibited merely because a Node appears in a listed endpoint kind. For Cardinality, Applies To identifies the source-backed node kind or named Selection whose members are each checked, the counted Relation Type and the incoming or outgoing direction. Selection membership comes from governing source declarations independently of matching edges present; zero-edge members remain included. An unknown or incomplete domain remains unresolved, not an empty passing set. CA-D-637 defines the encoding. This definition does not establish applicability encoding for the remaining Graph Rule Types or add a resolver or evaluator.
