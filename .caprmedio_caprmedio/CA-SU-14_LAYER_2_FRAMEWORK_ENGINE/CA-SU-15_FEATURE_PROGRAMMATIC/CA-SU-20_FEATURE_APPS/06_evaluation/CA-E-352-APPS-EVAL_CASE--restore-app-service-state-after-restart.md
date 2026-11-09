---
atom_id: CA-E-352
ref_id: CA-E-352
container:
  scope_unit: CA-SU-20
role: Evaluation
form: Eval Case
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Recovery"
tier: 2
relations:
  evaluation_for:
  - CA-M-158
  - CA-M-222
status: Active
version: 17
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: APPS
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
