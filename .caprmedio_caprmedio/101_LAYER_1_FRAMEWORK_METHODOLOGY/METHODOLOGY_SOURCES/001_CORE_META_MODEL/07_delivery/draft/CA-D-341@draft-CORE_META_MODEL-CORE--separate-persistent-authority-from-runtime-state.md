---
subjects:
  governs: "Entity/Carrier.Storage Boundary"
  depends_on:
    - "Framework-Owned Carrier"
    - "Project-Owned Carrier"
    - "Runtime State Carrier"
version: 13
updated_at: "2026-10-15 18:30:30 +0000"
relations: {}
atom_id: "CA-D-341@draft"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Separate Persistent Authority from Runtime State

## Scope

persistent Framework-Owned and Project-Owned Carriers.

## Claim

Framework-Owned **and** Project-Owned persistent Carriers **must** remain outside Runtime State so Runtime State cleanup cannot remove canonical authority **or** Journal history.

## Details
