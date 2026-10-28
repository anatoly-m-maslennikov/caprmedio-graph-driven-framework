---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
version: 18
updated_at: 2026-10-27 19:59:36 +0400
relations:
  evaluation_for:
  - CA-R-1519
  - CA-R-1520
atom_id: CA-E-489
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
type: Eval Case
tier: 3
---
# Summary

Validate Workflow execution and handoff definitions

## Scope

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
