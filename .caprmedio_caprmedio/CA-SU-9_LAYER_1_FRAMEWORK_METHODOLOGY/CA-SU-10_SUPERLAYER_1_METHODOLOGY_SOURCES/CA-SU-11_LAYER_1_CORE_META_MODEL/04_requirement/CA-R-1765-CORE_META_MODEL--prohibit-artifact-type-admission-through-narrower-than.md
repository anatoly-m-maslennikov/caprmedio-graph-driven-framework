---
atom_id: CA-R-1765
ref_id: CA-R-1765
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity
  dependencies:
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//NARROWER_THAN
tier: 1
status: Active
version: 35
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1765-CORE_META_MODEL-RULE--prohibit-artifact-type-admission-through-narrower-than.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Prohibit Artifact Type admission through NARROWER_THAN

## Claim

### Prose Claim


Artifact Type values.


an Artifact Type value **must not** use NARROWER_THAN **to** establish its admission as an Artifact.
