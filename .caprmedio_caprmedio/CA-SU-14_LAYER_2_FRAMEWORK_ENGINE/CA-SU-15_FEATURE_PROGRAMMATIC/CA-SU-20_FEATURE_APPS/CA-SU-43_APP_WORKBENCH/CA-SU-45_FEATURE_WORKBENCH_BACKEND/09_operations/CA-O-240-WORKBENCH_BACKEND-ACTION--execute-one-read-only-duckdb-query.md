---
atom_id: CA-O-240
ref_id: CA-O-240
container:
  scope_unit: CA-SU-45
role: Operations
form: Action
topics:
  {"main_subject": "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Query Processing", "dependencies": ["CAPRMEDIO_MODEL <+ Projection"]}
tier: 6
relations:
  depends_on:
  - CA-R-2728
  - CA-R-2729
  - CA-R-2724
  - CA-M-463
  - CA-M-462
  - CA-D-673
status: Active
version: 10
updated_at: 2026-11-05 20:32:03 +0400
carrier_destination:
  file:
    name: CA-O-240-WORKBENCH_BACKEND-ACTION--execute-one-read-only-duckdb-query.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/09_operations
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---

## Summary

Execute one read-only DuckDB query

## Operation

### Claim scope

One synchronous public Run or Check request.

### Claim
Execute one whole read-only Run or Check query through the Project's shared owner:

- validate the supplied whole query and its public arguments; a cursor position neither selects a statement nor executes a fragment;
- serialize the request with source refresh;
- admit one native read query for Run or Check;
- retain original ordered column metadata, materialize the accepted query once into an internal result table, and commit the trusted cache write;
- for Run, count that result and return its first bounded page with its query ID, actual submitted SQL and exact counts;
- for Check, return submitted SQL and exact counts and discard the internal result;
- return known SQL and delivery errors to the caller, and keep source diagnostics on stderr.

For a View rerun, validate the full request before disturbing the current result. Once valid execution begins, release that View's old materialized result before running the new query; a later native-query failure therefore leaves no old result. Editing View SQL alone does not release the last Run result. The dedicated result lifecycle controls retention, pinning and disposal; this Action neither writes its setting nor manually stages result data.

Run and Check do not save SQL, append a saved-item Journal record or require the Journal writer to be writable. Page, explicit Save, Worksheet Save, Load, List and Schema follow their shared Workbench contracts outside this Action.

The SQL operation does not edit Atom or Scope Unit source files or logical source facts. Internal materialized query state is disposable cache. It adds no query job, queue, scheduler, retry, rollback or recovery.
