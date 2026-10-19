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
version: 2
updated_at: "2026-10-20 00:26:28 +0400"
---
# Summary

Define Entity/Graph Rule.Type

## Scope

The Type property of a Graph Rule in the Entity model.

## Claim

Graph Rule.Type **means** the single-valued form of a Graph Rule, selected from Whitelist, Blacklist, Cardinality, Value Constraint, Topology Constraint and Endpoint Constraint.

## Details

Each Graph Rule has exactly one Graph Rule Type, distinct from the containing Atom's Requirement Type (Graph Rule). CA-D-637 carries this operative form as graph_rule_type in the fenced YAML body, not as a second Atom Type or generic Subtype. Whitelist identifies allowed endpoint kinds; Blacklist identifies banned endpoint kinds; Cardinality bounds matching connection counts per node; Value Constraint restricts property presence, value type, allowed values or range; Topology Constraint restricts graph shape, such as self-links or cycles; Endpoint Constraint restricts a relationship between endpoints, such as membership in the same Scope Unit. These describe the six forms, not six Requirement Types or complete executable schemas. Independent rules requiring different Types belong in separate Atoms.
