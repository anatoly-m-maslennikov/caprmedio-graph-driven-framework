---
subjects:
  active: CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Traceability
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/History/Journal > Event Record
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation
  - CAPRMEDIO <+ MODEL <+ Projection
version: 38
updated_at: 2026-11-02 18:35:20 +0400
relations:
  evaluation_for:
  - CA-M-135
  - CA-R-2535
atom_id: CA-E-624
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Evaluation
form: Eval Policy
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-624-CORE_META_MODEL-POLICY--validate-generated-only-provenance-boundary.md
  source_atom_id: CA-E-624
  source_atom_revision: 38
  source_sha256: 3cdd4a584bc0f61b4994d291ff3638132dea827e2e8da24cbe73f0d67a2b26e9
  original_relations_sha256: b0aadc358a427cc216398d47a4db7d796727f2db97a57ae01d8d48eebea1d338
---
## Summary

Validate Generated-Only Provenance Boundary

## Claim scope

generated-only provenance validation.

## Claim

generated-only provenance validation **must not** pass **if** an update **only** **to** generated Projections contributes an Implementation Relation **or** a generated Projection cites itself as its semantic input. the same boundary applies with **or** **without** a version-control integration.
