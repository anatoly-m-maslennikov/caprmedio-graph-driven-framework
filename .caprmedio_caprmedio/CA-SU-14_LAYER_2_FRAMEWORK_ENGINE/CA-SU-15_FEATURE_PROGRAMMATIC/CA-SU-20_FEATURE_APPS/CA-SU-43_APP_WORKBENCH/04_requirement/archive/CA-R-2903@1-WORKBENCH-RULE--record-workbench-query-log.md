---
atom_id: CA-R-2903
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 1
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Project
relations: {}
carrier_destination:
  file:
    name: CA-R-2903@1-WORKBENCH-RULE--record-workbench-query-log.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
updated_at: 2026-11-05 16:45:35 +0400
---

## Summary

Record Workbench Query Log

## Claim

Each actual query Run, whether successful or failed, **must** add one temporary query-log entry. A Check **must not** add a query-log entry. The entry **must** contain the original selected SQL exactly, the success/fail outcome, the error when execution fails, the row count and the column count. A technical ID and timestamp are allowed.

The backend and MCP **must** expose the same query-log list and fetch capability. Query-log entries **must** expire after seven days when the log is used; no cleanup daemon is required. The log **must not** store result rows, extra schema data or a deleted-result restoration mechanism. A preview **must** limit the returned rows without changing the SQL recorded in the log.

Saved Views remain separate from the temporary query log and do not expire with it.
