---
subjects:
  governs: Entity/Graph Syntax > Relation//IS_BORNE_BY
  depends_on:
  - Entity/Graph Syntax > Relation
  - Entity
version: 18
updated_at: 2026-10-29 07:17:16 +0400
relations: {}
atom_id: CA-R-1351@18
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
