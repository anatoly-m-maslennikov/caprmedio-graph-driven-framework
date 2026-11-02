---
atom_id: CA-C-627
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom/(.Role := Operations)/Step
  passive:
  - Atom/(.Role := Operations)/Substep
  - Atom/(.Role := Operations)/Action
version: 1
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Concern
form: Question
---
## Summary

Resolve Step definition details after model-instance deferral

## Question

After keeping Workflow, Step, Substep, and Action as MODEL kinds and deferring actual instance review, should the existing Linear/Conditional Step and per-Step parameter/input-binding clauses remain as model-definition constraints, or move to a later instance-oriented contract?

## Why this is non-blocking

The active Step constraints remain complete for the required containment and RUN alternatives. The answer only determines the final home and wording of the retained conditional-routing and binding-detail clauses.
