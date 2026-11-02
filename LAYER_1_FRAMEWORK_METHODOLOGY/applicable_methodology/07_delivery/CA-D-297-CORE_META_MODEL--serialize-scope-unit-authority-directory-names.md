---
subjects:
  governs: "Entity/Carrier/Directory Carrier.Name"
  depends_on:
    ["Entity/Node/Continuant/Scope Unit.Name", "Entity/Node/Continuant/Scope Unit.Label", "Entity/Node/Continuant/Scope Unit.Structural Level", "Entity/Node/Continuant/Scope Unit.Navigational Order Number", "Entity/Node/Continuant/Scope Unit.Local Order"]
version: 18
updated_at: "2026-10-19 15:55:25 +0400"
relations: {}
atom_id: "CA-D-297"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-297-CORE_META_MODEL--serialize-scope-unit-authority-directory-names.md
  source_atom_id: CA-D-297
  source_atom_revision: 18
  source_sha256: 385d565058ac04dac34b62822ce07be7084d37bf69a1a22bdd9d5f209ed2df65
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Scope Unit Authority Directory Names

## Scope

Project-internal Scope Unit authority Directory Carrier Names that use the default Scope Unit directory convention.

## Claim

**when** the default Scope Unit directory convention is used, **every** Project-internal Scope Unit authority Directory Carrier Name **must** serialize Structural Level, Navigational Order Number, Label, applicable Local Order, **and** Scope Unit Name **in** that order. a declared native Carrier binding under CA-D-445-CORE_META_MODEL-GENERAL-DELIVERY--admit-explicit-scope-unit-carrier-bindings **must not** be reinterpreted through this default convention.

## Details
