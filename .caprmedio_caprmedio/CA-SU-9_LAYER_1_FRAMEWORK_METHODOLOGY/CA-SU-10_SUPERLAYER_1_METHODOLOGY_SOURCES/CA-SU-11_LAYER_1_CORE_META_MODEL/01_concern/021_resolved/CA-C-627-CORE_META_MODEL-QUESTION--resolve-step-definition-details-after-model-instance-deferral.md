---
atom_id: CA-C-627
ref_id: CA-C-627
container:
  scope_unit: CA-SU-11
role: Concern
form: Question
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Step
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Substep
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Action
tier: 3
status: Resolved
version: 3
updated_at: 2026-11-02 17:54:42 +0400
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
carrier_destination:
  file:
    name: CA-C-627-CORE_META_MODEL-QUESTION--resolve-step-definition-details-after-model-instance-deferral.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/01_concern/021_resolved
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
