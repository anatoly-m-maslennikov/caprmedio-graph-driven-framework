---
subjects:
  governs: Subject/Engineering/Carrier
  depends_on:
  - Entity/Node/Continuant/History
version: 17
updated_at: 2026-10-23 03:14:50 +0400
relations: {}
atom_id: CA-D-341@17
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
status: Archived
author: Anatoly Maslennikov
global_tier: 9
---
# Summary

Separate Persistent Authority from Runtime State

## Scope

persistent Carriers holding canonical authority or retained history, in relation to runtime cleanup.

## Claim

runtime cleanup **must not** remove persistent Carriers holding canonical authority or retained history.

## Details

Delivery placement and retention rules must keep that content outside the cleanup target set. This protection does not require a Carrier.Ownership Class or Carrier.Storage Boundary property, and it does not classify a Carrier as disposable merely because a runtime uses it.

