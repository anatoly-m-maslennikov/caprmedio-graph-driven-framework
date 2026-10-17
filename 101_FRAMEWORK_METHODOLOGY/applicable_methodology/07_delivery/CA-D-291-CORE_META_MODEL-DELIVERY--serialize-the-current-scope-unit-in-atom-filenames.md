---
subjects:
  governs: "Entity/Continuant/Object/Atom.Owning Scope Unit"
  depends_on:
    ["Entity/Continuant/Object/Atom.Owning Scope Unit", "Entity/Continuant/Object/Scope Unit"]
version: 18
updated_at: "2026-10-16 12:09:14 +0000"
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
  source_atom_revision: 18
  source_sha256: 10760e26d51b0943019baf2c7cae606b6613e00041b29a45464fdf10866d996d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize the Current Scope Unit in Atom Filenames

## Scope

Project-owned Atom filenames for Carriers contained **in** Scope Units.

## Claim

**every** Project-owned Atom filename **must** serialize the Scope Unit that **contains** its authoritative Carrier **`=1`** time **and** **must** omit that segment **if** the Carrier is **in** the Project Scope Unit.

## Details
