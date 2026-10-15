---
subjects:
  governs: "Journal"
  depends_on:
    ["Journal.Record"]
version: 12
updated_at: "2026-10-15 12:18:08 +0000"
relations: {}
atom_id: "CA-D-308"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Serialize Journals as Append-Only Carriers

## Scope

Journal Carriers.

## Claim

**every** Journal Carrier **must** serialize its ordered Records append-only **in** its registered format **and** **must not** rewrite an admitted Record.

## Details
