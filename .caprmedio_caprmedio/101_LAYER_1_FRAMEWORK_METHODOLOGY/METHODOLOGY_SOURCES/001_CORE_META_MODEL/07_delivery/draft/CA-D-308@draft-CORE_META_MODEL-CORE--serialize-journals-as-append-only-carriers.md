---
subjects:
  governs: "Entity/Node/Continuant/History/Journal"
  depends_on:
    ["Entity/Node/Continuant/History/Journal.Record"]
version: 15
updated_at: "2026-10-19 11:46:01 +0000"
relations: {}
atom_id: "CA-D-308@draft"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
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
