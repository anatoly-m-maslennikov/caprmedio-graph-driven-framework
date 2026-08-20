---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-20 20:25:00
relations:
  evaluation_for:
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--append-governed-file-change-event
---
# Retry the commit without duplicating the Journal event

## Claim checked

A commit failure after a successful Journal append can be retried with the same event identity and receipt without another append.

## Test case

Force Git commit creation to fail after one valid Journal receipt is returned, restore Git availability, and retry the same sealed context.

## Acceptance criteria

The Journal contains exactly one event with the sealed identity, the retry reuses its original receipt, and exactly one final commit contains that event and the governed subject change.

## Failure disposition

Reject the flow if retry appends another event, changes the action message or partition, loses the first receipt, or creates more than one successful commit.
