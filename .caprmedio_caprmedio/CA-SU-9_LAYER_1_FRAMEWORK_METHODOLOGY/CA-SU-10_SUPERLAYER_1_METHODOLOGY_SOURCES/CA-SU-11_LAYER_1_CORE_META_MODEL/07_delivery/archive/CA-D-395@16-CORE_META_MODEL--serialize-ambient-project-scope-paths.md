---
subjects:
  governs: Subject/Engineering/Carrier
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - Subject/Domain/Node/Continuant/Scope Unit
version: 16
updated_at: 2026-10-24 01:37:42 +0400
relations: {}
atom_id: CA-D-395@16
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Serialize Ambient Project Scope Paths

## Scope

the `scope_path` encoding of a Carrier.

## Claim

a Carrier encoding of `scope_path` **must** omit the ambient current Project **and** use an empty path for Project Scope.

## Details
