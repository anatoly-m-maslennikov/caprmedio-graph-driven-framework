---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 2
updated_at: 2026-08-20 21:33:00
relations:
  evaluation_for:
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
---
# Reject a commit without the complete valid Journal receipt set

## Claim checked

The Git Doer cannot commit a governed subject change unless every related Journal record has been durably appended and proven by the complete matching receipt set.

## Test case

Invoke `COMMIT_CHANGE_SET` with one current sealed context and, in separate runs, a missing, incomplete, predicted, stale, digest-mismatched, action-mismatched, and extra unrelated Journal receipt set.

## Acceptance criteria

Each invalid receipt set produces a stable receipt-validation diagnostic before staging or committing, and the subject change, Journal, index, and Git history remain unchanged.

## Failure disposition

Reject the Git Doer if it reconstructs receipts, commits without the complete exact set, accepts mismatched or unrelated event or carrier data, or partially mutates Git state.
