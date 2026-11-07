---
atom_id: CA-R-947
ref_id: CA-R-947
container:
  scope_unit: CA-SU-11
role: Requirement
form: Requirement
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Goal)
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Project
tier: 6
relations:
  child_of:
  - CA-R-925@37
  - CA-R-2747
status: Active
version: 43
updated_at: "2026-11-07 15:18:44 +0400"
carrier_destination:
  file:
    name: CA-R-947-CORE_META_MODEL-REQUIREMENT--validate-goal-claim-scope.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Validate Goal Claim Scope

## Claim

### Prose Claim

A Goal is a Project Requirement. Its Main Subject identifies the Project Scope Unit. A Goal does not independently declare or change a Scope Unit's Name, parent, order, or Carrier binding.
