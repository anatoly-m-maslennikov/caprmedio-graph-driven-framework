---
atom_id: CA-R-1203
ref_id: CA-R-1203
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Content
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//GOVERNS
  - CAPRMEDIO_MODEL <+ Entity
tier: 1
status: Active
version: 32
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1203-CORE_META_MODEL-RULE--split-at-multiple-governed-subject-boundaries.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Split at Multiple Governed Subject Boundaries

## Claim

### Prose Claim


an Atom Claim governing canonical Entities through GOVERNS Subject Relations.


an Atom **must** be split **if** its Claim governs **`>1`** canonical Entities through GOVERNS Subject Relations.
