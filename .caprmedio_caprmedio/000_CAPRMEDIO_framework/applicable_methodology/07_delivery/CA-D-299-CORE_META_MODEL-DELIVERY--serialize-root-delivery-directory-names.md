---
subjects:
  governs: "Entity/Carrier/Directory Carrier.Name"
  depends_on:
    ["Entity/Continuant/Node/Scope Unit.Name", "Entity/Continuant/Node/Scope Unit.Label", "Entity/Continuant/Node/Scope Unit.Structural Level", "Entity/Continuant/Node/Scope Unit.Navigational Order Number", "Entity/Continuant/Node/Scope Unit.Local Order"]
version: 17
updated_at: "2026-10-18 07:30:42 +0400"
relations: {}
atom_id: "CA-D-299"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-299-CORE_META_MODEL-DELIVERY--serialize-root-delivery-directory-names.md
  source_atom_id: CA-D-299
  source_atom_revision: 17
  source_sha256: d09b48ffac63adaa9e7537f66748601b295bf15c6b1467ea650c2caf2c6d7b18
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Root Delivery Directory Names

## Scope

root Delivery Directory Carriers for non-Project Scope Units **when** the default Scope Unit directory convention is used.

## Claim

**every** root Delivery Directory Carrier **must** serialize Structural Level, Navigational Order Number, **and** Scope Unit Name **and** **must not** serialize Label **or** Local Order. a declared native Carrier binding under CA-D-445 **must not** be reinterpreted through this default convention.

## Details
