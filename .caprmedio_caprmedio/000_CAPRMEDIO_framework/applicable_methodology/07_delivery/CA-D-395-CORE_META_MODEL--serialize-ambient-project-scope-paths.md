---
subjects:
  governs: "Entity/Carrier"
  depends_on:
    ["Entity/Continuant/Object/Project", "Entity/Continuant/Object/Scope Unit"]
version: 9
updated_at: "2026-10-15 18:51:52 +0000"
relations: {}
atom_id: "CA-D-395"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-395-CORE_META_MODEL--serialize-ambient-project-scope-paths.md
  source_atom_id: CA-D-395
  source_atom_revision: 9
  source_sha256: 485438d020cd5e7cec4db898ffef3ec312bf9ab1901e767cd6b1c64a4a173bca
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Ambient Project Scope Paths

## Scope

the `scope_path` encoding of a Carrier.

## Claim

a Carrier encoding of `scope_path` **must** omit the ambient current Project **and** use an empty path for Project Scope.

## Details
