---
atom_id: CA-R-2482
ref_id: CA-R-2482
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Declaration)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
version: 2
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2482-CORE_META_MODEL-RULE--declare-formal-scope-independently-of-scope-unit.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Formal Scope Independently of Scope Unit

## Claim

### Prose Claim


Formal Scope expressed by a Declaration.


- A formal Scope Declaration is contained outside the Scope Unit it constrains.
- It states permitted active and passive Subjects, Relations, endpoints and cardinalities.
- Its Subjects resolve in the applicable MODEL and PROJECT STRUCTURE instances.
- A Target Scope does not widen its granted permissions.
- The Declaration does not establish runtime behavior.

