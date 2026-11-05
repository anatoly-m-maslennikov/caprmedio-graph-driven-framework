---
atom_id: CA-R-2639
ref_id: CA-R-2639
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Step
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Action
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Workflow
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 17:54:42 +0400
carrier_destination:
  file:
    name: CA-R-2639-CORE_META_MODEL-RULE--bind-step-parameters.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Bind Step parameters

## Claim

### Prose Claim


Step selections and parameter bindings.


A Step **must** own the bindings for the Action or Workflow it RUNS.

Each bound value comes from one of:

- A previous Step output.
- The input of the enclosing Workflow Run.
- A fixed value declared by the Step.

A Step binding references the selected Action or Workflow contract. It does not copy or redefine that contract.
