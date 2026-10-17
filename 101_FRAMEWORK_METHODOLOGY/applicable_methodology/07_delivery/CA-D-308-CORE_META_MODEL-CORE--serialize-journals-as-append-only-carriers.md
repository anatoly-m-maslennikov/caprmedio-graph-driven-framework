---
subjects:
  governs: "Entity/Continuant/History/Journal"
  depends_on:
    ["Entity/Continuant/History/Journal.Record"]
version: 13
updated_at: "2026-10-15 18:51:12 +0000"
relations: {}
atom_id: "CA-D-308"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-308-CORE_META_MODEL-CORE--serialize-journals-as-append-only-carriers.md
  source_atom_id: CA-D-308
  source_atom_revision: 13
  source_sha256: 4296c88c669b97c41ca8b097fa4bc80216092f6d8ab9b5eb17b32e68b7f6673d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Journals as Append-Only Carriers

## Scope

Journal Carriers.

## Claim

**every** Journal Carrier **must** serialize its ordered Records append-only **in** its registered format **and** **must not** rewrite an admitted Record.

## Details
