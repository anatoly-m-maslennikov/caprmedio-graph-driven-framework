---
atom_id: CA-R-1999@8
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Graph/Rule.Default Value
  depends_on:
  - Subject/CAPRMEDIO/Graph/Rule
  - Subject/CAPRMEDIO/Graph/Rule.Condition
relations: {}
version: 8
updated_at: 2026-10-29 07:45:28 +0400
tier: 1
type: Entity Definition
---
## Summary

Define Entity/Graph Rule.Default Value

## Claim scope

The optional fallback value associated with a Graph Rule.

## Claim

Graph Rule.Default Value **means** an optional fallback used when the corresponding value is absent, without replacing an explicit value and subject to the applicable constraints.

## Details

The property is optional. Selecting a default does not automatically write or materialize that value. This definition supplies no concrete default, cross-rule precedence, merge behavior, or override policy.
