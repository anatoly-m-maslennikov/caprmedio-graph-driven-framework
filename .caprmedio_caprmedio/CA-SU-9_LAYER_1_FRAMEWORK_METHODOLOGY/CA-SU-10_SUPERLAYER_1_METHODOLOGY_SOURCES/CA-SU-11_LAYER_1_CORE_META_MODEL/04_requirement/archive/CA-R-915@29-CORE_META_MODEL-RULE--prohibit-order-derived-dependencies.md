---
subjects:
  governs: Entity/Graph Syntax > Relation
version: 29
updated_at: 2026-10-29 10:13:49 +0400
relations:
  child_of:
  - CA-R-913
atom_id: CA-R-915@29
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
## Summary
Prohibit order-derived dependencies

## Claim scope

Dependencies between related Governed Entities.

## Claim

the Local Order of two Scope Units **or** the position of one canonical target reference **in** `relations.<RELATION_KIND>` **must not** establish **or** alter a dependency between related Governed Entities.
