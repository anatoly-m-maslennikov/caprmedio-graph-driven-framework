---
subjects:
  governs: "Entity/Continuant/Node/Project.Framework Settings"
  depends_on:
    ["Entity/Continuant/Node/Project.Framework Settings", "Entity/Continuant/Node/Actor/Type: Operator", "Entity/Continuant/Node/Project.Framework Settings.Interaction.Reporting Mode"]
version: 14
updated_at: "2026-10-17 23:28:04 +0000"
relations:
  child_of:
    - CA-D-361
  relates_to:
    - CA-R-1628
    - CA-R-1750
atom_id: "CA-D-383@draft"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize Interaction Reporting Mode

## Scope

an explicit instance reporting default **in** the Framework Instance Settings TOML Carrier.

## Claim

an explicit instance reporting default **in** the Framework Instance Settings TOML Carrier **must** use `reporting_mode` **in** the `[interaction]` section, using an allowed value governed by CA-R-1628-CORE_META_MODEL-REQUIREMENT--allow-silent-and-verbose-reporting-modes.

## Details
