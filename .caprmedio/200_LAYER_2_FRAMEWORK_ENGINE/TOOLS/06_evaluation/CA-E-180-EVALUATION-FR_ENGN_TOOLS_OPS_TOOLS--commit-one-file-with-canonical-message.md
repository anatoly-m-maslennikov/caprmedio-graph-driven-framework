---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-20 19:56:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS_OPS_TOOLS--process-one-file-change
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
---
# Commit one file with the canonical message

## Claim checked

Applying one valid sealed context creates exactly one commit for exactly one governed file identity with the canonical typed-upstream message.

## Test case

Prepare one valid `UPDATE` context with one unrelated unstaged change, apply `COMMIT_CHANGE_SET`, and inspect the new commit, index, remaining working tree, and returned result envelope.

## Acceptance criteria

Exactly one new commit exists; its tree changes only the resolved identity; its one-line message exactly matches the context; the unrelated unstaged change remains untouched; and the returned commit identifier resolves to that commit.

## Failure disposition

Reject the Doer and report the first extra commit, file identity, message difference, or unintended working-tree effect.
