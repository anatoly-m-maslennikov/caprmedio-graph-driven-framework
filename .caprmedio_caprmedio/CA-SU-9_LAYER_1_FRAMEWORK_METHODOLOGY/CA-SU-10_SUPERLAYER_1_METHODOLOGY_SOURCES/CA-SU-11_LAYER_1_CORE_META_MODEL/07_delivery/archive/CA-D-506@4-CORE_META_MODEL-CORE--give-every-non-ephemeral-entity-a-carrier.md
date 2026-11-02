---
atom_id: CA-D-506@4
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Archived
version: 4
updated_at: 2026-10-23 03:14:50 +0400
author: Anatoly Maslennikov
subjects:
  governs: Non-ephemeral Entity
  depends_on:
  - Entity
  - Subject/Engineering/Carrier
  - Property
relations: {}
---
# Summary

Give every non-ephemeral Entity a Carrier

## Scope

non-ephemeral Entities.

## Claim

**every** non-ephemeral Entity **must** have **`>=1`** Carrier through its Entity/Carrier binding.

## Details

a binding **may** use a shared Carrier **or** a location within it. a carried Property does **not** require a separate file merely because it is an Entity.
