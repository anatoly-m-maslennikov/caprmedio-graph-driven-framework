---
atom_id: CA-E-359
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - subtype-contract
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
# Reject inheritance without a substitutable contract

## Claim checked

One PROGRAMMATIC inheritance relationship exists only for a stable
substitutable subtype contract.

## Test case

Evaluate one changed subclass that inherits behavior for code reuse but cannot
replace its base under the base contract.

## Acceptance criteria

Pass only when the inheritance is rejected and the behavior is expressed by a
function, module, or composed collaborator.

## Failure disposition

Reject the subtype boundary until substitutability is demonstrated or
inheritance is removed.
