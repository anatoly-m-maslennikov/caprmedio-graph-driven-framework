---
subjects:
  governs: "Default Settings"
  depends_on:
    ["Default Settings", "Entity/Node/Continuant/Project.Framework Settings", "Entity/Carrier"]
version: 10
updated_at: "2026-10-19 15:55:46 +0400"
relations:
  child_of:
    - "CA-D-407"
  relates_to:
    - "CA-D-361"
    - "CA-D-368"
    - "CA-D-369"
    - "CA-D-374"
    - "CA-D-383"
    - "CA-D-387"
atom_id: "CA-D-408"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-408-CORE_META_MODEL--reuse-framework-parameter-fields-in-default-settings.md
  source_atom_id: CA-D-408
  source_atom_revision: 10
  source_sha256: c8e5a009e6b7294033f8c75a396529d41abec566870e4e878392f702f2118040
  original_relations_sha256: 152b49bebf85179792750940cb8af3dc599305c49ea15d7a163894030d31f53e
---
# Summary

Reuse framework parameter fields in Default Settings

## Scope

parameter values in the Default Settings TOML Carrier.

## Claim

**every** parameter value **in** the Default Settings TOML Carrier **must** use the same registered section, field path, value type, **and** allowed domain as the corresponding explicit Framework Instance Settings parameter, **without** introducing a separate defaults-field schema.

## Details
