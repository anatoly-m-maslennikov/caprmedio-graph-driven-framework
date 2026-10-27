---
subjects:
  governs: 'Subject/Graph/Relation/Type: IS_BORNE_BY'
  depends_on:
  - Subject/Graph/Relation
  - Subject
version: 15
updated_at: 2026-10-25 03:48:37 +0400
relations: {}
atom_id: CA-R-1351@15
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
