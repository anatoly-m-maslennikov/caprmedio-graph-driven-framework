---
subjects:
  governs: "Entity/Continuant/Node/Project.Framework Settings.Framework Control-Root Locator"
  depends_on:
    ["Entity/Continuant/Node/Project.Framework Settings", "Entity/Continuant/Node/Project", "Entity/Carrier/Directory Carrier"]
version: 13
updated_at: "2026-10-18 07:38:32 +0400"
relations:
  child_of:
    - "CA-D-361"
atom_id: "CA-D-370"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-370-CORE_META_MODEL--serialize-the-framework-control-root-locator.md
  source_atom_id: CA-D-370
  source_atom_revision: 13
  source_sha256: a7d77b72122fcfac8b47e175afa9d89d0a6ce4e69e1d37174baad3d14101730d
  original_relations_sha256: dbd41c990ca96026d80a7c6e36e3203724208ce3569ca634233af924bbbfab2f
---
# Summary

Serialize the framework control-root locator

## Scope

the framework control-root locator for a Project in the Framework Instance Settings TOML Carrier.

## Claim

the Framework Instance Settings TOML Carrier **must** encode the framework control-root locator for its Project, resolving **to** the Directory Carrier prescribed by CA-D-317 **without** selecting a different authority root.

## Details
