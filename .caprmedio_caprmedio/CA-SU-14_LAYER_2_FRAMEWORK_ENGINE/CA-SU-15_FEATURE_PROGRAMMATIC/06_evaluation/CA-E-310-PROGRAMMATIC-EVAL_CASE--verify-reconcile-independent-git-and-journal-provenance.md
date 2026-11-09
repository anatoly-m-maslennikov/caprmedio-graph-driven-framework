---
atom_id: CA-E-310
ref_id: CA-E-310
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
status: Active
version: 21
updated_at: 2026-10-27 19:59:32 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
---
# Verify reconcile independent git and journal provenance

## Claim checked

one action whose real-change Git commit completes **before** its Journal record
converges **to** one canonical reconciled cross-system binding.

## Applicable conditions

apply **when** a sealed action is **in** `git_complete_journal_pending`.

## Test case

create one reachable real-change commit for a sealed action, append **=1**
canonical Journal record bound **to** that commit, **then** commit the Journal carrier
**in** a later separate Git commit.

## Acceptance criteria

pass **only** **when** the action becomes `reconciled`, **=1** canonical Journal
record binds **=1** reachable real-change commit, **and** the Journal record
does **not** embed the SHA of the commit containing that same record.

## Failure disposition

keep the action pending **or** blocked, preserve its sealed state, **and** reject later
provenance reliance **until** reconciliation succeeds.

## Sources

- [CA-M-192 — Reconcile independent Git and Journal provenance](../05_method/CA-M-192-PROGRAMMATIC-METHOD--reconcile-independent-git-and-journal-provenance.md)
