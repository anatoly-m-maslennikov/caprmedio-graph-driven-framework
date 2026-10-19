---
subjects:
  governs: "Atom Carrier.Filename.Scope Unit Token"
  depends_on:
    ["Entity/Continuant/Object/Scope Unit.Name", "Project Configuration"]
version: 15
updated_at: "2026-10-15 18:51:06 +0000"
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
  source_atom_revision: 15
  source_sha256: 0649d97cfa856736f7aecfda23d329fd556d08ce47ad5afc1ca9d6eb58c5a2d6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary
Serialize Scope Unit References as Filename Tokens

## Scope
Scope Unit references serialized **in** Atom filenames.

## Claim

**every** Scope Unit reference serialized **in** an Atom filename **must** use **`=1`** stable uppercase token selected from its Scope Unit Name by Project Configuration.

## Details
