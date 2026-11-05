---
atom_id: CA-R-935
ref_id: CA-R-935
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Target Scope Unit
tier: 5
relations:
  child_of:
  - CA-R-932@37
status: Active
version: 37
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-R-935-CORE_META_MODEL-RULE--prohibit-demands-between-ancestors-and-descendants.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary
Prohibit Demands between ancestors and descendants

## Claim

### Prose Claim


Demand Atoms.


a Demand Atom's Claim Target Scope Unit **must not** be an ancestor **or** descendant of its Consumer Scope Unit.
