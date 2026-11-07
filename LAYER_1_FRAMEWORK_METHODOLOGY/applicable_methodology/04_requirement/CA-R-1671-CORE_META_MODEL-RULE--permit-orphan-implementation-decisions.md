---
atom_id: CA-R-1671
ref_id: CA-R-1671
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
tier: 3
relations:
  child_of:
  - CA-R-037
  - CA-R-1767
status: Active
version: 28
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1671-CORE_META_MODEL-RULE--permit-orphan-implementation-decisions.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1671-CORE_META_MODEL-RULE--permit-orphan-implementation-decisions.md
  source_atom_id: CA-R-1671
  source_atom_revision: 28
  source_sha256: 81480c73ce61d97e89967f0aa16e0a98abdecdd9cb55206e0e596732c35fd3a7
  original_relations_sha256: 88d99219171064e6cdae57d7c68ea42a4e821c1db504d1ed385cbb2a12ce6002
---
## Summary

Permit orphan Implementation Decisions

## Claim

### Prose Claim


orphan permission for an active Eng Decision in strict authority mode.


`eng_decision` **must** be registered as orphan-permitted, so an active Eng Decision **may** have no parent Eng Policy even **in** strict authority mode.

## Details

This Atom-topology permission does not create a local Policy owner at a leaf or justify artificial children; local Eng Policy ownership and child applicability remain governed by CA-R-2119@8 and CA-R-2120@8.
