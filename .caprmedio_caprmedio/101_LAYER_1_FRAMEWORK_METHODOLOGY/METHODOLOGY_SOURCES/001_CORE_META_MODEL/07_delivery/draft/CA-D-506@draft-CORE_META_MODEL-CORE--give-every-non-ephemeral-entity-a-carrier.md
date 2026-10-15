---
atom_id: "CA-D-506@draft"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
global_tier: 9
status: "Draft"
version: 2
updated_at: "2026-10-15 12:06:44 +0000"
author: "Anatoly Maslennikov"
subjects:
  governs: "Non-ephemeral Entity"
  depends_on:
    - "Entity"
    - "Carrier"
    - "Property"
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
