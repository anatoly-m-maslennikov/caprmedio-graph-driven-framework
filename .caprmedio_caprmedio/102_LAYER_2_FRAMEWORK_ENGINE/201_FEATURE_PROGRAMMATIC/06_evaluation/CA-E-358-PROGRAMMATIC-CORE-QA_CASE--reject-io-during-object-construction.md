---
atom_id: CA-E-358
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - object-construction
  depends_on:
    continuant:
      - PROGRAMMATIC
version: 1
updated_at: 2026-08-27 15:55:57 +0400
relations:
  evaluation_for:
    - CA-M-158
  derived_from:
    - CA-A-053
---
# Reject I/O during object construction

## Claim checked

One PROGRAMMATIC object is constructed without acquiring resources or applying
external effects.

## Test case

Construct one object while its declared resource boundary is unavailable and
observe whether construction attempts filesystem, process, network,
persistence, or logging-export I/O.

## Acceptance criteria

Pass only when construction completes without I/O and acquisition begins only
through a specifically named explicit method.

## Failure disposition

Reject the object lifecycle until acquisition is removed from construction.
