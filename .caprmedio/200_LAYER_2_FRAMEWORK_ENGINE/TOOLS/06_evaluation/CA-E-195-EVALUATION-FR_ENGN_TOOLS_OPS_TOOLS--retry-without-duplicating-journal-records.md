---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 4
updated_at: 2026-08-20 22:22:00
relations:
  evaluation_for:
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--append-governed-file-change-journal-records
---
# Retry the commit without duplicating Journal records

## Claim checked

A partial Journal append or later commit failure can be retried under the same repository lease with the same event identities and payload digests without duplicating or redefining any record.

## Test case

Use one sealed context with multiple related records. Interrupt after a proper subset is appended, retry the same event identities and payload digests, then attempt one accepted event identity with a different canonical payload. After the complete receipt set is returned, force Git commit creation to fail, attempt to advance a different action for the repository, and finally resume the original context.

## Acceptance criteria

The Journal contains exactly one copy of every sealed record identity; an identical retry reuses existing receipts and appends only missing records; the divergent payload fails before mutation with a stable identity-collision diagnostic. Git failure leaves one visible recoverable blocked action with its lease state, the different action waits, and resuming the original context creates exactly one final commit with all related sidecar lines before releasing the lease.

## Failure disposition

Reject the flow if retry duplicates or redefines a record, changes a partition, loses an existing receipt, silently loses or bypasses the lease, lets another action mutate the repository, omits a related sidecar line, or creates more than one successful commit.
