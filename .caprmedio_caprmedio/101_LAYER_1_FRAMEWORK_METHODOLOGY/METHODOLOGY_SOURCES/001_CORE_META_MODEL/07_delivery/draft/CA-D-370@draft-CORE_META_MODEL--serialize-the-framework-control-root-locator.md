---
subjects:
  governs: "Entity/Node/Continuant/Project.Framework Settings.Framework Control-Root Locator"
  depends_on:
    ["Entity/Node/Continuant/Project.Framework Settings", "Entity/Node/Continuant/Project", "Entity/Carrier/Directory Carrier"]
version: 14
updated_at: "2026-10-19 11:46:22 +0000"
relations:
  child_of:
    - "CA-D-361"
atom_id: "CA-D-370@draft"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Draft"
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
