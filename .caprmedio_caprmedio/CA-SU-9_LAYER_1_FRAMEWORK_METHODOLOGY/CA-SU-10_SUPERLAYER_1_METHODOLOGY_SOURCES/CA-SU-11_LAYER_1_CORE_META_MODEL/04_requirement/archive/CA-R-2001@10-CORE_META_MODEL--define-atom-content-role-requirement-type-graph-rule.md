---
atom_id: CA-R-2001@10
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement/Type: Graph Rule'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement'
  - Subject/Graph Rule
  - Subject/Graph Rule.Type
relations: {}
version: 10
updated_at: 2026-10-26 05:29:36 +0400
tier: 1
type: Definition
---
# Summary

Define Atom/Content Role: Requirement/Type: Graph Rule

## Scope

The Graph Rule value in the qualified Requirement Type domain.

## Claim

Graph Rule **means** the Requirement Type whose operative YAML states one formal condition or constraint on graph structure, including Nodes, Relations, their properties, endpoints or cardinality.

## Details

This specific Requirement Type is distinct from the generic Rule Type defined by CA-R-2000; it is not a generic Subtype. The containing Atom's frontmatter Type is Graph Rule. Its one operative `claim.graph_rule_type` selects the Graph Rule's form under CA-R-1996; these are different properties. CA-M-394 governs authoring and CA-D-637 carries the Summary and formal YAML Claim in frontmatter. The governed Subject identifies the structure constrained by the rule, not an extra authoritative Rule instance. A formal Graph Rule has one fully formal Claim in its YAML `claim.*` mapping, not a Substance Property or a duplicate prose Claim section. Its Summary is required; Semantics and Details are optional supporting sections under CA-D-637. Ordinary model definitions are not Graph Rule instances and remain in their currently admitted prose carrier. This definition does not register runtime support, retype existing Atoms, add a rule evaluator or supply missing Type schemas.
