---
subjects:
  governs: "Entity/Continuant/Object/Atom"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Requirement/Type: Goal", "Entity/Continuant/Object/Atom/Content Role: Requirement/Type: Demand", "Entity/Continuant/Object/Atom/Content Role: Plan"]
version: 17
updated_at: "2026-10-16 12:09:04 +0000"
relations: {"evaluation_for": ["CA-R-923", "CA-R-924", "CA-R-1576", "CA-R-1588"]}
atom_id: "CA-E-425"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-425-CORE_META_MODEL-QA_CASE--validate-relational-atom-classifications.md
  source_atom_id: CA-E-425
  source_atom_revision: 17
  source_sha256: 9b7f27b84c1ee4c5ab3cb9589dd72dbc49b770b9dc2ce0807e47cfe622563ab7
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Validate Relational Atom Classifications

## Scope

Relational Atom classifications.

## Claim

the Relational Atom classification Evaluation **must** enforce the qualified Types admitted by CA-R-924 **without** treating Plan Labels as Types.

- accept permitted relational Requirement/Goal, Requirement/Demand, **and** Plan/Plan cases with explicit non-default Claim targets.
- accept a current-scope Plan with decomposition **or** blocking **without** classifying it as relational merely because those Relations exist.
- change the Plan Label from Task **to** Objective **or** Epic; retain the same target-based classification.
- reject an unregistered qualified Type, an invalid relational target, **or** a Label interpreted as Type authority.

report the exact Atom, qualified Type, **and** target condition.

## Details
