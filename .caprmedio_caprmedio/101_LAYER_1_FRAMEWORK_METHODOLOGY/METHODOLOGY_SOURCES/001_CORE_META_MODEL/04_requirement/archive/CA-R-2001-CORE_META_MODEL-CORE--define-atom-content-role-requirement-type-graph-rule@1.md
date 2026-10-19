---
atom_id: CA-R-2001
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Graph Rule'
  depends_on:
  - 'Entity/Node/Continuant/Atom/Content Role: Requirement'
  - Entity/Graph Rule
  - Entity/Graph Rule.Type
relations: {}
version: 1
updated_at: "2026-10-20 00:25:38 +0400"
---
# Summary

Define Atom/Content Role: Requirement/Type: Graph Rule

## Scope

The Graph Rule value in the qualified Requirement Type domain.

## Claim

Graph Rule **means** the Requirement Type whose operative Substance states one formal condition or constraint on graph structure, including Nodes, Relations, their properties, endpoints or cardinality.

## Details

This specific Requirement Type is distinct from the generic Rule Type defined by CA-R-2000; it is not a generic Subtype. The containing Atom's frontmatter Type is Graph Rule. Its one operative graph_rule_type selects the Graph Rule's form under CA-R-1996; these are different properties. CA-M-394 governs authoring and CA-D-637 carries the Summary and fenced operative YAML body. The governed Subject identifies the structure constrained by the rule, not an extra authoritative Rule instance. Ordinary model definitions are not Graph Rule instances and remain in their currently admitted prose carrier. This definition does not register runtime support, retype existing Atoms, add a rule evaluator or supply missing Type schemas.
