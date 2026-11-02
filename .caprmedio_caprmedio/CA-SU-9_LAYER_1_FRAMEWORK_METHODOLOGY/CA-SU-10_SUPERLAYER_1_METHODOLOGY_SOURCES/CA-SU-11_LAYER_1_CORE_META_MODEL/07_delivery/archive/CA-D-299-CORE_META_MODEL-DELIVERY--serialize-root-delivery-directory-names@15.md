---
subjects:
  governs: "Entity/Carrier/Directory Carrier.Name"
  depends_on:
    ["Entity/Continuant/Node/Scope Unit.Name", "Entity/Continuant/Node/Scope Unit.Label", "Entity/Continuant/Node/Scope Unit.Structural Level", "Entity/Continuant/Node/Scope Unit.Navigational Order Number", "Entity/Continuant/Node/Scope Unit.Local Order"]
version: 15
updated_at: "2026-10-18 03:34:36 +0400"
relations: {}
atom_id: "CA-D-299"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
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
