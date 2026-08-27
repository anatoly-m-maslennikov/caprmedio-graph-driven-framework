---
atom_id: CA-E-371
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - programmatic-mutation-identity
  depends_on:
    continuant:
      - PROGRAMMATIC
version: 1
updated_at: 2026-08-27 15:55:57 +0400
relations:
  evaluation_for:
    - CA-M-191
  derived_from:
    - CA-A-058
---
# Reject a mutation without stable Initiative identities

## Claim checked

One programmatic mutation is blocked before its first effect when its sealed
Initiative or stable action identity is missing or replaced.

## Test case

Submit one mutation whose worker replaces the stable action identity with its
queue-parent identity before applying the effect.

## Acceptance criteria

Pass only when the mutation returns an explicit blocked outcome and applies no
effect.

## Failure disposition

Reject dispatch until the original Initiative and action identities are
restored.
