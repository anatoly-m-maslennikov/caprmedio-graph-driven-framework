---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom
  passive:
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Goal'
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Demand'
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan)
version: 30
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-R-923
  - CA-R-924
  - CA-R-1576@21
  - CA-R-1588
atom_id: CA-E-425
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 5
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-425-CORE_META_MODEL-EVAL_CASE--validate-relational-atom-classifications.md
  source_atom_id: CA-E-425
  source_atom_revision: 30
  source_sha256: a0f6aa47fa53bd23a9f05509c5238ddcd7acec34d40df3422f71b26580e8ceaa
  original_relations_sha256: f51298c27d48a0f3abb1efc6b55cfe7af6ae821371edecacd6a64bf78acd5f9e
---
## Summary

Validate Relational Atom Classifications

## Claim scope

Relational Atom classifications.

## Claim

the Relational Atom classification Evaluation **must** enforce the qualified Types admitted by CA-R-924 **without** treating Plan Labels as Types.

- accept permitted relational Requirement/Goal, Requirement/Demand, **and** Plan/Plan cases with explicit non-default Claim targets.
- accept a current-scope Plan with decomposition **or** blocking **without** classifying it as relational merely because those Relations exist.
- change the Plan Label from Task **to** Objective **or** Epic; retain the same target-based classification.
- reject an unregistered qualified Type, an invalid relational target, **or** a Label interpreted as Type authority.

report the exact Atom, qualified Type, **and** target condition.
