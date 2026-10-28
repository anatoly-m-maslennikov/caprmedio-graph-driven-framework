---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Traceability
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  - Subject/CAPRMEDIO/Graph/Relation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
version: 31
updated_at: 2026-10-27 19:59:38 +0400
relations:
  evaluation_for:
  - CA-M-135
  - CA-R-1746
atom_id: CA-E-624
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
type: Policy
tier: 4
---
# Summary

Validate Generated-Only Provenance Boundary

## Scope

generated-only provenance validation.

## Claim

generated-only provenance validation **must not** pass **if** an update **only** **to** generated Projections contributes an Implementation Relation **or** a generated Projection cites itself as its semantic input. the same boundary applies with **or** **without** a version-control integration.

## Details
