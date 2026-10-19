---
subjects:
  governs: "Default Settings"
  depends_on:
    ["Default Settings", "Entity/Node/Continuant/Project.Framework Settings", "Entity/Carrier"]
version: 10
updated_at: "2026-10-19 11:46:47 +0000"
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
atom_id: "CA-D-408@draft"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Reuse framework parameter fields in Default Settings

## Scope

parameter values in the Default Settings TOML Carrier.

## Claim

**every** parameter value **in** the Default Settings TOML Carrier **must** use the same registered section, field path, value type, **and** allowed domain as the corresponding explicit Framework Instance Settings parameter, **without** introducing a separate defaults-field schema.

## Details
