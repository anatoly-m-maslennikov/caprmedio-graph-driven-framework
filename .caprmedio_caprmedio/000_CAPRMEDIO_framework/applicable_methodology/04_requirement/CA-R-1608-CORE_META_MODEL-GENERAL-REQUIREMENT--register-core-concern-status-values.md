---
atom_id: CA-R-1608
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Concern.Status"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role: Concern", "Entity/Continuant/Node/Atom.Status"]
version: 7
updated_at: "2026-10-18 03:33:45 +0400"
relations:
  relates_to:
    - CA-R-1308
    - CA-R-1313
    - CA-R-1336
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1608-CORE_META_MODEL-GENERAL-REQUIREMENT--register-core-concern-status-values.md
  source_atom_id: CA-R-1608
  source_atom_revision: 7
  source_sha256: 9be064022d3e07a3e3259f0f9c06048fe27cb94baa1861935725aacac850bd5f
  original_relations_sha256: 2c6453ce04412f942992095a079e1deae0b11a3c6fa53b60e6e419ede3b8f74c
---
# Summary

Register Core Concern Status Values

## Scope

the Core Concern Status model.

## Claim

the Core Concern Status model **must** inherit the allowed values of Atom.Status and add (Resolved, Canceled).

## Details
