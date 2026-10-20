---
subjects:
  governs: "Entity/Node/Continuant/Project.Framework Settings"
  depends_on:
    ["Entity/Node/Continuant/Project.Framework Settings"]
version: 15
updated_at: "2026-10-19 15:55:40 +0400"
relations:
  child_of:
    - CA-D-361
  relates_to:
    - CA-R-1630
atom_id: "CA-D-387"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-387-CORE_META_MODEL--serialize-atomic-admission-strictness.md
  source_atom_id: CA-D-387
  source_atom_revision: 15
  source_sha256: 2d0bc2fb62e81b3e6a31d1e6a618fa83c8a6b7a48fa93ec5e3dfcac537203090
  original_relations_sha256: 4f8fca2057373dee7e1934385c6ad655c38a428a7dc3d670e9844c9f996ddbfb
---
# Summary

Serialize Atomic Admission Strictness

## Scope

an explicit atomic admission strictness selection in the Framework Instance Settings TOML Carrier.

## Claim

an explicit atomic admission strictness selection **in** the Framework Instance Settings TOML Carrier **must** use `creation_strictness` **in** `[artifacts]`, using the allowed values governed by CA-R-1630.

## Details
