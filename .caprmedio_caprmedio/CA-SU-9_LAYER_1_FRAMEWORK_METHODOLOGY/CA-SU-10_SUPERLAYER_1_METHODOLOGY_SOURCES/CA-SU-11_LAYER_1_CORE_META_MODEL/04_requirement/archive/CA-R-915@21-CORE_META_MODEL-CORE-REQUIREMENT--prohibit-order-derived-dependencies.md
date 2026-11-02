---
subjects:
  governs: Subject/Graph/Relation
version: 21
updated_at: 2026-10-24 01:37:42 +0400
relations:
  child_of:
  - CA-R-913
atom_id: CA-R-915@21
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary
Prohibit order-derived dependencies

## Scope

Dependencies between related Governed Entities.

## Claim

the Local Order of two Scope Units **or** the position of one canonical target reference **in** `relations.<RELATION_KIND>` **must not** establish **or** alter a dependency between related Governed Entities.

## Details
