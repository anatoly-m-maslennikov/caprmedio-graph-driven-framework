---
atom_id: CA-E-362
ref_id: CA-E-362
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution
    Control <+ Effect Authorization
tier: 5
relations:
  evaluation_for:
  - CA-M-409
  DERIVED_FROM:
  - CA-A-053
status: Active
version: 16
updated_at: 2026-11-10 20:47:54 +0400
cce_version: cce_1
cce_form: evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
destination:
  file:
    name: CA-E-362-PROGRAMMATIC-EVAL_CASE--reject-an-unsafe-subprocess-invocation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Reject an unsafe subprocess invocation

## Claim

### Prose Claim

#### Claim checked

**when** no explicit governing exception applies, a PROGRAMMATIC subprocess invocation **must** use an argument array, an explicit timeout, checked exit status, controlled environment input, **and** disabled shell execution under CA-M-409.

#### Test case

- evaluate a default-policy invocation expressed as a shell command string with shell execution enabled **and** no governing exception.
- evaluate a bounded argument-array invocation with disabled shell execution, timeout, checked exit status, **and** controlled environment input.

#### Acceptance criteria

- reject the first invocation **before** process creation **and** report the unsafe argument **and** shell boundary.
- admit the second invocation **only** **when** its complete bounded effect contract is satisfied.
- evaluate an explicitly permitted exception against its governing authority; this default-policy fixture **must not** create a universal prohibition **or** authorize an exception.

#### Failure disposition

reject an invocation that violates its governing effect boundary.
