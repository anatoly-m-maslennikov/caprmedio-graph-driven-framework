---
atom_id: CA-O-240
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Archived
version: 9
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
    name: CA-O-240@9-WORKBENCH_BACKEND-ACTION--execute-one-read-only-duckdb-query.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/09_operations/archive
---

## Summary

Execute one read-only DuckDB query

## Claim scope

One synchronous public Run or Check request.

## Claim

Execute one read-only Run or Check query through the Project's shared owner:

- select the statement at optional UTF-16 `cursor_position` using native SQL tokenization, preserving quoted strings, comments and dollar-quoted strings;
- serialize the request with source refresh;
- validate the request and admit one native read query for Run or Check;
- retain original ordered column metadata, materialize the accepted query once into an internal result table, and commit the trusted cache write;
- for Run, count that result and return its first bounded page with its query ID, actual selected SQL and exact counts;
- for Check, return selected SQL and exact counts and discard the internal result;
- return known SQL and delivery errors to the caller, and keep source diagnostics on stderr.

Run and Check do not save SQL, append a saved-item Journal record or require the Journal writer to be writable. Page, explicit Save, Worksheet Save, Load, List and Schema follow their shared Workbench contracts outside this Action.

The SQL operation does not edit Atom or Scope Unit source files or logical source facts. Internal materialized query state is disposable cache. It adds no query job, queue, scheduler, retry, rollback or recovery.
