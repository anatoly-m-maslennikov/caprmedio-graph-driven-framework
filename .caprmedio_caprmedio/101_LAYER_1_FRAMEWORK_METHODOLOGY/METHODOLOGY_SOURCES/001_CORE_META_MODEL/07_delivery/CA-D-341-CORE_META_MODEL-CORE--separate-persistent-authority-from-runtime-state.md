---
subjects:
  governs: Subject/Engineering/Carrier
  depends_on:
  - Subject/Domain/Node/Continuant/History
version: 20
updated_at: 2026-10-24 01:37:42 +0400
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

