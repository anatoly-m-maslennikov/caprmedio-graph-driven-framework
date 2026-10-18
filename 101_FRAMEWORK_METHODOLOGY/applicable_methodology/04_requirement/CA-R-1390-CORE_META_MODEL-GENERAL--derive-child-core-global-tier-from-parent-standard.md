---
subjects:
  governs: "Entity/Continuant/Node/Atom.Global Tier"
  depends_on:
    ["Entity/Continuant/Node/Atom.Local Tier: Core", "Entity/Continuant/Node/Scope Unit", "Entity/Continuant/Node/Scope Unit.Parent", "Entity/Continuant/Node/Scope Unit.Children"]
version: 14
updated_at: "2026-10-18 03:33:26 +0400"
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
  source_atom_revision: 14
  source_sha256: 71fad60d9a231ceaaa27ce9776c6b905b7ded1dbd0b759d08d661cf3d601a69f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Derive Child Core Global Tier from Parent Standard

## Scope

Core Atoms scoped **to** non-Project Scope Units and their direct parent Scope Units.

## Claim

a Core Atom scoped **to** a non-Project Scope Unit **must** have a Global Tier one greater than the Standard Global Tier of its direct parent Scope Unit.

## Details
