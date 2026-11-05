---
atom_id: CA-R-2001@12-draft
ref_id: CA-R-2001@12-draft
role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
topics:
  main_subject: 'Formal Model::CAPRMEDIO::Continuant/Atom/Content Role: Requirement/Type: Graph Rule'
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - Subject/CAPRMEDIO/Graph/Rule
  - Subject/CAPRMEDIO/Graph/Rule.Type
version: 12
updated_at: 2026-10-28 19:24:50 +0400
tier: 1
form: Definition
container:
  scope_unit: CA-SU-11
---
# Summary

Define Atom/Content Role: Requirement/Type: Graph Rule

## Claim scope

Requirement Atoms of Type Graph Rule.

## Claim

Graph Rule means the Requirement Type whose one content.claim states one fully formal condition on graph structure. The containing Atom has Content Role Requirement and Type Graph Rule. Its Claim is one complete fenced YAML block under ## Claim, not a claim mapping in frontmatter and not a second prose statement.

## Semantics

The parsed Claim mapping has one graph_rule_type selecting its formal shape, plus the applicability and condition fields admitted by that Type's schema. Atom Type and graph_rule_type remain different properties. Summary is required; Claim scope, Semantics and Details are optional supporting sections in the RMED layout. They do not duplicate, add to or override the operative condition.

## Details

CA-D-637 carries the revised representation. The six existing Graph Rule forms and their source meanings are retained. This Draft does not add an evaluator, schema, precedence rule or runtime support.

Superseded preparation: CA-A-1242 removes the special Graph Rule branch and Atom Type. Do not promote this legacy Graph Rule packet entry as written. Preserve its useful formal constraints/schema evidence for incorporation into the appropriate Definition Claims; no Current rule or predecessor is deleted by this marker.
