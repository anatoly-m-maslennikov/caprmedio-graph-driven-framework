---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 5
updated_at: 2026-08-20 21:41:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS_OPS_TOOLS--process-one-file-change
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--append-governed-file-change-journal-records
---
# Commit one governed change with all related Journal sidecars

## Claim checked

Applying one valid sealed context creates exactly one commit containing one governed subject identity and every and only receipt-bound Journal sidecar record related to the same action.

## Test case

Prepare one valid `UPDATE` context that requires multiple related Journal records across two carrier partitions and has one unrelated unstaged change, run the Journal Doer and Git Doer, and inspect the new commit, Journal records, index, remaining working tree, projected commit message, and returned result envelope.

## Acceptance criteria

Exactly one new commit exists; its tree changes only the resolved governed identity and every receipt-bound related Journal line, even across multiple carriers; it contains no unrelated Journal line; its one-line message equals the deterministic Projection of the structured file-change event; the unrelated unstaged change remains untouched; and the returned commit identifier resolves to that commit.

## Failure disposition

Reject the flow and report the first extra commit, governed identity, missing or unrelated Journal record, message difference, or unintended working-tree effect.
