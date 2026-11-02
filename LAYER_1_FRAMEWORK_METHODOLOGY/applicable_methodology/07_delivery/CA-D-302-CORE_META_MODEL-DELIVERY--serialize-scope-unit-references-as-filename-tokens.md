---
subjects:
  governs: "Atom Carrier.Filename.Scope Unit Token"
  depends_on:
    ["Entity/Node/Continuant/Scope Unit.Name", "Project Configuration"]
version: 16
updated_at: "2026-10-19 15:55:26 +0400"
relations: {}
atom_id: "CA-D-302"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-302-CORE_META_MODEL-DELIVERY--serialize-scope-unit-references-as-filename-tokens.md
  source_atom_id: CA-D-302
  source_atom_revision: 16
  source_sha256: 626b447a775f441eef6b81c426506adb2e803ec30113a62d9d7c9d51bc2e34c8
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary
Serialize Scope Unit References as Filename Tokens

## Scope
Scope Unit references serialized **in** Atom filenames.

## Claim

**every** Scope Unit reference serialized **in** an Atom filename **must** use **`=1`** stable uppercase token selected from its Scope Unit Name by Project Configuration.

## Details
