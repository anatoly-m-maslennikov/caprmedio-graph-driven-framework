---
subjects:
  governs: "Entity/Carrier"
  depends_on:
    ["Entity/Node/Continuant/Project", "Entity/Node/Continuant/Scope Unit"]
version: 13
updated_at: "2026-10-19 15:55:43 +0400"
relations: {}
atom_id: "CA-D-395"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-395-CORE_META_MODEL--serialize-ambient-project-scope-paths.md
  source_atom_id: CA-D-395
  source_atom_revision: 13
  source_sha256: 7fdd072781b75e3c409302420befa5f07765062b62c2d5898a7fb7ae0b29f5bb
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Ambient Project Scope Paths

## Scope

the `scope_path` encoding of a Carrier.

## Claim

a Carrier encoding of `scope_path` **must** omit the ambient current Project **and** use an empty path for Project Scope.

## Details
