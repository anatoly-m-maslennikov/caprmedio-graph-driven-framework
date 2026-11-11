---
atom_id: CA-O-240
ref_id: CA-O-240
container:
  scope_unit: CA-SU-45
role: Operations
form: Action
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Data Handling <+ Query Processing
  dependencies:
  - MODEL//CAPRMEDIO <+ Projection
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
version: 12
updated_at: 2026-11-10 20:47:54 +0400
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

Execute one whole read-only Run or Check through the selected Project's shared owner: validate arguments (cursor is editor metadata), serialize with refresh, admit one native read query and materialize it once with ordered metadata. Check returns validity/available exact counts/errors then discards its result without export/save/log/SQL echo. Run retains ID/counts and saves a Bookmark only after successful execution; it submits metadata-only history to the existing writer without waiting.

Direct Run exports complete cached result in the chosen format by default or explicit inline page; View Run returns metadata and fetches separately. Return descriptor only after export succeeds. Later save/export failure preserves known cached result and reports the failed part without retry/rollback; ordinary responses omit full SQL and source diagnostics go to stderr. Validate View rerun before releasing its old result; once execution begins release it even if SQL fails, while SQL editing alone preserves the last result. Page/View Fetch use existing cache only, never execute/save/log SQL; explicit Load/View-query reads return SQL. This action edits no source Atom/Scope Unit and adds no job, queue, scheduler, retry, rollback or recovery.
