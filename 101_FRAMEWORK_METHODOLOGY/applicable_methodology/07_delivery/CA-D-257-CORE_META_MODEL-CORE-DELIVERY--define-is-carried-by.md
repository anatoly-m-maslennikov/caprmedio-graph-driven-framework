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
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-257-CORE_META_MODEL-CORE-DELIVERY--define-is-carried-by.md
  source_atom_id: CA-D-257
  source_atom_revision: 15
  source_sha256: 515db40295c3892bda20dd11f5bc51af5325ead30491009afc5b5edf28371c75
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define IS_CARRIED_BY

## Scope

the inverse direction of Carrier bindings.

## Claim

IS_CARRIED_BY **means** the inverse of CARRIES, directed from a non-ephemeral Entity **to** its Carrier.

## Details

the Entity/Carrier binding exposes this direction. its endpoints follow CARRIES, including the exact carried Revision **when** the Entity has Revisions.
