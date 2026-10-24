---
subjects:
  governs: Subject/Graph/Relation
  depends_on:
  - atom-boundary
version: 20
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
atom_id: CA-R-1657@20
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
---
# Summary

Require acyclic structural ownership

## Scope

the directed graph formed by active `structural_parent` relations.

## Claim

the directed graph formed by active `structural_parent` relations **must** be acyclic.

## Details
