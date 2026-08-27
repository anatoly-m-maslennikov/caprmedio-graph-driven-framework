---
atom_id: CA-E-374
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - provenance-reliance
  depends_on:
    continuant:
      - PROGRAMMATIC
version: 1
updated_at: 2026-08-27 15:55:57 +0400
relations:
  evaluation_for:
    - CA-M-192
  derived_from:
    - CA-A-058
---
# Separate action creation from provenance reliance

## Claim checked

One action may complete its originating mutation while provenance is pending,
but a later release or promotion-dependent action cannot rely on it before
reconciliation.

## Test case

Complete one mutation into `git_complete_journal_pending`, then request a later
release that depends on that action's provenance.

## Acceptance criteria

Pass only when the originating mutation remains complete and the later release
is blocked until the action becomes `reconciled`.

## Failure disposition

Reject either behavior that blocks the originating mutation on its own pending
state or permits later governed reliance before reconciliation.
