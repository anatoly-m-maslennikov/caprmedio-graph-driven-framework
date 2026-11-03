---
atom_id: CA-C-627
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Resolved
subjects:
  active: Atom/(.Role := Operations)/Step
  passive:
  - Atom/(.Role := Operations)/Substep
  - Atom/(.Role := Operations)/Action
version: 3
updated_at: 2026-11-02 17:54:42 +0400
relations: {}
tier: 3
role: Concern
form: Question
---
## Summary

Resolve Step definition details after model-instance deferral

## Question

How does a Step select its work and bind parameters?

## Resolution

The Operator confirmed:

- A Step runs exactly one Action or Workflow, or contains one or more Substeps.
- RUNS and CONTAINS are mutually exclusive; a Step is nonempty.
- Step parameter bindings use previous Step outputs, enclosing Workflow Run input, or values fixed by the Step.
- The same sources apply to called Workflow inputs.

Detailed Workflow-instance review remains deferred.
