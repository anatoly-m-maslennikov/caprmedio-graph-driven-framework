---
atom_id: CA-E-362
ref_id: CA-E-362
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control"
  dependencies:
  - "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect Authorization"
tier: 5
relations:
  evaluation_for:
  - CA-M-409
  derived_from:
  - CA-A-053
status: Active
version: 15
updated_at: 2026-10-27 19:59:33 +0400
cce_version: cce_1
cce_form: evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Reject an unsafe subprocess invocation

## Claim checked

**when** no explicit governing exception applies, a PROGRAMMATIC subprocess invocation **must** use an argument array, an explicit timeout, checked exit status, controlled environment input, **and** disabled shell execution under CA-M-409.

## Test case

- evaluate a default-policy invocation expressed as a shell command string with shell execution enabled **and** no governing exception.
- evaluate a bounded argument-array invocation with disabled shell execution, timeout, checked exit status, **and** controlled environment input.

## Acceptance criteria

- reject the first invocation **before** process creation **and** report the unsafe argument **and** shell boundary.
- admit the second invocation **only** **when** its complete bounded effect contract is satisfied.
- evaluate an explicitly permitted exception against its governing authority; this default-policy fixture **must not** create a universal prohibition **or** authorize an exception.

## Failure disposition

reject an invocation that violates its governing effect boundary.
