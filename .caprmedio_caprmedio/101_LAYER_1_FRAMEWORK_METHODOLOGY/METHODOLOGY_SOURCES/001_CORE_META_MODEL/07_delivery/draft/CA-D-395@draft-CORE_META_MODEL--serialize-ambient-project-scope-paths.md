---
subjects:
  governs: "Entity/Carrier"
  depends_on:
    ["Entity/Node/Continuant/Project", "Entity/Node/Continuant/Scope Unit"]
version: 13
updated_at: "2026-10-19 11:46:46 +0000"
relations: {}
atom_id: "CA-D-395@draft"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize Ambient Project Scope Paths

## Scope

the `scope_path` encoding of a Carrier.

## Claim

a Carrier encoding of `scope_path` **must** omit the ambient current Project **and** use an empty path for Project Scope.

## Details
