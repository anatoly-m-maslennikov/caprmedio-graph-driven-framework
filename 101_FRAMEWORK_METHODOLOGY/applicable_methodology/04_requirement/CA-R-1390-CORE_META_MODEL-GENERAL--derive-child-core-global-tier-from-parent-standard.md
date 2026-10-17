---
subjects:
  governs: "Entity/Continuant/Object/Atom.Global Tier"
  depends_on:
    ["Entity/Continuant/Object/Atom.Local Tier: Core", "Entity/Continuant/Object/Scope Unit", "Entity/Continuant/Object/Scope Unit.Parent", "Entity/Continuant/Object/Scope Unit.Children"]
version: 13
updated_at: "2026-10-16 12:08:22 +0000"
relations: {}
atom_id: "CA-R-1390"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1390-CORE_META_MODEL-GENERAL--derive-child-core-global-tier-from-parent-standard.md
  source_atom_id: CA-R-1390
  source_atom_revision: 13
  source_sha256: f567a604e86d2c914455c321f41829b51f5688b1b825f15e11582d1df56ae3f9
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Derive Child Core Global Tier from Parent Standard

## Scope

Core Atoms scoped **to** non-Project Scope Units and their direct parent Scope Units.

## Claim

a Core Atom scoped **to** a non-Project Scope Unit **must** have a Global Tier one greater than the Standard Global Tier of its direct parent Scope Unit.

## Details
