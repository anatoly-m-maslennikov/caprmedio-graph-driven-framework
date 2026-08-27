---
atom_id: CA-E-270
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - engineering-ratchet
  depends_on:
    continuant:
      - PROGRAMMATIC
version: 3
updated_at: 2026-08-27 15:55:57 +0400
relations:
  evaluation_for:
    - CA-M-164
  derived_from:
    - CA-A-053
---
# Verify changed-code adoption ratchet

## Claim checked

One changed or new PROGRAMMATIC target within an admitted automation or typing
capability does not regress below its current passing boundary.

## Applicable conditions

Apply when a component changes source within an admitted typing, formatting,
linting, or behavioral-check capability. Unadmitted capability selection is
not applicable.

## Test case

Evaluate one changed target against its current admitted passing boundary.

## Acceptance criteria

Pass only when the target meets the current Method-owned boundary or has one
accepted Method-owned bounded exception. Configuration and Implementation must
materialize that selection, Delivery must govern its carrier, and Ops evidence
must report the actual result without becoming another authority.

## Failure disposition

Reject the ratchet claim and return the target to its change owner.
