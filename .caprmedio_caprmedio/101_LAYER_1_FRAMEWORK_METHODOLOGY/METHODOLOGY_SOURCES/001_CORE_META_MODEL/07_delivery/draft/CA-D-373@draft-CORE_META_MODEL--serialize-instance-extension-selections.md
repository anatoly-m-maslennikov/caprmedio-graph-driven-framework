---
subjects:
  governs: "Framework Instance.Settings.Extension Selections"
  depends_on:
    ["Framework Instance.Settings", "Extension"]
version: 8
updated_at: "2026-10-15 12:05:54 +0000"
relations:
  child_of:
    - "CA-D-361"
atom_id: "CA-D-373@draft"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
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
