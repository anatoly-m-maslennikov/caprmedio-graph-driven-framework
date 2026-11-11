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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-935-CORE_META_MODEL-RULE--prohibit-demands-between-ancestors-and-descendants.md
  source_atom_id: CA-R-935
  source_atom_revision: 37
  source_sha256: e2cf5d67b57f684ccf1b1c08ad7aca994246aba832c56daba0faf549734e7158
  original_relations_sha256: c20ed3844d666cd523ff76d7355fb5c2277a21d8c1137804e80822202d14a70b
---
## Summary
Prohibit Demands between ancestors and descendants

## Claim

### Prose Claim


Demand Atoms.


a Demand Atom's Claim Target Scope Unit **must not** be an ancestor **or** descendant of its Consumer Scope Unit.
