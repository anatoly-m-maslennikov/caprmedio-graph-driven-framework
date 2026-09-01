---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - artifact-operations
    occurrent:
      - evaluation
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  evaluation_for:
    - CA-M-213
---
# Verify capture ingest and reconcile external provenance

## Claim checked

CA-M-213 preserves reproducible external-source provenance through bounded analysis without implicitly creating project authority.

## Applicable when

Apply whenever external capture, analysis ingestion, or provenance reconciliation changes.

## Test case

Capture one external text source with complete origin and digest, ingest one derived claim into a bounded analysis frontier, then change the source and reconcile source, draft, session, target revision, and digest links without an adoption action.

## Acceptance criteria

The capture is immutable and reproducible; the analysis names the exact original source and target frontier; reconciliation reports the changed source as stale; no Requirement or other accepted authority is created or revised.

## Failure disposition

Reject the provenance method and preserve source carrier, origin and digest evidence, ingestion envelope, target frontier, reconciliation findings, and authority scan.
