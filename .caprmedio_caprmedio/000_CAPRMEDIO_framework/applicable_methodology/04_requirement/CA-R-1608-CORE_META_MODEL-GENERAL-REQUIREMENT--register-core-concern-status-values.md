---
atom_id: CA-R-1608
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Concern.Status"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Concern", "Entity/Continuant/Object/Atom.Status"]
version: 5
updated_at: "2026-10-15 18:45:00 +0000"
relations:
  relates_to:
    - CA-R-1308
    - CA-R-1313
    - CA-R-1336
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1608-CORE_META_MODEL-GENERAL-REQUIREMENT--register-core-concern-status-values.md
  source_atom_id: CA-R-1608
  source_atom_revision: 5
  source_sha256: b1b21b03fd1e58169979b2e379c45e1fa22b8aa32759ca21bdb68c9779526151
  original_relations_sha256: 2c6453ce04412f942992095a079e1deae0b11a3c6fa53b60e6e419ede3b8f74c
---
# Summary

Register Core Concern Status Values

## Scope

`Atom/Content Role: Concern/Status`.

## Claim

the Core allowed values of `Atom/Content Role: Concern/Status` **must** be exactly (`draft`, `active`, `resolved`, `canceled`).

## Details
