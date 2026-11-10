---
identity:
  atom_id: CA-M-534
  ref_id: CA-M-534
context:
  container:
    scope_unit: CA-SU-43
  role: Method
  form: Decision
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Observability <+ Logging
  tier: 4
state:
  status: Active
  version: 1
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-534-WORKBENCH-DECISION--write-workbench-query-history-in-hourly-batches.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method
relations:
  method_for:
  - CA-R-2903
author: Anatoly Maslennikov
---

## Summary

Write Workbench query history in hourly batches

## Claim

### Prose Claim

Query-log files use hourly UTC batches. Expiry removes old entries from reads and old batch files when the log is used. Bookmarks and Views are permanent and outside these batches.

#### Query log storage

Append the raw technical log as UTF-8 NDJSON under `.caprmedio_runtime/workbench/query_log`. After a Run and requested synchronous Save handling, submit one record to the owner's ordered background writer; Check submits none. The Run submission timestamp selects `query-log-YYYY-MM-DD-HH.ndjson`. Logging does not delay Run. Add no staging file, backfill, retry, second log or event field.

Every new and returned retained record has exactly these seven fields: `log_id`, `at`, `sql`, `outcome`, `error`, `row_count` and `column_count`. Preserve the existing outcome semantics and exact approved SQL. A failed Run has null counts when unavailable. Never store result rows, result schema, View state, source data or a query result table in this log.

On append, list and get, retain and return only records whose UTC `at` is under 48 hours old. This lifetime is independent of result retention and watcher history. Saved Views and Journal records have no query-log TTL.

Read the legacy `.caprmedio_runtime/workbench/query-log.json` single-file list as compatibility input alongside retained hourly records. Its retained records remain readable until the same 48-hour expiry. Do not rewrite, migrate, backfill or stage legacy bytes. New records never append to that file. A background log-write failure is reported to stderr only, without retry or a query-log response warning. It does not alter a completed Run or synchronous Save result.

#### Background log writes

Use one ordered writer per Workbench owner. Do not wait for its file write before returning Run; serialize reads and writes so readers never see a partial line. Report background failure to stderr without retry or a response warning. Drain submitted writes on orderly shutdown; a crash may lose unflushed history.

Explicit query and View saves still finish writing before returning IDs. Keep this log separate from watcher delivery/history, result retention and saved Journal records.

Check returns query-request metadata only and is not logged. List and fetch query-log entries through `query_log_list` and `query_log_get`. Execution responses do not automatically echo SQL; the log stores the exact submitted SQL and returns it on an explicit log read.
