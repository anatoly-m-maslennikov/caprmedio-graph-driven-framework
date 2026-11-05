---
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Traceability
  passive:
  - CAPRMEDIO_MODEL <+ Event Record
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Projection
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
---
## Summary

Validate Generated-Only Provenance Boundary

## Claim

### Prose Claim


generated-only provenance validation.


generated-only provenance validation **must not** pass **if** an update **only** **to** generated Projections contributes an Implementation Relation **or** a generated Projection cites itself as its semantic input. the same boundary applies with **or** **without** a version-control integration.
