---
subjects:
  governs: Subject/Graph Node/Carrier
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Scope Unit
version: 19
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-D-395@19
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
