---
atom_id: CA-E-425
ref_id: CA-E-425
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Goal)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Demand)'
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
tier: 5
relations:
  evaluation_for:
  - CA-R-923
  - CA-R-924
  - CA-R-1576@21
  - CA-R-1588
status: Active
version: 30
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-E-425-CORE_META_MODEL-EVAL_CASE--validate-relational-atom-classifications.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Validate Relational Atom Classifications

## Claim

### Prose Claim


Relational Atom classifications.


the Relational Atom classification Evaluation **must** enforce the qualified Types admitted by CA-R-924 **without** treating Plan Labels as Types.

- accept permitted relational Requirement/Goal, Requirement/Demand, **and** Plan/Plan cases with explicit non-default Claim targets.
- accept a current-scope Plan with decomposition **or** blocking **without** classifying it as relational merely because those Relations exist.
- change the Plan Label from Task **to** Objective **or** Epic; retain the same target-based classification.
- reject an unregistered qualified Type, an invalid relational target, **or** a Label interpreted as Type authority.

report the exact Atom, qualified Type, **and** target condition.
