---
subjects:
  governs: "Default Settings"
  depends_on:
    ["Default Settings", "Entity/Carrier/File Carrier", "Entity/Continuant/Object/Scope Unit", "Methodology Source"]
version: 11
updated_at: "2026-10-18 07:33:41 +0400"
relations:
  child_of:
    - "CA-R-1441"
atom_id: "CA-D-407"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-407-CORE_META_MODEL--store-default-settings-with-the-core-meta-model-source.md
  source_atom_id: CA-D-407
  source_atom_revision: 11
  source_sha256: eae8617c29f81198f617625ec8d3f56836ba3057352c9026158c3325e4e678de
  original_relations_sha256: adcd5f37a417426e98fa71a748e8c7ae57d289af75f231f6392f838cf84dd0f2
---
# Summary

Store Default Settings with the Core Meta-Model source

## Scope

the authoritative TOML File Carrier of the Default Settings Artifact.

## Claim

the Default Settings Artifact **must** use `caprmedio_framework_default_settings.toml` **at** the root of the CORE_META_MODEL source Scope Unit as its **`=1`** authoritative TOML File Carrier.

## Details
