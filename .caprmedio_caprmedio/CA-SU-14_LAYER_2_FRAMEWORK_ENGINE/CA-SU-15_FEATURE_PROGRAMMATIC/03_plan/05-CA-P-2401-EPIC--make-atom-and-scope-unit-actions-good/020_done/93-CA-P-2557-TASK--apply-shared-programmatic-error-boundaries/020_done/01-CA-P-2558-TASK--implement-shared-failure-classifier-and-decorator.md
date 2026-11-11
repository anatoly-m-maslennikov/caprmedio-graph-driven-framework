---
atom_id: CA-P-2558
ref_id: CA-P-2558
container:
  atom: CA-P-2557
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Runtime Failure Classification
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2557
  relates_to:
  - CA-M-396
  - CA-M-397
  - CA-M-398
  - CA-M-399
  - CA-M-400
status: Done
version: 8
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 1-CA-P-2558-TASK--implement-shared-failure-classifier-and-decorator.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/93-CA-P-2557-TASK--apply-shared-programmatic-error-boundaries/done
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Implement shared failure classifier and decorator

## Objective

Build one transport-neutral sync/async boundary with explicit failure classification, caller-owned response adapters, and existing diagnostic logging. Python RuntimeError alone must not mean blocking runtime failure. Preserve cancellation, metadata and caller result/effect ownership.

## Details

One Task per file. After completion, review and update dependant Tasks before their execution. Actual business Workflow lifecycle recording remains with its declared executor; this Task does not invent it in an error decorator.

### Definition of Done

Focused semantic/function tests cover ordinary success, request failures, explicit blocking runtime failures, logging failure and cancellation. At most 15 minutes own work; split further if required.

### Execution checkpoint

The independent review follow-up is complete: actual exception classes are retained only when an exception exists; synthetic refusals do not invent one. Diagnostic severity is constrained to ERROR/WARNING/INFO/DEBUG. Ten focused boundary cases pass, including cancellation and diagnostic-sink failures, and scoped Ruff passes. The final related 32-case rerun also passes. Shared API and old positional FailureRecord construction are preserved; no retry or Journal side effects. Final independent review: APPROVED. Source/focused-test acceptance only, not deployment.
