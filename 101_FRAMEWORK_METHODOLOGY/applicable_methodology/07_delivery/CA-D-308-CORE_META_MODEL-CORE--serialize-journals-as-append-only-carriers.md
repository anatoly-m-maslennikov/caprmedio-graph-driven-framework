---
subjects:
  governs: "Entity/Continuant/Node/History/Journal"
  depends_on:
    ["Entity/Continuant/Node/History/Journal.Record"]
version: 14
updated_at: "2026-10-18 03:34:38 +0400"
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
  source_atom_revision: 14
  source_sha256: f83d4c2263e086b15f4c9dfe3152ac721ab7f974e3fdb6a96da9cd8e2449bf84
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Journals as Append-Only Carriers

## Scope

Journal Carriers.

## Claim

**every** Journal Carrier **must** serialize its ordered Records append-only **in** its registered format **and** **must not** rewrite an admitted Record.

## Details
