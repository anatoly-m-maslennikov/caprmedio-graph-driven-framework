---
subjects:
  governs: "Entity/Node/Continuant/Project.Framework Settings"
  depends_on:
    ["Tool", "Extension", "Entity/Node/Continuant/Project.Framework Settings", "Default Settings"]
version: 13
updated_at: "2026-10-19 15:55:33 +0400"
relations:
  child_of:
    - CA-D-359
  relates_to:
    - CA-M-279
    - CA-D-408
atom_id: "CA-D-361"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-361-CORE_META_MODEL--serialize-framework-settings-content-in-toml.md
  source_atom_id: CA-D-361
  source_atom_revision: 13
  source_sha256: ae4d342976482d03fbf2979bb52f695865f04fb54b824522d1ed1d813a54e33d
  original_relations_sha256: c721615c7983c0a76470a5c52c89f21a22517496a3a90da9fb26001e4e66f71f
---
# Summary

Serialize Framework Settings Content in TOML

## Scope

the Framework Instance Settings TOML Carrier.

## Claim

the Framework Instance Settings TOML Carrier **must** encode explicit Operator-selected instance choices through sections **and** fields specified by Standard-tier Atoms under its Core content **and** authority boundaries **and** applicable General settings specifications; it **must not** store Project initialization inputs **or** authoritative Project Structure declarations **or** derived structural values as independently editable settings.

## Details
