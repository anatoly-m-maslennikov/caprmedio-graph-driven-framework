---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-20 19:59:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS_OPS_TOOLS--process-one-file-change
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
---
# Reject unrelated staged changes

## Claim checked

The commit Doer does not create a commit while the index contains a staged change outside the resolved file identity.

## Test case

Prepare one valid sealed `UPDATE` context, stage a separate repository file, and invoke `COMMIT_CHANGE_SET` in apply mode.

## Acceptance criteria

The Doer returns a deterministic unrelated-staged-change diagnostic, preserves the complete index, and creates no commit.

## Failure disposition

Reject the Doer if it commits, unstages, overwrites, or absorbs any staged change.
