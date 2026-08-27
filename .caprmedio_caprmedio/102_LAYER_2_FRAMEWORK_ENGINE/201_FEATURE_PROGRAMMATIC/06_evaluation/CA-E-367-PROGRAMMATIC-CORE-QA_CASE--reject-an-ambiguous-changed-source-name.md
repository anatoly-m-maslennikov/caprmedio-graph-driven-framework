---
atom_id: CA-E-367
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - source-name
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
# Reject an ambiguous changed source name

## Claim checked

One new or materially changed source unit has a specific,
intention-revealing name that states one responsibility.

## Test case

Evaluate one changed class named `Manager` without a qualifying project term or
owned responsibility.

## Acceptance criteria

Pass only when the class is rejected until its name identifies the exact
responsibility it owns.

## Failure disposition

Block the changed unit from claiming naming conformance.
