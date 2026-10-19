---
subjects:
  governs: "Entity/Carrier"
  depends_on:
    ["Entity/Continuant/Node/Project", "Entity/Continuant/Node/Scope Unit"]
version: 12
updated_at: "2026-10-18 07:33:30 +0400"
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
  source_atom_revision: 12
  source_sha256: 45a36d8d0648502b73408ae87695e6832e2b5f4fe4469037735b4791abc78226
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Ambient Project Scope Paths

## Scope

the `scope_path` encoding of a Carrier.

## Claim

a Carrier encoding of `scope_path` **must** omit the ambient current Project **and** use an empty path for Project Scope.

## Details
