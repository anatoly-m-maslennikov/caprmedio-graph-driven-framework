---
subjects:
  governs: "Entity/Carrier/Directory Carrier.Name"
  depends_on:
    ["Entity/Node/Continuant/Scope Unit.Name", "Entity/Node/Continuant/Scope Unit.Label", "Entity/Node/Continuant/Scope Unit.Structural Level", "Entity/Node/Continuant/Scope Unit.Navigational Order Number", "Entity/Node/Continuant/Scope Unit.Local Order"]
version: 18
updated_at: "2026-10-19 11:45:52 +0000"
relations: {}
atom_id: "CA-D-297@draft"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Draft"
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
