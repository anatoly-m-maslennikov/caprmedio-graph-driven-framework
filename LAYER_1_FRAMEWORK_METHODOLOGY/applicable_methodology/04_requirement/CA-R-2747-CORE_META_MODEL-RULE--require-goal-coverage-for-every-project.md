---
subjects:
  active: CAPRMEDIO_MODEL <+ Project
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Goal)
  - CAPRMEDIO_MODEL <+ Atom.Header.Subjects.Active
version: 1
updated_at: 2026-11-04 09:19:08 +0400
relations:
  child_of:
  - CA-R-925@37
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
atom_id: CA-R-2747
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 5
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-2747-CORE_META_MODEL-RULE--require-goal-coverage-for-every-project.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2747-CORE_META_MODEL-RULE--require-goal-coverage-for-every-project.md
  source_atom_id: CA-R-2747
  source_atom_revision: 1
  source_sha256: c38c9d341d86a34b043a847922b8728bdb0289efc31079bb8a9b70308f6a0335
  original_relations_sha256: 6850fba6396bfa91e19d1d450786556e91ffc8d09c26a7750d2d1d3cd69a363b
---
## Summary

Require Goal Coverage for Every Project

## Claim

### Prose Claim

Every Project is the Scope Unit resolved by the active Subject of at least one accepted Requirement Atom of Form Goal.
