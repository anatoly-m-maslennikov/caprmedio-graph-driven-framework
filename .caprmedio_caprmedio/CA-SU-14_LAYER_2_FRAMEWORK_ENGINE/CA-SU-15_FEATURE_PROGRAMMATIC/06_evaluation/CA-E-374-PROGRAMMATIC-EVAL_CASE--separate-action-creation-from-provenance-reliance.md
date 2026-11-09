---
atom_id: CA-E-374
ref_id: CA-E-374
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Dynamic Testing"
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
tier: 1
relations:
  evaluation_for:
  - CA-M-192
  derived_from:
  - CA-A-058
status: Active
version: 19
updated_at: 2026-10-27 19:59:33 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
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
