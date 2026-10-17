---
subjects:
  governs: "relation-model"
  depends_on:
    ["scope-topology", "Atom Scope", "Entity/Continuant/Object/Atom.Target Scope Unit"]
version: 20
updated_at: "2026-10-15 18:47:06 +0000"
relations:
  child_of:
    - CA-R-932
atom_id: "CA-R-935"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-935-CORE_META_MODEL-GENERAL-REQUIREMENT--prohibit-demands-between-ancestors-and-descendants.md
  source_atom_id: CA-R-935
  source_atom_revision: 20
  source_sha256: cefbd54d0ae2eef680a08318b2c0e352f6911b1bff0141de7f5cc8cc8d5f2d21
  original_relations_sha256: 986ab56d61737841b77ed4fc4f1a391a0c8ad370d896e576cf2be7bdd2bdf459
---
# Summary
Prohibit Demands between ancestors and descendants

## Scope

Demand Atoms.

## Claim

a Demand Atom's Claim Target Scope Unit **must not** be an ancestor **or** descendant of its Consumer Scope Unit.

## Details
