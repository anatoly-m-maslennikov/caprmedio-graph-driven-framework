---
atom_id: CA-E-373
ref_id: CA-E-373
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
# Reject duplicate or mismatched provenance bindings

## Claim checked

one sealed action cannot become reconciled while duplicate canonical records,
duplicate real-change commits, **or** revision **or** digest mismatches remain.

## Test case

provide one sealed action with two Journal records that both claim canonical
binding **to** the same real-change commit.

## Acceptance criteria

pass **only** **when** reconciliation detects the duplicate, returns an explicit
blocked state, **and** does **not** select one record by guesswork.

## Failure disposition

preserve the discrepancy **and** block provenance reliance **until** deterministic
repair establishes one binding.

## Sources

- [CA-M-192 — Reconcile independent Git and Journal provenance](../05_method/CA-M-192-PROGRAMMATIC-METHOD--reconcile-independent-git-and-journal-provenance.md)
