---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-20 20:26:00
relations:
  evaluation_for:
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
---
# Reject a commit without a valid Journal receipt

## Claim checked

The Git Doer cannot commit a governed subject change unless the matching Journal event has been durably appended.

## Test case

Invoke `COMMIT_CHANGE_SET` with one current sealed context and a missing, predicted, stale, or digest-mismatched Journal receipt.

## Acceptance criteria

Each invalid receipt produces a stable receipt-validation diagnostic before staging or committing, and the subject change, Journal, index, and Git history remain unchanged.

## Failure disposition

Reject the Git Doer if it reconstructs the receipt, commits without it, accepts mismatched event or carrier data, or partially mutates Git state.
