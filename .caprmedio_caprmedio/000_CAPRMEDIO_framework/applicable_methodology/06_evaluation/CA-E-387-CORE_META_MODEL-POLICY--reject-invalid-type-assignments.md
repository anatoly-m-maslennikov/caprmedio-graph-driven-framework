---
subjects:
  active: CAPRMEDIO_MODEL <+ Entity
  passive:
  - CAPRMEDIO_MODEL <+ Entity
version: 27
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-R-1285
  - CA-R-1349
  - CA-R-1350
atom_id: CA-E-387
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Evaluation
form: Eval Policy
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-387-CORE_META_MODEL-POLICY--reject-invalid-type-assignments.md
  source_atom_id: CA-E-387
  source_atom_revision: 27
  source_sha256: 47018a2f255d7b07fa5b14ace7150b74def55f43f0c42fd5ead8b9c431f54a80
  original_relations_sha256: 957da0285972aed757b9d4f108d4be4aefeefc7f5f7a2ed7ac90dc6bae3aa9ed
---
## Summary

Reject Invalid Type Assignments

## Claim

### Prose Claim


Type assignments on Entity occurrences.


the Evaluation **must** reject a Type assignment **if** **any** of the following holds:

- an Entity occurrence that bears Type has **`!=1`** direct Type values.
- the selected value is **not** allowed by its most-specific applicable qualified Type Subject.
- qualified Type Subjects create **`>1`** Type Property slots for the occurrence.

absence of a Type value **in** an Entity occurrence that does **not** bear Type is **not** a cardinality failure under this Evaluation.
