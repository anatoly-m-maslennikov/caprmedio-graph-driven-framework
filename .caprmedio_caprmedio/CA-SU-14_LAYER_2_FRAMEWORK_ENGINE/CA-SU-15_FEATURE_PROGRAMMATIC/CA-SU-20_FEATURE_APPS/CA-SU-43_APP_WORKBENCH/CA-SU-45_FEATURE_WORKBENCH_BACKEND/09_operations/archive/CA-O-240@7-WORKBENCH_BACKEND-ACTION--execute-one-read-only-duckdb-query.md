---
atom_id: CA-O-240
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Archived
version: 7
author: Anatoly Maslennikov
role: Operations
form: Action
tier: 6
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  depends_on:
  - CA-R-2728
  - CA-R-2729
  - CA-R-2724
  - CA-M-463
  - CA-M-462
  - CA-D-673
carrier_destination:
  file:
    name: CA-O-240@7-WORKBENCH_BACKEND-ACTION--execute-one-read-only-duckdb-query.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/09_operations/archive
updated_at: 2026-11-04 23:19:17 +0400
---

## Summary

Execute one read-only DuckDB query

## Claim scope

One synchronous public Run, Page, Check, Save, Worksheet Save, Load, Saved List or Schema request.

## Claim

Execute a read-only query through the Project's shared owner:

- select the statement at optional UTF-16 `cursor_position` using native SQL tokenization, preserving quoted strings, comments and dollar-quoted strings;
- save the exact selected SQL as an immutable UTF-8 `q_<uuid hex>.sql` under `.caprmedio_runtime/workbench/saved_queries/` before Run or Check execution;
- return `saved_query_id`, `saved_query_url`, `kind` and the actual selected `sql` separately from the materialized result query ID, including them in query-error answers;
- if saving fails, return an explicit error and do not execute the query or promise a saved-query ID;
- save a full Worksheet script as `{"sql": "..."}` in an immutable `w_<uuid hex>.json` file;
- serialize the request with source refresh;
- validate the request and admit one native read query for Run or Check;
- retain original ordered column metadata, materialize the accepted query once into an internal result table, and commit the trusted cache write;
- for Run, count that result and return its first bounded page with its query ID and exact counts;
- for Page, read the requested slice from the existing stable result without rerunning SQL;
- for Check, return exact counts and discard the internal result;
- return known SQL, page and delivery errors to the caller, and keep source diagnostics on stderr.
- serve `query_save`, `worksheet_save`, `query_load`, `query_saved_list` and `query_schema` as explicit synchronous operations. Loading accepts an ID or URL and returns the saved identity and SQL without executing it; the list returns recent query and Worksheet entries with saved_query_id, saved_query_url, kind, preview and filesystem saved time; schema returns only `{tables: {atoms: [{name, type}], scope_units: [{name, type}]}}` metadata.

The Action does not edit source files or logical source facts. It adds no query job, queue, scheduler, retry, rollback, recovery or business Journal record.
