---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-20 20:23:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS_OPS_TOOLS--process-one-file-change
---
# Append the Journal event before the commit

## Claim checked

The Journal Doer completes and returns its durable receipt before the Git Doer begins commit creation.

## Test case

Instrument one valid apply flow to record the Journal fsync and receipt-return boundary and the first Git index or commit mutation.

## Acceptance criteria

The Journal append, fsync, and valid receipt all occur before any Git mutation, and the Git Doer consumes that exact receipt.

## Failure disposition

Reject the flow if Git mutation starts first, the append is not durable, or the Git Doer uses a predicted or different receipt.
