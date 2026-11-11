---
atom_id: CA-R-2903
ref_id: CA-R-2903@3
container:
  scope_unit: CA-SU-43
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project
tier: 3
status: Archived
version: 3
updated_at: 2026-11-07 01:21:17 +0400
carrier_destination:
  file:
    name: CA-R-2903@3-WORKBENCH-RULE--record-workbench-query-log.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archived
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Record Workbench Query Log

## Claim

Each actual query Run, whether successful or failed, **must** add one temporary query-log entry. A Check **must not** add a query-log entry. The entry **must** contain the original query SQL exactly, the success/fail outcome, the error when execution fails, the row count and the column count. A technical ID and timestamp are allowed.

The backend and MCP **must** expose the same query-log list and fetch capability. Query-log entries **must** expire after two days (48 hours) when the log is used; no cleanup daemon is required. The log **must not** store result rows, extra schema data or a deleted-result restoration mechanism. A preview **must** limit the returned rows without changing the SQL recorded in the log.

Saved Views remain separate from the temporary query log and do not expire with it.

Query-log files use one hourly UTC batch. Expiry removes expired entries from query-log reads and expires old batch files when the log is used. Saved queries and Views are permanent and remain outside these batches.

Automatic query history may become visible after the Run response. A history-write failure must not discard or alter a completed Run or explicit Save result.
