---
subjects:
  governs: Subject
  depends_on:
  - 'Subject/Graph/Relation/Type: IS_ALLOWED_VALUE_OF'
  - Subject/Domain/Node/Continuant/Term//Property
version: 19
updated_at: 2026-10-24 11:58:20 +0400
relations: {}
atom_id: CA-R-1245@19
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
