---
atom_id: CA-R-2747
ref_id: CA-R-2747
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)/(.Header.Context.Form := Goal)
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Topics.Main Subject
tier: 5
relations:
  child_of:
  - CA-R-925@37
status: Active
version: 1
updated_at: 2026-11-04 09:19:08 +0400
carrier_destination:
  file:
    name: CA-R-2747-CORE_META_MODEL-RULE--require-goal-coverage-for-every-project.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Require Goal Coverage for Every Project

## Claim

### Prose Claim

Every Project is the Scope Unit resolved by the active Subject of at least one accepted Requirement Atom of Form Goal.
