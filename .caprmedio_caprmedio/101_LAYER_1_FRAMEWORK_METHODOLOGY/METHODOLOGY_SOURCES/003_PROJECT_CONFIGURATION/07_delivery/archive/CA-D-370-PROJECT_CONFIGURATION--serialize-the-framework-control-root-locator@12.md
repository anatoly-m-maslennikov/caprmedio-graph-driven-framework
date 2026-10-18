---
subjects:
  governs: "Entity/Continuant/Node/Project.Framework Settings.Framework Control-Root Locator"
  depends_on:
    ["Entity/Continuant/Node/Project.Framework Settings", "Entity/Continuant/Node/Project", "Entity/Carrier/Directory Carrier"]
version: 12
updated_at: "2026-10-18 07:16:01 +0400"
relations:
  child_of:
    - "CA-D-361"
atom_id: "CA-D-370"
content_role: "Delivery"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
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
