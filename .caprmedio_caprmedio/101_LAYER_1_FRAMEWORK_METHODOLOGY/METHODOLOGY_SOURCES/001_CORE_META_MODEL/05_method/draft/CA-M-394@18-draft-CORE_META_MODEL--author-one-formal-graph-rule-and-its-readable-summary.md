---
atom_id: CA-M-394@18-draft
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: 'Formal Model::CAPRMEDIO::Continuant/Atom/Content Role: Requirement/Type: Graph Rule.content.claim'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Rule.Type
  - Subject/CAPRMEDIO/Graph/Rule.Applies To
  - Subject/CAPRMEDIO/Graph/Rule.Condition
  - Subject/CAPRMEDIO/Graph/Rule.Default Value
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary
relations: {}
version: 18
updated_at: 2026-10-28 19:24:50 +0400
tier: 1
type: Implementation Method
---
# Summary

Author one formal Graph Rule and its readable Summary

## Claim scope

Authoring one formal Graph Rule Atom.

## Claim

To author a formal Graph Rule, write one independently replaceable formal mapping in one fenced yaml block under ## Claim, using the registered schema for its single graph_rule_type. Then derive the source-faithful Summary. This is one content.claim, not a frontmatter Claim plus a prose or code duplicate.

## Details

Use Atom Content Role Requirement and Type Graph Rule. Keep ordinary Atom metadata in frontmatter and the entire operative rule in the Claim block. Use the exact RMED heading order from CA-D-479. Claim scope, Semantics and Details are optional and cannot add or override an operative condition. Split independently replaceable rules into separate Atoms. Preserve the admitted Cardinality and Endpoint Constraint semantics in CA-D-637, including zero-edge cases, source-backed selection membership, numeric bounds and exact ordering operator. Do not invent schemas or infer an evaluator from successful YAML parsing. Retain the established Summary unless creating a successor identity under the Summary-change rule.

Superseded preparation: CA-A-1242 removes the special Graph Rule branch and Atom Type. Do not promote this legacy Graph Rule packet entry as written. Preserve its useful formal constraints/schema evidence for incorporation into the appropriate Definition Claims; no Current rule or predecessor is deleted by this marker.
