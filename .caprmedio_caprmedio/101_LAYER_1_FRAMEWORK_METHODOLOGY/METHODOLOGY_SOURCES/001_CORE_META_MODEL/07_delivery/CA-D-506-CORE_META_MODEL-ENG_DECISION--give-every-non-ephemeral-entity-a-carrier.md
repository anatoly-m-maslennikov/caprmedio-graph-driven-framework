---
atom_id: CA-D-506
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
version: 13
updated_at: 2026-10-27 19:59:26 +0400
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node
  depends_on:
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Property
relations: {}
tier: 1
type: Eng Decision
---
# Summary

Give every non-ephemeral Entity a Carrier

## Scope

non-ephemeral Entities.

## Claim

**every** non-ephemeral Entity **must** have **`>=1`** Carrier through its Entity/Carrier binding.

## Details

a binding **may** use a shared Carrier **or** a location within it. a carried Property does **not** require a separate file merely because it is an Entity.
