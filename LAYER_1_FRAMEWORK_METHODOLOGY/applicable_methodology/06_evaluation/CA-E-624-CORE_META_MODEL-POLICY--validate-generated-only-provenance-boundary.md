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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-624-CORE_META_MODEL-POLICY--validate-generated-only-provenance-boundary.md
  source_atom_id: CA-E-624
  source_atom_revision: 38
  source_sha256: 15e5dbc2ee1c5e367bc22b08419755261d30d200584396e27385fff896ef21c5
  original_relations_sha256: b0aadc358a427cc216398d47a4db7d796727f2db97a57ae01d8d48eebea1d338
---
## Summary

Validate Generated-Only Provenance Boundary

## Claim

### Prose Claim


generated-only provenance validation.


generated-only provenance validation **must not** pass **if** an update **only** **to** generated Projections contributes an Implementation Relation **or** a generated Projection cites itself as its semantic input. the same boundary applies with **or** **without** a version-control integration.
