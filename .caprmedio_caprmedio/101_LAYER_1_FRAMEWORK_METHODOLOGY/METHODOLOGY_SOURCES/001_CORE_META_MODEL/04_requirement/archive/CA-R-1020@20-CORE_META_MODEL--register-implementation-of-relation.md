---
subjects:
  governs: 'Subject/Graph/Relation/Type: implementation_of'
  depends_on:
  - Subject/Graph/Relation
version: 20
updated_at: 2026-10-24 10:48:25 +0400
relations: {}
atom_id: CA-R-1020@20
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Register implementation_of relation

## Scope

the `implementation_of` direct relation owned by a governed Implementation carrier.

## Claim

`implementation_of` **must** be registered as a direct relation owned by a governed Implementation carrier **and** directed **to** **`=1`** specification Atom that the carrier implements.

## Details
