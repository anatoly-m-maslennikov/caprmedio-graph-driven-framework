---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 3
updated_at: 2026-08-20 20:18:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS_OPS_TOOLS--process-one-file-change
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--append-governed-file-change-event
---
# Commit one governed change with its Journal sidecar

## Claim checked

Applying one valid sealed context creates exactly one commit for one governed subject identity and exactly one receipt-bound Journal record with the same canonical typed-upstream message.

## Test case

Prepare one valid `UPDATE` context with one unrelated unstaged change, run the Journal Doer and Git Doer, and inspect the new commit, Journal record, index, remaining working tree, and returned result envelope.

## Acceptance criteria

Exactly one new commit exists; its tree changes only the resolved governed identity and one appended line in the receipt-bound Journal segment; its one-line message exactly matches both the context and Journal `action_message`; the unrelated unstaged change remains untouched; and the returned commit identifier resolves to that commit.

## Failure disposition

Reject the flow and report the first extra commit, governed identity, Journal record, message difference, or unintended working-tree effect.
