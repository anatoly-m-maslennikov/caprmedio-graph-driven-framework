---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 3
updated_at: 2026-08-20 21:42:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS_OPS_TOOLS--process-one-file-change
---
# Append all related Journal records before the commit

## Claim checked

The Journal Doer completes every related append and returns the complete durable receipt set before the Git Doer begins commit creation.

## Test case

Instrument one valid apply flow whose related records span multiple Journal carriers to record every Journal fsync and receipt-return boundary and the first Git index or commit mutation.

## Acceptance criteria

Every related Journal append is fsynced and the complete valid receipt set is returned before any Git mutation, and the Git Doer consumes exactly that set.

## Failure disposition

Reject the flow if Git mutation starts first, any related append is not durable, or the Git Doer uses a predicted, incomplete, or different receipt set.
