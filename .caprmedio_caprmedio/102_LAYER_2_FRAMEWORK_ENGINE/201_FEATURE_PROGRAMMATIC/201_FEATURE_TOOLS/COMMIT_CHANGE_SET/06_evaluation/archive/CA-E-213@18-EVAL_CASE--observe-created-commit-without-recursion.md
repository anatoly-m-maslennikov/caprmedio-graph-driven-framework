---
subjects:
  governs: Subject/Engineering/Git/Commit
  depends_on: []
version: 18
updated_at: 2026-10-24 22:06:39 +0400
relations:
  evaluation_for:
  - CA-R-805
  - CA-R-812
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-213@18
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Observe created commit without recursion

## Claim checked

Completion observation records reconstructible runtime evidence for real-change **and** Journal-only commits **without** creating another action **or** commit.

## Test case

Create one valid real-change commit **and** one later Journal-only batch while installed observation hooks are registered. Inspect the observation log **and** outbox/reconciliation state **after** each commit.

## Acceptance criteria

Each commit produces one idempotent runtime observation naming its commit identity, parent, changed paths, commit class, **and** validation result. The real-change observation validates its sealed target **and** Initiative message; the Journal-only observation validates its selected Journal carrier set **and** batch form. No Atom, Journal record, index entry, ref beyond the original commit, trigger, **or** recursive commit is created.

## Failure disposition

Reject the delivery **if** completion is **not** observable, invalid content is reported valid, observation mutates governed source, **or** observation starts recursive work.
