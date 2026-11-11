---
atom_id: CA-R-1293
ref_id: CA-R-1293
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)/(.Header.Context.Form := Demand).Target Scope Unit'
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit.order.number
  - CAPRMEDIO_MODEL <+ Scope Unit
tier: 1
status: Active
version: 29
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1293-CORE_META_MODEL-RULE--prohibit-demands-to-later-ordered-siblings.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Prohibit Demands to Later Ordered Siblings

## Claim

### Prose Claim


Demand Atoms owned by Ordered Scope Units.


a Demand Atom owned by an Ordered Scope Unit **must not** target a later Ordered sibling under the same direct parent.
