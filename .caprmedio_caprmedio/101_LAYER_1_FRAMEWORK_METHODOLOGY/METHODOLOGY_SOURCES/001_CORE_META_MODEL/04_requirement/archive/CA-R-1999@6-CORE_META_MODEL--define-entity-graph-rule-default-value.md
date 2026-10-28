---
atom_id: CA-R-1999@6
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph Rule.Default Value
  depends_on:
  - Subject/Graph Rule
  - Subject/Graph Rule.Condition
relations: {}
version: 6
updated_at: 2026-10-25 17:32:27 +0400
tier: 1
type: Definition
---
# Summary

Define Entity/Graph Rule.Default Value

## Scope

The optional fallback value associated with a Graph Rule.

## Claim

Graph Rule.Default Value **means** an optional fallback used when the corresponding value is absent, without replacing an explicit value and subject to the applicable constraints.

## Details

The property is optional. Selecting a default does not automatically write or materialize that value. This definition supplies no concrete default, cross-rule precedence, merge behavior, or override policy.
