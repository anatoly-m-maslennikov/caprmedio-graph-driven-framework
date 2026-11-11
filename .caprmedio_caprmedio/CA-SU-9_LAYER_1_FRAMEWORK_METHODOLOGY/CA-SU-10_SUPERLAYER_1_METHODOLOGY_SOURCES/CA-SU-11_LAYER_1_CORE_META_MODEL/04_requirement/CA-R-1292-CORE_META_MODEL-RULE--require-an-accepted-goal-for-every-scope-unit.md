---
atom_id: CA-R-1292
ref_id: CA-R-1292
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)/(.Header.Context.Form := Goal)'
  - CAPRMEDIO_MODEL <+ Atom.Content
tier: 1
status: Active
version: 31
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1292-CORE_META_MODEL-RULE--require-an-accepted-goal-for-every-scope-unit.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Require an Accepted Goal for Every Scope Unit

## Claim

### Prose Claim


Scope Units and their Claim Target Scope Unit references.


**every** Scope Unit **must** remain the Claim Target Scope Unit of **`>=1`** accepted Goal Atom.
