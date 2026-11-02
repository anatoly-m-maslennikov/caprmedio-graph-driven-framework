---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Graph Node/Engineering/Execution Control/Recovery
  depends_on: []
version: 15
updated_at: 2026-10-27 06:04:45 +0400
relations:
  evaluation_for:
  - CA-M-158
  - CA-M-222
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-352@15
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: APPS
type: Eval Case
tier: 2
---
# Restore App service state after restart

## Claim checked

the App service restores owned lifecycle state **without** treating derived **or**
transient interface state as project authority.

## Test case

Provide governed source, a derived database snapshot, one running background
task, **and** transient interface state; terminate **and** restart the local App
service.

## Acceptance criteria

Governed source remains authoritative, rebuildable derived state is
reconciled, unfinished background work follows its declared recovery rule, **and**
transient interface state is neither mistaken for project authority nor
silently persisted.

## Failure disposition

Reject service recovery **when** authority changes, derived state remains stale,
work is lost **or** duplicated, **or** transient state is silently promoted **to** durable
state.

## Sources

- [Python documentation: task groups](https://docs.python.org/3/library/asyncio-task.html#task-groups)
- [Python documentation: SQLite transaction control](https://docs.python.org/3/library/sqlite3.html#transaction-control)
