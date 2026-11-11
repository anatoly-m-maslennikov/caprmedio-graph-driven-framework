---
atom_id: CA-E-489
ref_id: CA-E-489
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role:=Operations)/Workflow
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Workflow) >{1+} Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Step)'
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role:=Operations)/Action
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
tier: 3
relations:
  evaluation_for:
  - CA-R-1519
  - CA-R-1520
status: Active
version: 23
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-E-489-CORE_META_MODEL-EVAL_CASE--validate-workflow-execution-and-handoff-definitions.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Validate Workflow execution and handoff definitions

## Claim

### Prose Claim


a Workflow's declared execution **and** handoff behavior.


the Evaluation **must** check whether a Workflow's declared execution **and** handoff behavior is well formed under CA-R-1519 **and** CA-R-1520, independently of current executor availability.

## Details

### Cases and expected results

- complete input declarations, resolvable Action references, admitted transitions, explicit terminal outcomes, **and** declared capability requirements: pass this definition check **without** requiring a running executor.
- a missing required input declaration, unresolved definition reference, missing continuation-selection rule, **or** absent applicable approval condition: reject the affected definition.
- a well-formed definition whose selected executor lacks a declared capability, worker, **or** current permission: the definition remains valid; execution admission is blocked under CA-R-1519. do **not** report unavailable execution as malformed authority.
- a missing invocation input **or** runtime resource is an execution-admission problem rather than a definition defect **when** its required binding is correctly declared.
- a terminal handoff declares the target Revision, complete continuation inputs, reason, check evidence, **and** performed-effect account: accept its declared continuation boundary.
- a handoff definition resumes predecessor Steps, claims successor success **before** execution, bypasses approval, resets retries, **or** admits an unbounded continuation cycle: reject.
- a cross-Workflow Step route offered as a Run handoff: reject; the two boundaries have different endpoints **and** responsibilities.

report the exact failing source **and** condition. definition validity **must not** be reported as permission, execution readiness, successful execution, **or** evidence that a Run occurred.
