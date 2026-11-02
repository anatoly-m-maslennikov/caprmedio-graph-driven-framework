---
subjects:
  governs: Entity/Graph Syntax > Relation//IS_BORNE_BY
  depends_on:
  - Entity/Graph Syntax > Relation
  - Entity
version: 19
updated_at: 2026-10-29 07:45:26 +0400
relations: {}
atom_id: CA-R-1351@19
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Give Primary Entity Occurrences No Bearer

## Claim scope

Primary Entity occurrences referenced by a Subject.

## Claim

a Primary Entity referenced by a Subject **must** have **`=0`** IS_BORNE_BY parents.

## Details
