---
atom_id: CA-R-1990
ref_id: CA-R-1990
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Enabled Relations.Contains'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Enabled Relations.Contains
relations:
  child_of:
  - CA-R-2478
version: 12
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-1990-CORE_META_MODEL-RULE--enable-containment-for-plan-atoms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Enable containment for Plan Atoms

## Claim

### Prose Claim


Containment capability of Plan Atoms.


`Atom/(.Header.Role := Plan).Enabled Relations.Contains` **must** be True. a Plan Atom **may** contain other Plan Atoms.

## Details

Plan labels such as Epic, Task and Version do not create different containment Types. Containment is optional and can nest. This permission does not implement a Plan projection or replace other typed relations between Plans.
