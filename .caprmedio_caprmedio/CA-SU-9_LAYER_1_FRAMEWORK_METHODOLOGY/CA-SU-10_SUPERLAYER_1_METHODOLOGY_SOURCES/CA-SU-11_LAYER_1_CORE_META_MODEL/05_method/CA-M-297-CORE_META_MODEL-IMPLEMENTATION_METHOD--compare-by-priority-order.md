---
atom_id: CA-M-297
ref_id: CA-M-297
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//PROJECT_LEXICOGRAPHIC
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//PROJECT_PRIORITY_MODEL
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Method)
tier: 4
relations:
  child_of:
  - CA-R-1487
  method_for:
  - CA-R-1487
status: Active
version: 21
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-M-297-CORE_META_MODEL-IMPLEMENTATION_METHOD--compare-by-priority-order.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Compare by priority order

## Claim

### Prose Claim


priority-order comparison of admissible alternatives.


**when** the Operator selects comparison by priority order, the comparison of admissible alternatives **must** use the resolved order of active, applicable criteria as follows:

- an earlier criterion takes precedence over a later criterion.
- for alternatives tied on **all** earlier criteria, the first criterion that distinguishes them determines their relative preference.
- later criteria **must not** override a preference established by an earlier criterion.
- alternatives tied on **all** applicable criteria remain tied.
- an incomplete criterion order **or** an incomparable result at the current deciding criterion leaves the comparison unresolved; a later criterion **must not** bypass that gap.

this Method defines the comparison technique, **not** priority activation, alternative-selection execution, **or** escalation.
