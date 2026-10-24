---
subjects:
  governs: Subject/Graph/Relation
  depends_on:
  - atom-boundary
version: 18
updated_at: 2026-10-23 03:06:32 +0400
relations:
  child_of:
  - CA-R-1756
atom_id: CA-R-1659@18
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
status: Archived
author: Anatoly Maslennikov
global_tier: 11
---
# Summary

Derive inverse structural ownership

## Scope

the inverse `structural_children` view derived from stored `structural_parent` relations.

## Claim

CAPRMEDIO **must** derive the inverse `structural_children` view from stored `structural_parent` relations **and** **must not** persist that inverse separately.

## Details
