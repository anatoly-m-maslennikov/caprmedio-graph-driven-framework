---
atom_id: CA-E-372
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - provenance
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
# Reconcile a Journal-first action

## Claim checked

One action whose canonical Journal record is prepared before its real-change
Git commit becomes reconciled after the exact reachable commit SHA is known.

## Test case

Prepare one canonical Journal record for a sealed action, complete one
real-change commit, bind the record to that exact reachable commit, and commit
the Journal carrier later.

## Acceptance criteria

Pass only when the action advances from `journal_recorded_git_pending` to
`reconciled` with exactly one record and one reachable real-change commit.

## Failure disposition

Preserve the pending state and reject provenance reliance until binding is
complete.
