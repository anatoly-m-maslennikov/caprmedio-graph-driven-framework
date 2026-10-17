---
subjects:
  governs: "IS_CARRIED_BY"
  depends_on:
    ["CARRIES", "Entity", "Entity Carrier Binding", "Entity/Carrier"]
version: 15
updated_at: "2026-10-15 18:50:39 +0000"
relations: {}
atom_id: "CA-D-257"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Define IS_CARRIED_BY

## Scope

the inverse direction of Carrier bindings.

## Claim

IS_CARRIED_BY **means** the inverse of CARRIES, directed from a non-ephemeral Entity **to** its Carrier.

## Details

the Entity/Carrier binding exposes this direction. its endpoints follow CARRIES, including the exact carried Revision **when** the Entity has Revisions.
