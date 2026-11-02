---
subjects:
  governs: "Entity/Continuant/Object/Project.Framework Settings.Framework Control-Root Locator"
  depends_on:
    ["Entity/Continuant/Object/Project.Framework Settings", "Entity/Continuant/Object/Project", "Entity/Carrier/Directory Carrier"]
version: 10
updated_at: "2026-10-15 18:51:36 +0000"
relations:
  child_of:
    - "CA-D-361"
atom_id: "CA-D-370"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize the framework control-root locator

## Scope

the framework control-root locator for a Project in the Framework Instance Settings TOML Carrier.

## Claim

the Framework Instance Settings TOML Carrier **must** encode the framework control-root locator for its Project, resolving **to** the Directory Carrier prescribed by CA-D-317 **without** selecting a different authority root.

## Details
