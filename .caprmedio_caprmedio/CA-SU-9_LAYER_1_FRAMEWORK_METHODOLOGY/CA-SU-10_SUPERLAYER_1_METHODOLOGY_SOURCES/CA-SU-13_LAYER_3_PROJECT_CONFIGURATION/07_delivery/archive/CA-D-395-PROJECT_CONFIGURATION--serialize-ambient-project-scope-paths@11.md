---
subjects:
  governs: "Entity/Carrier"
  depends_on:
    ["Entity/Continuant/Node/Project", "Entity/Continuant/Node/Scope Unit"]
version: 11
updated_at: "2026-10-18 07:18:25 +0400"
relations: {}
atom_id: "CA-D-395"
content_role: "Delivery"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "Standard"
status: "Active"
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
