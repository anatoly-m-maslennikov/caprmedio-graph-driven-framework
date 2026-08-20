---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-20 20:20:00
relations:
  evaluation_for:
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--gather-complete-commit-action-context
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-522--append-work-journal-events
---
# Partition the Journal by the configured calendar date

## Claim checked

Journal date partitioning uses the configured Artifact timestamp timezone rather than UTC or filesystem time.

## Test case

Configure `Asia/Tbilisi`, gather an event at `2026-08-20 00:30:00 +04`, and append it while the corresponding UTC date is still `2026-08-19`.

## Acceptance criteria

The sealed local date is `2026-08-20`, and the event is routed to `<author>-2026-08-20-part-1.ndjson`.

## Failure disposition

Reject the flow if it uses `2026-08-19`, a filesystem timestamp, or a timezone other than the configured one.
