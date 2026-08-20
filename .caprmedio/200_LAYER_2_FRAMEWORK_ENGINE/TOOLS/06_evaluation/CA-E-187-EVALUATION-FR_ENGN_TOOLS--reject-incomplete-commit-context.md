---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 3
updated_at: 2026-08-20 22:58:24
relations:
  evaluation_for:
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS--gather-complete-commit-action-context
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS--commit-one-governed-file-action
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS--append-governed-file-change-journal-records
---
# Reject incomplete commit context

## Claim checked

The commit Doer fails closed when a required sealed-context field is absent.

## Test case

Remove the singular canonical `result` field from one otherwise valid sealed `UPDATE` context and invoke the complete apply flow.

## Acceptance criteria

The flow returns a deterministic missing-`result` diagnostic before the first Journal append, releases any provisional unconsumed lease, and creates no Journal record, runtime blockage, or Git state change.

## Failure disposition

Reject the flow if it reconstructs the omitted canonical field from the working tree, appends or commits, leaves an unconsumed lease, partially applies the context, or emits a generic diagnostic.
