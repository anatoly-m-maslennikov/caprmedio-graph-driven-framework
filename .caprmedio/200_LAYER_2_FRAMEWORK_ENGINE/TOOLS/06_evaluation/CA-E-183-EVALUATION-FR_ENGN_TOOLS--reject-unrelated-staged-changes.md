---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 3
updated_at: 2026-08-20 22:58:24
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS--process-one-file-change
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS--commit-one-governed-file-action
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS--append-governed-file-change-journal-records
---
# Reject unrelated staged changes

## Claim checked

The commit Doer does not create a commit while the index contains a staged change outside the resolved file identity.

## Test case

Prepare one valid sealed `UPDATE` context, stage a separate repository file, and invoke the complete apply flow.

## Acceptance criteria

The flow returns a deterministic unrelated-staged-change diagnostic before the first Journal append, releases any provisional unconsumed lease, preserves the complete index, and creates no Journal record, runtime blockage, or commit.

## Failure disposition

Reject the Doer if it commits, unstages, overwrites, or absorbs any staged change.
