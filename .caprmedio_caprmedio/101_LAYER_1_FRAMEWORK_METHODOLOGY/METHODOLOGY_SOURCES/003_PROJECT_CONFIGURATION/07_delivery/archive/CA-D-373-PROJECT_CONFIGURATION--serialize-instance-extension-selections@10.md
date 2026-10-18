---
subjects:
  governs: "Entity/Continuant/Object/Project.Framework Settings.Extension Selections"
  depends_on:
    ["Entity/Continuant/Object/Project.Framework Settings", "Extension"]
version: 10
updated_at: "2026-10-18 07:16:31 +0400"
relations:
  child_of:
    - "CA-D-361"
atom_id: "CA-D-373"
content_role: "Delivery"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize instance Extension selections

## Scope

the Framework Instance Settings TOML Carrier.

## Claim

the Framework Instance Settings TOML Carrier **must** encode enabled **or** disabled Extensions with selected revisions **when** applicable **and** retained per-Extension settings; retained settings **must not** activate a disabled Extension.

## Details
