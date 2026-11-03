---
atom_id: CA-R-2639
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Step
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Action
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Workflow
version: 2
relations: {}
tier: 3
role: Requirement
form: Rule
updated_at: 2026-11-02 17:54:42 +0400
---

## Summary

Bind Step parameters

## Claim scope

Step selections and parameter bindings.

## Claim

A Step **must** own the bindings for the Action or Workflow it RUNS.

Each bound value comes from one of:

- A previous Step output.
- The input of the enclosing Workflow Run.
- A fixed value declared by the Step.

A Step binding references the selected Action or Workflow contract. It does not copy or redefine that contract.
