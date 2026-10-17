---
subjects:
  governs: "Entity/Carrier/Directory Carrier.Name"
  depends_on:
    ["Entity/Continuant/Object/Scope Unit/Type: Ordered", "Entity/Continuant/Object/Scope Unit/Type: Unordered", "Entity/Continuant/Object/Scope Unit.Label", "Entity/Continuant/Object/Scope Unit.Local Order"]
version: 14
updated_at: "2026-10-16 12:09:16 +0000"
relations: {}
atom_id: "CA-D-298"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-298-CORE_META_MODEL--serialize-local-order-only-for-ordered-scope-unit-directories.md
  source_atom_id: CA-D-298
  source_atom_revision: 14
  source_sha256: 99a40f8aed58d665b12d706e7cb01c3968c636629aa9885edae6c823b2dfef3c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Local Order Only for Ordered Scope Unit Directories

## Scope

Scope Unit authority Directory Carrier Names that use the default Scope Unit directory convention.

## Claim

**when** the default Scope Unit directory convention is used, a Scope Unit authority Directory Carrier Name **must** serialize Local Order immediately **after** Label **only** for an Ordered Scope Unit **and** **must not** serialize Local Order for an Unordered Scope Unit. a declared native Carrier binding under CA-D-445-CORE_META_MODEL-GENERAL-DELIVERY--admit-explicit-scope-unit-carrier-bindings **must not** be reinterpreted through this default convention.

## Details
