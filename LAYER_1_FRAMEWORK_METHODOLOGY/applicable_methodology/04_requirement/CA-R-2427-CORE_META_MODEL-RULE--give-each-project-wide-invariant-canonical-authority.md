---
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-2426
subjects:
  active: CAPRMEDIO <+ MODEL <+ Project
  passive:
  - CAPRMEDIO <+ MODEL <+ Project
atom_id: CA-R-2427
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2427-CORE_META_MODEL-RULE--give-each-project-wide-invariant-canonical-authority.md
  source_atom_id: CA-R-2427
  source_atom_revision: 2
  source_sha256: 030a2a87552571c36a96dbc45a069091f070f36c67d597ac3f40139419cce794
  original_relations_sha256: 9f0c9e0f1fcf2f2c5a9fa2fc59daedca1bf033d712ca789b48d9c7a61722ae82
---
## Summary

Give each Project-wide invariant canonical authority

## Claim scope

Project-wide foundational invariants.

## Claim

Every Project-wide foundational invariant must have exactly one active Project-owned Tier `0` Atom as its canonical authority owner. One such Atom may own several related invariants; this does not require one Atom per invariant or one Tier `0` Atom for the Project. Faithful specialization does not create independent duplicate authority.
