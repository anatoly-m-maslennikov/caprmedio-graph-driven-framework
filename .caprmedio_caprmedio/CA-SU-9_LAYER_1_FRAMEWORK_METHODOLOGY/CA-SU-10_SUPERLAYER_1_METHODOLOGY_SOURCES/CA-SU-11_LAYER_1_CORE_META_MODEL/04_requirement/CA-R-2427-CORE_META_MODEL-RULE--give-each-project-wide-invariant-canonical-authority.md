---
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-2426
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project
  dependencies:
  - CAPRMEDIO_MODEL <+ Project
atom_id: CA-R-2427
ref_id: CA-R-2427
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2427-CORE_META_MODEL-RULE--give-each-project-wide-invariant-canonical-authority.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Give each Project-wide invariant canonical authority

## Claim

### Prose Claim


Project-wide foundational invariants.


Every Project-wide foundational invariant must have exactly one active Project-owned Tier `0` Atom as its canonical authority owner. One such Atom may own several related invariants; this does not require one Atom per invariant or one Tier `0` Atom for the Project. Faithful specialization does not create independent duplicate authority.
