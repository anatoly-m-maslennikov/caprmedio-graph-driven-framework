---
atom_id: CA-R-1608
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Concern.Status"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Concern", "Entity/Node/Continuant/Atom.Status"]
version: 8
updated_at: "2026-10-19 15:53:42 +0400"
relations:
  relates_to:
    - CA-R-1308
    - CA-R-1313
    - CA-R-1336
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1608-CORE_META_MODEL-GENERAL-REQUIREMENT--register-core-concern-status-values.md
  source_atom_id: CA-R-1608
  source_atom_revision: 8
  source_sha256: e66304f5d6a880354ab2cc08a586d13259c9e544c6e164dab00870f8b54ecf6f
  original_relations_sha256: 2c6453ce04412f942992095a079e1deae0b11a3c6fa53b60e6e419ede3b8f74c
---
# Summary

Register Core Concern Status Values

## Scope

the Core Concern Status model.

## Claim

the Core Concern Status model **must** inherit the allowed values of Atom.Status and add (Resolved, Canceled).

## Details
