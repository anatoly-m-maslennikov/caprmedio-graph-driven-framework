---
subjects:
  active: Atom/(.Role:=Operations)/Workflow
  passive:
  - Entity/Object/Occurrent/Execution/Workflow Run
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - Atom/(.Role:=Operations)/Action
  - Atom
  - Entity/Object/Continuant/Actor/Operator
version: 23
updated_at: 2026-11-02 08:06:47 +0400
relations:
  evaluation_for:
  - CA-R-1519
  - CA-R-1520
atom_id: CA-E-489
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-489-CORE_META_MODEL-EVAL_CASE--validate-workflow-execution-and-handoff-definitions.md
  source_atom_id: CA-E-489
  source_atom_revision: 23
  source_sha256: 20cc90b3c43b01249170731a25969ad2550ca2d3bb8fe81e74a112060fd572a2
  original_relations_sha256: 0102f19294d46f92e70f4ced01eb0886d175700ad499ae88801edb6e86df9647
---
## Summary

Validate Workflow execution and handoff definitions

## Claim scope

a Workflow's declared execution **and** handoff behavior.

## Claim

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
