---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/External Effect Boundary
  depends_on:
  - Subject/Engineering/Effect Authorization
  - Subject/Engineering/Effect Boundary
version: 8
updated_at: 2026-10-24 00:38:25 +0400
relations:
  evaluation_for:
  - CA-M-409
  derived_from:
  - CA-A-053
atom_id: CA-E-362@8
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
tier: 3
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
