---
subjects:
  governs: "Entity/Carrier/Directory Carrier.Name"
  depends_on:
    ["Entity/Node/Continuant/Scope Unit.Name", "Entity/Node/Continuant/Scope Unit.Label", "Entity/Node/Continuant/Scope Unit.Structural Level", "Entity/Node/Continuant/Scope Unit.Navigational Order Number", "Entity/Node/Continuant/Scope Unit.Local Order"]
version: 18
updated_at: "2026-10-19 11:45:52 +0000"
relations: {}
atom_id: "CA-D-299@draft"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize Root Delivery Directory Names

## Scope

root Delivery Directory Carriers for non-Project Scope Units **when** the default Scope Unit directory convention is used.

## Claim

**every** root Delivery Directory Carrier **must** serialize Structural Level, Navigational Order Number, **and** Scope Unit Name **and** **must not** serialize Label **or** Local Order. a declared native Carrier binding under CA-D-445 **must not** be reinterpreted through this default convention.

## Details
