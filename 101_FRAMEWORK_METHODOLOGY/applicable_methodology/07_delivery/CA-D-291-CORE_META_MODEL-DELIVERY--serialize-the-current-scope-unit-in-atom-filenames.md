---
subjects:
  governs: "Entity/Node/Continuant/Atom.Owning Scope Unit"
  depends_on:
    ["Entity/Node/Continuant/Atom.Owning Scope Unit", "Entity/Node/Continuant/Scope Unit"]
version: 20
updated_at: "2026-10-19 15:55:23 +0400"
relations: {}
atom_id: "CA-D-291"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-291-CORE_META_MODEL-DELIVERY--serialize-the-current-scope-unit-in-atom-filenames.md
  source_atom_id: CA-D-291
  source_atom_revision: 20
  source_sha256: 084654cc2fb8e52e8beb65ae953c6bfedabf78b2a6cf2f0232dfe3ac9a921d27
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize the Current Scope Unit in Atom Filenames

## Scope

Project-owned Atom filenames for Carriers contained **in** Scope Units.

## Claim

**every** Project-owned Atom filename **must** serialize the Scope Unit that **contains** its authoritative Carrier **`=1`** time **and** **must** omit that segment **if** the Carrier is **in** the Project Scope Unit.

## Details
