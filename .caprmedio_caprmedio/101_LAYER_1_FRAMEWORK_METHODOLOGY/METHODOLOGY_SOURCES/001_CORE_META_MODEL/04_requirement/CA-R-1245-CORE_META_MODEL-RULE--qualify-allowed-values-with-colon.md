---
subjects:
  governs: Subject
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Relation/Type: IS_ALLOWED_VALUE_OF'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Property
version: 21
updated_at: 2026-10-27 19:59:52 +0400
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
# Summary

Qualify Allowed Values with Colon

## Scope

IS_ALLOWED_VALUE_OF relations in a Subject Expression.

## Claim

**in** a Subject Expression, `:` **must** express **only** one IS_ALLOWED_VALUE_OF relation from the following value **to** the immediately preceding Property occurrence.

## Details
