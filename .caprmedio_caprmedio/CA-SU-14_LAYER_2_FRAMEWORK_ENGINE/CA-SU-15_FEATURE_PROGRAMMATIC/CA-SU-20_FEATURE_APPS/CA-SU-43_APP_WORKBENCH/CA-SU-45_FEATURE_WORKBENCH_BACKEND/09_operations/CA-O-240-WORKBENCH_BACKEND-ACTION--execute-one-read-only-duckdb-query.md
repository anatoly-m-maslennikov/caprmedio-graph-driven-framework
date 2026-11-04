---
atom_id: CA-O-240
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Active
version: 8
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
    name: CA-O-240-WORKBENCH_BACKEND-ACTION--execute-one-read-only-duckdb-query.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/09_operations
updated_at: 2026-11-05 01:40:28 +0400
---

## Summary

Execute one read-only DuckDB query

## Claim scope

One synchronous public Run or Check request.

## Claim

Execute one read-only Run or Check query through the Project's shared owner:

- select the statement at optional UTF-16 `cursor_position` using native SQL tokenization, preserving quoted strings, comments and dollar-quoted strings;
- save the exact selected SQL without a name to a dedicated append-only saved-item Journal under the configured Project Journal root before Run or Check execution. New saved entries use canonical unprefixed UUIDv7 IDs and fields `kind`, exact `sql`, optional `name` and `saved_at`; use the existing 1,000-row date-partitioned `workbench-saved-items` writer;
- return `saved_query_id`, `saved_query_url`, `kind` and the actual selected `sql` separately from the materialized result query ID, including them in query-error answers;
- if saving fails, return an explicit error and do not execute the query or promise a saved-query ID;
- serialize the request with source refresh;
- validate the request and admit one native read query for Run or Check;
- retain original ordered column metadata, materialize the accepted query once into an internal result table, and commit the trusted cache write;
- for Run, count that result and return its first bounded page with its query ID and exact counts;
- for Check, return exact counts and discard the internal result;
- return known SQL and delivery errors to the caller, and keep source diagnostics on stderr.
- save only the selected Run or Check SQL automatically; Page, explicit Save, Worksheet Save, Load, List and Schema follow the shared Workbench contracts outside this Action.

The SQL operation does not edit Atom or Scope Unit source files or logical source facts. Saved-item Journal appends are separate from business Journal records. It adds no query job, queue, scheduler, retry, rollback or recovery.
