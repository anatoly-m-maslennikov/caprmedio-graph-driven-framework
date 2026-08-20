---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 2
updated_at: 2026-08-20 22:06:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS_OPS_TOOLS--process-one-file-change
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--gather-complete-commit-action-context
---
# Gather deterministic context read-only

## Claim checked

The optional `COMMIT_CONTEXT` Finder returns complete deterministic context without mutating governed or Git state.

## Test case

Prepare one fixed `UPDATE` trigger and repository fixture, snapshot all governed files, runtime outputs, index entries, and Git references, then invoke the Finder twice with the same input.

## Acceptance criteria

Both sealed envelopes are byte-identical and contain the adapter and source-event provenance, one file identity, the `UPDATE` change set, before and after carriers, versions, digests, Git base, complete typed upstream relations, structured event, predicted sidecar record set, deterministic Git message Projection, lease availability, and validation results; every snapshot remains unchanged and no apply lease is acquired.

## Failure disposition

Reject the Finder and identify the first missing, unstable, or mutated field or state.
