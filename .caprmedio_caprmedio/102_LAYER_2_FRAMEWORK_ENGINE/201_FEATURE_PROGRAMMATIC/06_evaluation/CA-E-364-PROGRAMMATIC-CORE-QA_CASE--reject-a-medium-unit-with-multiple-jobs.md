---
atom_id: CA-E-364
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - executable-unit-size
  depends_on:
    continuant:
      - PROGRAMMATIC
version: 1
updated_at: 2026-08-27 15:55:57 +0400
relations:
  evaluation_for:
    - CA-M-162
  derived_from:
    - CA-A-053
---
# Reject a medium unit with multiple jobs

## Claim checked

One changed executable unit between 26 and 40 logical lines performs exactly
one coherent job.

## Test case

Evaluate one 30-line changed function whose accurate name and branches reveal
two independently reusable responsibilities.

## Acceptance criteria

Pass only when the unit is rejected until the two responsibilities are split.

## Failure disposition

Block the unit from claiming the 26-to-40-line allowance.
