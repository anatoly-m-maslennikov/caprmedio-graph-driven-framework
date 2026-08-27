---
atom_id: CA-E-373
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - provenance-binding
  depends_on:
    continuant:
      - PROGRAMMATIC
version: 1
updated_at: 2026-08-27 15:55:57 +0400
relations:
  evaluation_for:
    - CA-M-192
  derived_from:
    - CA-A-058
---
# Reject duplicate or mismatched provenance bindings

## Claim checked

One sealed action cannot become reconciled while duplicate canonical records,
duplicate real-change commits, or revision or digest mismatches remain.

## Test case

Provide one sealed action with two Journal records that both claim canonical
binding to the same real-change commit.

## Acceptance criteria

Pass only when reconciliation detects the duplicate, returns an explicit
blocked state, and does not select one record by guesswork.

## Failure disposition

Preserve the discrepancy and block provenance reliance until deterministic
repair establishes one binding.
