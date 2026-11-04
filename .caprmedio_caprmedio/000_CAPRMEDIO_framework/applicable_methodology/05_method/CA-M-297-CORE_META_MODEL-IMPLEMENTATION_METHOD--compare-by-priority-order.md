---
version: 21
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-1487
  method_for:
  - CA-R-1487
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//PROJECT_LEXICOGRAPHIC
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//PROJECT_PRIORITY_MODEL
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)
atom_id: CA-M-297
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Method
form: Implementation Method
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-297-CORE_META_MODEL-IMPLEMENTATION_METHOD--compare-by-priority-order.md
  source_atom_id: CA-M-297
  source_atom_revision: 21
  source_sha256: 00d9d5705208f95abaaaf788f379a17c84e7d7e020afbb7d634a3a50864e1da5
  original_relations_sha256: ae04acb88297daa974bd08169ba33dbc88019ff0c09b2e9daea0eccf21fc1cb8
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
