---
subjects:
  governs: "Framework Instance.Settings"
  depends_on:
    ["Framework Instance.Settings", "Projection"]
version: 21
updated_at: "2026-10-15 12:14:11 +0000"
relations: {}
atom_id: "CA-R-1631@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Configure Optional Projection Activation

## Scope

the Framework Instance Settings Artifact and registered optional Projections.

## Claim

the Framework Instance Settings Artifact **must** resolve **every** registered optional Projection as active **or** inactive, with inactive as the default **and** an unknown Type value under Projection rejected.

## Details
