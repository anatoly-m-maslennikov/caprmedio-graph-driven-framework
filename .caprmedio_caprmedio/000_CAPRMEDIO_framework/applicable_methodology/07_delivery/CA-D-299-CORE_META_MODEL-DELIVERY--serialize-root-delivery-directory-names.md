---
subjects:
  governs: "Entity/Carrier/Directory Carrier.Name"
  depends_on:
    ["Entity/Continuant/Object/Scope Unit.Name", "Entity/Continuant/Object/Scope Unit.Label", "Entity/Continuant/Object/Scope Unit.Structural Level", "Entity/Continuant/Object/Scope Unit.Navigational Order Number", "Entity/Continuant/Object/Scope Unit.Local Order"]
version: 14
updated_at: "2026-10-16 12:09:16 +0000"
relations: {}
atom_id: "CA-D-299"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-299-CORE_META_MODEL-DELIVERY--serialize-root-delivery-directory-names.md
  source_atom_id: CA-D-299
  source_atom_revision: 14
  source_sha256: a7865440da4b881be0de7e1fd919dd98a366c038b57b2d358acea964df468bbf
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Root Delivery Directory Names

## Scope

root Delivery Directory Carriers for non-Project Scope Units **when** the default Scope Unit directory convention is used.

## Claim

**every** root Delivery Directory Carrier **must** serialize Structural Level, Navigational Order Number, **and** Scope Unit Name **and** **must not** serialize Label **or** Local Order. a declared native Carrier binding under CA-D-445 **must not** be reinterpreted through this default convention.

## Details
