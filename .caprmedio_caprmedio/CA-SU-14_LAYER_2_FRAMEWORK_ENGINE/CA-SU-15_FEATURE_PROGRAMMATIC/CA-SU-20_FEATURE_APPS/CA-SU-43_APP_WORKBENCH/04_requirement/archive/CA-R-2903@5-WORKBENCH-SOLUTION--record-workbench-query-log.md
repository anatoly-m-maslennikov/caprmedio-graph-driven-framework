---
identity:
  atom_id: CA-R-2903@5
  ref_id: CA-R-2903@5
context:
  container:
    scope_unit: CA-SU-43
  role: Requirement
  form: Solution
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Project
  tier: 3
state:
  status: Archived
  version: 5
  updated_at: 2026-11-09 21:15:45 +0400
destination:
  file:
    name: CA-R-2903@5-WORKBENCH-SOLUTION--record-workbench-query-log.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-D-698
  - CA-M-502
---

## Summary

Record Workbench Query Log

## Claim

### Prose Claim

Each actual query Run, whether successful or failed, **must** add one temporary query-log entry. A Check **must not** add a query-log entry. The entry **must** contain the original query SQL exactly, the success/fail outcome, the error when execution fails, the row count and the column count. A technical ID and timestamp are allowed.

The backend and MCP **must** expose the same query-log list and fetch capability. Query-log entries **must** expire after two days (48 hours) when the log is used; no cleanup daemon is required. The log **must not** store result rows, extra schema data or a deleted-result restoration mechanism. A preview **must** limit the returned rows without changing the SQL recorded in the log.

Saved Views remain separate from the temporary query log and do not expire with it.

Query-log files use one hourly UTC batch. Expiry removes expired entries from query-log reads and expires old batch files when the log is used. Saved queries and Views are permanent and remain outside these batches.

Automatic query history may become visible after the Run response. A history-write failure must not discard or alter a completed Run or explicit Save result.

## Details

### Query log storage

Deliver the raw technical query log as UTF-8 NDJSON appends under `.caprmedio_runtime/workbench/query_log`. After an actual Run and any requested synchronous Save handling, submit one record to the Workbench owner's ordered background writer. Check submits none. Use the Run's submission timestamp to choose its UTC-hour file, named `query-log-YYYY-MM-DD-HH.ndjson`. Logging does not delay the Run response. Add no staging file, backfill, retry, second log or new event field.

Every new and returned retained record has exactly these seven fields: `log_id`, `at`, `sql`, `outcome`, `error`, `row_count` and `column_count`. Preserve the existing outcome semantics and exact approved SQL. A failed Run has null counts when unavailable. Never store result rows, result schema, View state, source data or a query result table in this log.

On append, list and get, retain and return only records whose UTC `at` is less than 48 hours old. Apply that two-day query-log lifetime independently of result retention and independently of the watcher change log, which has distinct ownership and semantics. Saved Views and their Journal records have no query-log TTL.

Read the legacy `.caprmedio_runtime/workbench/query-log.json` single-file list as compatibility input alongside retained hourly records. Its retained records remain readable until the same 48-hour expiry. Do not rewrite, migrate, backfill or stage legacy bytes. New records never append to that file. A background log-write failure is reported to stderr only, without retry or a query-log response warning. It does not alter a completed Run or synchronous Save result.

### Background log writes

Use one ordered background writer in each Workbench owner for automatic query history. Submit one record after each Run and any requested synchronous Save handling, using the submission timestamp. Do not wait for its file write before returning the Run result. Serialize query-log reads and writes so readers never see a partial line. Report background failures to stderr, without retry or a response warning. Drain submitted writes on orderly owner shutdown; a process crash may lose unflushed history.

Explicit query and View saves still finish writing before returning their IDs. Keep the query log separate from watcher event delivery, watcher history, result retention and saved Journal records.
