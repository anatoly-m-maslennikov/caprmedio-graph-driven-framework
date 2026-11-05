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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2639-CORE_META_MODEL-RULE--bind-step-parameters.md
  source_atom_id: CA-R-2639
  source_atom_revision: 2
  source_sha256: c2fc5eb609c9c46f6c7f69b0de5488381af41c4f1fb894c3dc928c9d27f18dd2
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
