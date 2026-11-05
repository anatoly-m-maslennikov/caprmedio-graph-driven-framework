---
atom_id: CA-E-404
ref_id: CA-E-404
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//depends_on
  dependencies:
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//DEPENDS_ON
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 5
relations:
  evaluation_for:
  - CA-R-1026
  - CA-R-915
  - CA-D-268
  - CA-M-239
  - CA-R-1580
status: Active
version: 27
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-E-404-CORE_META_MODEL-EVAL_POLICY--reject-invalid-dependency-order-derivations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-404-CORE_META_MODEL-POLICY--reject-invalid-dependency-order-derivations.md
  source_atom_id: CA-E-404
  source_atom_revision: 27
  source_sha256: d66978f6fc0f14ea0a85b3a43ea5696658da80b4c4b5f1552276e10431164886
  original_relations_sha256: 44f0551ce813b22e053e5e81c99f3b7917efa6de275ea5d8b2f4fd34965ff846
---
## Summary

Reject Invalid Dependency-Order Derivations

## Claim

### Prose Claim


derived non-Plan Artifact dependency orders.


the Evaluation **must** reject one derived non-Plan Artifact dependency order **if** a relation endpoint is **not** an admitted non-Plan Artifact, one `relations.depends_on` target reference repeats, a permutation of target-list positions changes its direct-edge set **or** derived order, an edge is absent from `relations.depends_on`, `relations.derived_from` contributes an edge, **or** the direct dependency graph **contains** a cycle.

## Details

Plan blocking **must** be checked separately under CA-E-504-CORE_META_MODEL-EVAL_CASE--validate-plan-blocking-and-parallel-readiness; a Plan `BLOCKS` fact **must not** fail merely because it is absent from `relations.depends_on`.
