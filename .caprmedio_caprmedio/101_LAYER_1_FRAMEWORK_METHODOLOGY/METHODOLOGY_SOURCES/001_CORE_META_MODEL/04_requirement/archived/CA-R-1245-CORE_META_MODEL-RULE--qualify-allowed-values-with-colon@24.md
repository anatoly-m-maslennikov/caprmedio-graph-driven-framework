---
subjects:
  governs: Entity
  depends_on:
  - Entity/Graph Syntax > Relation//IS_ALLOWED_VALUE_OF
  - Entity/Object/Continuant/Term//Property
version: 24
updated_at: 2026-10-29 10:13:48 +0400
relations: {}
atom_id: CA-R-1245
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Rule
---
## Summary

Qualify Allowed Values with Colon

## Claim scope

IS_ALLOWED_VALUE_OF relations in a Subject Expression.

## Claim

**in** a Subject Expression, `:` **must** express **only** one IS_ALLOWED_VALUE_OF relation from the following value **to** the immediately preceding Property occurrence.
