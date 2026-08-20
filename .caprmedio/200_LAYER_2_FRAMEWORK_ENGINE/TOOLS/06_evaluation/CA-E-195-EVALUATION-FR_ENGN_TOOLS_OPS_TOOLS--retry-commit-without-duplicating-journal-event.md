---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 2
updated_at: 2026-08-20 21:32:00
relations:
  evaluation_for:
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--append-governed-file-change-journal-records
---
# Retry the commit without duplicating Journal records

## Claim checked

A partial Journal append or later commit failure can be retried with the same event identities and receipt set without duplicating any record.

## Test case

Use one sealed context with multiple related records; first interrupt after a proper subset is appended, then force Git commit creation to fail after the complete receipt set is returned, and retry the same context after each failure.

## Acceptance criteria

The Journal contains exactly one copy of every sealed record identity, each retry reuses existing receipts and appends only missing records, and exactly one final commit contains the governed subject change plus all related sidecar lines.

## Failure disposition

Reject the flow if retry duplicates a record, changes structured event content or partition, loses an existing receipt, omits a related sidecar line, or creates more than one successful commit.
