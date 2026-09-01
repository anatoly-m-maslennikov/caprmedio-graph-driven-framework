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
    - CA-M-211
---
# Verify materialize and validate one artifact catalog

## Claim checked

CA-M-211 builds a deterministic current catalog containing exactly its registered authority contributions and no independent meaning.

## Applicable when

Apply whenever a catalog definition, source contribution, generator, or validator changes.

## Test case

Build a catalog twice from a known authority frontier, then inject one stale entry, one duplicate, and one unknown entry into the materialization and validate it against unchanged sources.

## Acceptance criteria

The two clean builds are byte-identical and contain every and only registered contributions in stable order with source frontier metadata; validation identifies the stale, duplicate, and unknown entries separately.

## Failure disposition

Reject the catalog method and preserve definition, source frontier, both clean outputs, tampered output, and exact validation findings.
