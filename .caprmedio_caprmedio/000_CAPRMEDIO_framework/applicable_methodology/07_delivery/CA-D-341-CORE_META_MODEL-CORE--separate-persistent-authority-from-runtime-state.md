---
subjects:
  governs: Entity/Carrier
  depends_on:
  - "Entity/Continuant/Node/History"
version: 15
updated_at: "2026-10-18 03:34:40 +0400"
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
  source_atom_revision: 15
  source_sha256: c5f6086abb68a5590757d38385fa7fbf11d8227b9265366edb3dff8f137c8635
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Separate Persistent Authority from Runtime State

## Scope

persistent Carriers holding canonical authority or retained history, in relation to runtime cleanup.

## Claim

runtime cleanup **must not** remove persistent Carriers holding canonical authority or retained history.

## Details

Delivery placement and retention rules must keep that content outside the cleanup target set. This protection does not require a Carrier.Ownership Class or Carrier.Storage Boundary property, and it does not classify a Carrier as disposable merely because a runtime uses it.

