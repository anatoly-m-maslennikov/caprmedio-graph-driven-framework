---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Relation/Type: IS_BORNE_BY'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Relation
  - Subject
version: 17
updated_at: 2026-10-27 19:59:53 +0400
relations: {}
atom_id: CA-R-1351
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Give Primary Entity Occurrences No Bearer

## Scope

Primary Entity occurrences referenced by a Subject.

## Claim

a Primary Entity referenced by a Subject **must** have **`=0`** IS_BORNE_BY parents.

## Details
