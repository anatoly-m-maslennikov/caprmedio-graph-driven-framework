---
atom_id: CA-R-1990
ref_id: CA-R-1990
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Enabled Relations.Contains'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Enabled Relations.Contains
tier: 3
relations:
  child_of:
  - CA-R-2478
status: Active
version: 12
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1990-CORE_META_MODEL-RULE--enable-containment-for-plan-atoms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1990-CORE_META_MODEL-RULE--enable-containment-for-plan-atoms.md
  source_atom_id: CA-R-1990
  source_atom_revision: 12
  source_sha256: b883608bcd21abe4b4b5fa2aed288c7137a51cd935cf73fcfedac91ffb4e4360
  original_relations_sha256: 4fde62f0627e52833e954bbd64d451c404b9f9d66585c52603ef12fa5886adfa
---
## Summary

Enable containment for Plan Atoms

## Claim

### Prose Claim


Containment capability of Plan Atoms.


`Atom/(.Header.Role := Plan).Enabled Relations.Contains` **must** be True. a Plan Atom **may** contain other Plan Atoms.

## Details

Plan labels such as Epic, Task and Version do not create different containment Types. Containment is optional and can nest. This permission does not implement a Plan projection or replace other typed relations between Plans.
