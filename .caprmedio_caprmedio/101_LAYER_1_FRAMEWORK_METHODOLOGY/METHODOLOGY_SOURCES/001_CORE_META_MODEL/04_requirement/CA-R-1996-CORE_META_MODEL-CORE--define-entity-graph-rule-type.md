---
atom_id: CA-R-1996
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Rule.Type
  depends_on:
  - Entity/Graph Rule
  - 'Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Rule'
relations: {}
version: 1
updated_at: "2026-10-19 21:55:09 +0400"
---
# Summary

Define Entity/Graph Rule.Type

## Scope

The Type property of a Graph Rule in the Entity model.

## Claim

Graph Rule.Type **means** the single-valued form of a Graph Rule, selected from Whitelist, Blacklist, Cardinality, Value Constraint, Topology Constraint and Endpoint Constraint.

## Details

Each Graph Rule has exactly one Graph Rule Type, distinct from the containing Atom's Requirement Type Rule. Whitelist identifies allowed endpoint kinds; Blacklist identifies banned endpoint kinds; Cardinality bounds matching connection counts per node; Value Constraint restricts property presence, value type, allowed values or range; Topology Constraint restricts graph shape, such as self-links or cycles; Endpoint Constraint restricts a relationship between endpoints, such as membership in the same Scope Unit. These describe the six forms, not six Requirement Types or complete executable schemas. Independent rules requiring different Types belong in separate Atoms.
