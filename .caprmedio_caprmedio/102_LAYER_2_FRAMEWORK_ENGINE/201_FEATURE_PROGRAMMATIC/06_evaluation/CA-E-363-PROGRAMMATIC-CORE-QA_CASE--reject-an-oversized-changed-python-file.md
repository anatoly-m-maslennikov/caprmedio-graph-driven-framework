---
atom_id: CA-E-363
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - source-file-size
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
# Reject an oversized changed Python file

## Claim checked

One new or materially changed hand-authored PROGRAMMATIC Python file remains at
or below 200 physical lines or has a specific bounded exception.

## Test case

Evaluate one changed 201-line hand-authored Python file with no file-size
exception.

## Acceptance criteria

Pass only when conformance is rejected until the file is reduced, split by
responsibility, or supplied with one accepted bounded exception.

## Failure disposition

Block the changed file from claiming source-boundary conformance.
