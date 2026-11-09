---
identity:
  atom_id: CA-D-698@4
  ref_id: CA-D-698@4
context:
  container:
    scope_unit: CA-SU-45
  role: Delivery
  form: Solution
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Observability
      <+ Logging
    dependencies:
    - CAPRMEDIO_MODEL <+ Projection
  tier: 4
relations:
  delivery_for:
  - CA-R-2903
state:
  status: Archived
  version: 4
  updated_at: 2026-11-09 07:45:14 +0400
destination:
  file:
    name: CA-D-698@4-WORKBENCH_BACKEND-SOLUTION--deliver-hourly-query-log-files.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/07_delivery/archive
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---

## Summary

Deliver hourly Workbench query-log files

## Claim

### Prose Claim

Deliver the raw technical query log as UTF-8 NDJSON appends under `.caprmedio_runtime/workbench/query_log`. After an actual Run and any requested synchronous Save handling, submit one record to the Workbench owner's ordered background writer. Check submits none. Use the Run's submission timestamp to choose its UTC-hour file, named `query-log-YYYY-MM-DD-HH.ndjson`. Logging does not delay the Run response. Add no staging file, backfill, retry, second log or new event field.

Every new and returned retained record has exactly these seven fields: `log_id`, `at`, `sql`, `outcome`, `error`, `row_count` and `column_count`. Preserve the existing outcome semantics and exact approved SQL. A failed Run has null counts when unavailable. Never store result rows, result schema, View state, source data or a query result table in this log.

On append, list and get, retain and return only records whose UTC `at` is less than 48 hours old. Apply that two-day query-log lifetime independently of result retention and independently of the watcher change log, which has distinct ownership and semantics. Saved Views and their Journal records have no query-log TTL.

Read the legacy `.caprmedio_runtime/workbench/query-log.json` single-file list as compatibility input alongside retained hourly records. Its retained records remain readable until the same 48-hour expiry. Do not rewrite, migrate, backfill or stage legacy bytes. New records never append to that file. A background log-write failure is reported to stderr only, without retry or a query-log response warning. It does not alter a completed Run or synchronous Save result.
