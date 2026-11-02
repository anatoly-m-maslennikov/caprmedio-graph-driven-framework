---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Demand.Target Scope Unit"
  depends_on:
    ["Entity/Node/Continuant/Scope Unit.Local Order", "Entity/Node/Continuant/Scope Unit/Type: Ordered"]
version: 17
updated_at: "2026-10-19 15:52:45 +0400"
relations: {}
atom_id: "CA-R-1293"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1293-CORE_META_MODEL-CORE--prohibit-demands-to-later-ordered-siblings.md
  source_atom_id: CA-R-1293
  source_atom_revision: 17
  source_sha256: a232d6f8be3ed42a36eb6f4bbd0e9b4bc2fd3760c164fe57f8ec7c7f3b8f0f93
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Prohibit Demands to Later Ordered Siblings

## Scope

Demand Atoms owned by Ordered Scope Units.

## Claim

a Demand Atom owned by an Ordered Scope Unit **must not** target a later Ordered sibling under the same direct parent.

## Details
