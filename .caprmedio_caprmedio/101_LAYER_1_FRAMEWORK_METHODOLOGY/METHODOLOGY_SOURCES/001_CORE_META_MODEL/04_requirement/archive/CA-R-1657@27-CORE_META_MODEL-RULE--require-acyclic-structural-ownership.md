---
subjects:
  governs: Entity/Graph Syntax > Relation
version: 27
updated_at: 2026-10-29 07:17:18 +0400
relations: {}
atom_id: CA-R-1657@27
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Require acyclic structural ownership

## Scope

the directed graph formed by active `structural_parent` relations.

## Claim

the directed graph formed by active `structural_parent` relations **must** be acyclic.

## Details
