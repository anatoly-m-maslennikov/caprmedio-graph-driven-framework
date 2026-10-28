---
subjects:
  governs: Subject/CAPRMEDIO/Carrier
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
version: 20
updated_at: 2026-10-27 19:59:24 +0400
relations: {}
atom_id: CA-D-395
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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
