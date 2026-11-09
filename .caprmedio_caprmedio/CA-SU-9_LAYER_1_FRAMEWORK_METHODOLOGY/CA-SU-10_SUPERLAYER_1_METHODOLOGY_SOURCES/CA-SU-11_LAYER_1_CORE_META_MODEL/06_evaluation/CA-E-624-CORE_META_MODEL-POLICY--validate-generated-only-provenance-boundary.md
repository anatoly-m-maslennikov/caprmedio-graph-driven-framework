---
atom_id: CA-E-624
ref_id: CA-E-624
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Policy
topics:
  main_subject: "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Quality <+ Traceability"
  dependencies:
  - CAPRMEDIO_MODEL <+ Event Record
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Projection
tier: 4
relations:
  evaluation_for:
  - CA-M-135
  - CA-R-2535
status: Active
version: 38
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-E-624-CORE_META_MODEL-EVAL_POLICY--validate-generated-only-provenance-boundary.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Validate Generated-Only Provenance Boundary

## Claim

### Prose Claim


generated-only provenance validation.


generated-only provenance validation **must not** pass **if** an update **only** **to** generated Projections contributes an Implementation Relation **or** a generated Projection cites itself as its semantic input. the same boundary applies with **or** **without** a version-control integration.
