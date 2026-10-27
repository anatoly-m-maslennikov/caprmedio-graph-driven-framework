---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: provenance
  depends_on:
  - Subject/Engineering/programmatic software
version: 15
updated_at: 2026-10-24 11:29:41 +0400
relations:
  evaluation_for:
  - CA-M-192
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-310@15
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
type: Eval Case
tier: 1
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
