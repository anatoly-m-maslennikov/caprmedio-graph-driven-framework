---
atom_id: CA-E-366
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - source-effect-boundary
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
# Reject a hidden effect in changed source

## Claim checked

One changed effect function declares its complete effect boundary or allocates
persistent ownership to an object.

## Test case

Evaluate one changed function that reads the process environment implicitly
before writing its declared target.

## Acceptance criteria

Pass only when the function is rejected until the environment observation is
an explicit input or an owned adapter boundary.

## Failure disposition

Block the changed unit until the hidden observation is removed.
