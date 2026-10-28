---
subjects:
  governs: Subject/CAPRMEDIO/Carrier
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History
version: 25
updated_at: 2026-10-27 19:59:23 +0400
relations: {}
atom_id: CA-D-341
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Eng Decision
---
# Summary

Separate Persistent Authority from Runtime State

## Scope

persistent Carriers holding canonical authority or retained history, in relation to runtime cleanup.

## Claim

runtime cleanup **must not** remove persistent Carriers holding canonical authority or retained history.

## Details

Delivery placement and retention rules must keep that content outside the cleanup target set. This protection does not require a Carrier.Ownership Class or Carrier.Storage Boundary property, and it does not classify a Carrier as disposable merely because a runtime uses it.

