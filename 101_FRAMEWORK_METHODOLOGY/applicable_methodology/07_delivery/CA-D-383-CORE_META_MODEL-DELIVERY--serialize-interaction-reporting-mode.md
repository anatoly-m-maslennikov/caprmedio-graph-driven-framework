---
subjects:
  governs: "Entity/Continuant/Object/Project.Framework Settings"
  depends_on:
    ["Entity/Continuant/Object/Project.Framework Settings", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/Object/Project.Framework Settings.Interaction.Reporting Mode"]
version: 13
updated_at: "2026-10-15 18:51:45 +0000"
relations:
  child_of:
    - CA-D-361
  relates_to:
    - CA-R-1628
    - CA-R-1750
atom_id: "CA-D-383"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-383-CORE_META_MODEL-DELIVERY--serialize-interaction-reporting-mode.md
  source_atom_id: CA-D-383
  source_atom_revision: 13
  source_sha256: 4c2d7a246f545c7524ce0e06d206c251ec1b66bf626f01480f23926c4d4af2db
  original_relations_sha256: f35ab4d15e0ddafd47faf74ffa94717141e3d1f8a5764928d58928f822191627
---
# Summary

Serialize Interaction Reporting Mode

## Scope

an explicit instance reporting default **in** the Framework Instance Settings TOML Carrier.

## Claim

an explicit instance reporting default **in** the Framework Instance Settings TOML Carrier **must** use `reporting_mode` **in** the `[interaction]` section, using an allowed value governed by CA-R-1628-CORE_META_MODEL-REQUIREMENT--allow-silent-and-verbose-reporting-modes.

## Details
