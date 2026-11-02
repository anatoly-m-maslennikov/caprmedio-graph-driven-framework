---
subjects:
  governs: Subject/Graph/Relation
version: 21
updated_at: 2026-10-24 01:37:42 +0400
relations:
  child_of:
  - CA-R-1756
atom_id: CA-R-1659@21
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary

Derive inverse structural ownership

## Scope

the inverse `structural_children` view derived from stored `structural_parent` relations.

## Claim

CAPRMEDIO **must** derive the inverse `structural_children` view from stored `structural_parent` relations **and** **must not** persist that inverse separately.

## Details
