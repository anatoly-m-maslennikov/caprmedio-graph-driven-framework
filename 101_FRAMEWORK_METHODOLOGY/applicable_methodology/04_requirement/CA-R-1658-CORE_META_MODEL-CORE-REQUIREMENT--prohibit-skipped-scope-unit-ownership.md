---
subjects:
  governs: "Entity/Continuant/Node/Scope Unit.Parent"
  depends_on:
    []
version: 19
updated_at: "2026-10-18 03:33:47 +0400"
relations: {}
atom_id: "CA-R-1658"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1658-CORE_META_MODEL-CORE-REQUIREMENT--prohibit-skipped-scope-unit-ownership.md
  source_atom_id: CA-R-1658
  source_atom_revision: 19
  source_sha256: 52c3c18745b7572223a04425d18ca36ad32cb59b46dd38a532f931515d8e0859
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Prohibit skipped Scope Unit ownership

## Scope

Scope Unit ownership through a stored structural-parent relation.

## Claim

a Scope Unit **must not** own a descendant Scope Unit through a stored structural-parent relation **when** another active Scope Unit lies between them.

## Details
