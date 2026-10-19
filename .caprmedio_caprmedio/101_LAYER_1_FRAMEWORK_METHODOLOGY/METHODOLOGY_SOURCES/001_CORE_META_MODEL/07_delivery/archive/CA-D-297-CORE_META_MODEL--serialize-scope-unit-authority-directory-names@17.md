---
subjects:
  governs: "Entity/Carrier/Directory Carrier.Name"
  depends_on:
    ["Entity/Continuant/Node/Scope Unit.Name", "Entity/Continuant/Node/Scope Unit.Label", "Entity/Continuant/Node/Scope Unit.Structural Level", "Entity/Continuant/Node/Scope Unit.Navigational Order Number", "Entity/Continuant/Node/Scope Unit.Local Order"]
version: 17
updated_at: "2026-10-18 07:30:23 +0400"
relations: {}
atom_id: "CA-D-297"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize Scope Unit Authority Directory Names

## Scope

Project-internal Scope Unit authority Directory Carrier Names that use the default Scope Unit directory convention.

## Claim

**when** the default Scope Unit directory convention is used, **every** Project-internal Scope Unit authority Directory Carrier Name **must** serialize Structural Level, Navigational Order Number, Label, applicable Local Order, **and** Scope Unit Name **in** that order. a declared native Carrier binding under CA-D-445-CORE_META_MODEL-GENERAL-DELIVERY--admit-explicit-scope-unit-carrier-bindings **must not** be reinterpreted through this default convention.

## Details
