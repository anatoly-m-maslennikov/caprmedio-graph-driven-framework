---
subjects:
  governs: "Entity/Carrier.Storage Boundary"
  depends_on:
    - "Framework-Owned Carrier"
    - "Project-Owned Carrier"
    - "Runtime State Carrier"
version: 13
updated_at: "2026-10-15 18:51:20 +0000"
relations: {}
atom_id: "CA-D-341"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-341-CORE_META_MODEL-CORE--separate-persistent-authority-from-runtime-state.md
  source_atom_id: CA-D-341
  source_atom_revision: 13
  source_sha256: cd3146dfff71babbd03c9586d8f53f478ac359a35a0531582f780321f5fb69e2
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Separate Persistent Authority from Runtime State

## Scope

persistent Framework-Owned and Project-Owned Carriers.

## Claim

Framework-Owned **and** Project-Owned persistent Carriers **must** remain outside Runtime State so Runtime State cleanup cannot remove canonical authority **or** Journal history.

## Details
