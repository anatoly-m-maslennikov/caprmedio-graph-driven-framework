---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - programmatic-mutation
    occurrent:
      - evaluation
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  evaluation_for:
    - CA-M-206
---
# Verify project bounded work journal ndjson to toon

## Claim checked

CA-M-206 produces a reproducible lossless TOON Projection of one unchanged bounded Journal frontier.

## Applicable when

Apply whenever the Journal-to-TOON encoder, frontier grammar, or Projection metadata changes.

## Test case

Select a known ordered NDJSON event range, project it twice, and compare decoded values, identities, order, source frontier, encoder provenance, and output bytes. During a third projection, change one selected source line before completion.

## Acceptance criteria

Both unchanged runs are byte-identical and decode to every original event field in original order; metadata identifies the exact source frontier and encoder; the changed-frontier run produces no accepted Projection.

## Failure disposition

Reject the Projection method and preserve source and output digests, decoded comparisons, provenance metadata, and changed-frontier handling.
