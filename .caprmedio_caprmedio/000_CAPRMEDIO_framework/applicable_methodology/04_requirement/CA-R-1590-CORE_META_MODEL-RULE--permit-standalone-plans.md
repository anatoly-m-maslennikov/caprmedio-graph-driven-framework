---
atom_id: CA-R-1590
ref_id: CA-R-1590
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom
tier: 2
status: Active
version: 22
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1590-CORE_META_MODEL-RULE--permit-standalone-plans.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1590-CORE_META_MODEL-RULE--permit-standalone-plans.md
  source_atom_id: CA-R-1590
  source_atom_revision: 22
  source_sha256: 5041b19668178e7bfeb279911425b4c3a37a0cdb2ebab1947a8505ca4efc8f1d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Permit standalone Plans

## Claim

### Prose Claim


Plan Atoms.


a Plan Atom **may** exist **without** an `IS_CONTAINED_BY` connection to a containing Plan; its Label **must not** require a containing Plan.
