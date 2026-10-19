---
subjects:
  governs: "Entity/Carrier/File Carrier.Filename"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Demand.Target Scope Unit"]
version: 16
updated_at: "2026-10-19 11:45:51 +0000"
relations: {}
atom_id: "CA-D-287@draft"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize Demand Type and Producer Scope

## Scope

Demand Atom filenames.

## Claim

**every** Demand Atom filename **must** serialize its Type **and** Producer Scope as `DEMANDS_FROM-<PRODUCER_SCOPE>`.

## Details
