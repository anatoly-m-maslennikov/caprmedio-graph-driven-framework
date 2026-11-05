---
atom_id: CA-R-1447
ref_id: CA-R-1447
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Carrier
tier: 2
status: Active
version: 25
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1447-CORE_META_MODEL-RULE--define-owned-atoms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Owned Atoms

## Claim

### Prose Claim


the ownership of Atoms by Scope Units.


Owned Atoms **means** the set of **all** Atoms whose internally carried current Scope Unit **`=`** the selected Scope Unit.

- a grouping Carrier, Plan decomposition, **or** physical placement does **not** replace that ownership value.
- a missing, invalid, **or** ambiguous ownership value leaves membership unresolved; do **not** derive it from the filename **or** containing folders.
- evaluate placement consistency separately **without** changing the selected Atom's declared ownership.
