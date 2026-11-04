---
atom_id: CA-R-2639
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Step
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Action
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Workflow
version: 2
relations: {}
tier: 3
role: Requirement
form: Rule
updated_at: 2026-11-02 17:54:42 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2639-CORE_META_MODEL-RULE--bind-step-parameters.md
  source_atom_id: CA-R-2639
  source_atom_revision: 2
  source_sha256: c645f6e1915c1b265ea57be061202626372206d7a5c3256100ea494f44594241
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
