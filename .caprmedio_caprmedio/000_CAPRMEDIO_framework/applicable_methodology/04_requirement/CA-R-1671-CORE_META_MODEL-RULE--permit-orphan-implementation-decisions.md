---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom
version: 28
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-037
  - CA-R-1767
atom_id: CA-R-1671
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1671-CORE_META_MODEL-RULE--permit-orphan-implementation-decisions.md
  source_atom_id: CA-R-1671
  source_atom_revision: 28
  source_sha256: 0be73032774d1270277b3c2c41aef439a15be0a5809a7f47f2253132b1b5d06e
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
