---
atom_id: CA-E-362
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - subprocess-invocation
  depends_on:
    continuant:
      - PROGRAMMATIC
version: 1
updated_at: 2026-08-27 15:55:57 +0400
relations:
  evaluation_for:
    - CA-M-161
  derived_from:
    - CA-A-053
---
# Reject an unsafe subprocess invocation

## Claim checked

One PROGRAMMATIC subprocess uses an argument array, explicit timeout, checked
exit status, controlled environment input, and shell execution disabled.

## Test case

Evaluate one invocation expressed as a shell command string with shell
execution enabled.

## Acceptance criteria

Pass only when the invocation is rejected before process creation and reports
the unsafe argument and shell boundary.

## Failure disposition

Reject the subprocess path until it uses the complete bounded invocation
contract.
