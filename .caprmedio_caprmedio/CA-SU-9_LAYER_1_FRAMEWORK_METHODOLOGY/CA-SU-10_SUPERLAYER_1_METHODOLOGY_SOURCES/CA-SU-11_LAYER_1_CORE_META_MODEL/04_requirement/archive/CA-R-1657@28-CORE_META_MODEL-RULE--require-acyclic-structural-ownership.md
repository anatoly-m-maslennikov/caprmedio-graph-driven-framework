---
subjects:
  governs: Entity/Graph Syntax > Relation
version: 28
updated_at: 2026-10-29 07:45:27 +0400
relations: {}
atom_id: CA-R-1657@28
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Require acyclic structural ownership

## Claim scope

the directed graph formed by active `structural_parent` relations.

## Claim

the directed graph formed by active `structural_parent` relations **must** be acyclic.

## Details
