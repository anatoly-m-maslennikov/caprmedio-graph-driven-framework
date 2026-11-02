---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Graph Node/Engineering/provenance
  depends_on:
  - Subject/Graph Node/Engineering/programmatic software
version: 16
updated_at: 2026-10-25 17:32:27 +0400
relations:
  evaluation_for:
  - CA-M-192
  derived_from:
  - CA-A-058
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-374@16
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
type: Eval Case
tier: 1
---
# Separate action creation from provenance reliance

## Claim checked

one action **may** complete its originating mutation while provenance is pending,
but a later release **or** promotion-dependent action cannot rely on it **before**
reconciliation.

## Test case

complete one mutation into `git_complete_journal_pending`, **then** request a later
release that depends on that action's provenance.

## Acceptance criteria

pass **only** **when** the originating mutation remains complete **and** the later release
is blocked **until** the action becomes `reconciled`.

## Failure disposition

reject either behavior that blocks the originating mutation on its own pending
state **or** permits later governed reliance **before** reconciliation.

## Sources

- [CA-M-192 — Reconcile independent Git and Journal provenance](../05_method/CA-M-192-PROGRAMMATIC-METHOD--reconcile-independent-git-and-journal-provenance.md)
