---
atom_id: CA-O-242
ref_id: CA-O-242@1-draft
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
  - CA-R-2728@9-draft
  - CA-R-2729
  - CA-R-2724
  - CA-M-463
  - CA-M-550@1-draft
  - CA-D-673@19-draft
  IS_REPLACEMENT_FOR:
  - CA-O-240
status: Draft
version: 1
updated_at: 2026-11-11 01:59:26 +0400
carrier_destination:
  file:
    name: CA-O-242@1-draft-WORKBENCH_BACKEND-ACTION--execute-workbench-sql-statements.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/09_operations/draft
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Execute Workbench SQL statements

## Operation

### Claim scope

One synchronous public Run or Check request.

### Claim

Execute a synchronous Run or Check through the selected Project shared owner under CA-R-2728@9-draft. Validate the whole Tab script or explicit statement selection; execute statements in order, stop at first failure and retain completed results and effects. SELECT uses the query Projection; supported UPDATE and find/replace changes use the shared source adapter, explicit mode, change preview and apply under CA-R-2728@9-draft. Check validates without source writes. Serialize with refresh and report complete per-statement and per-change results and errors.

Direct Run exports complete cached result in the chosen format by default or explicit inline page; View Run returns metadata and fetches separately. Return descriptor only after export succeeds. Later save/export failure preserves known cached result and reports the failed part without retry/rollback; ordinary responses omit full SQL and source diagnostics go to stderr. Validate View rerun before releasing its old result; once execution begins release it even if SQL fails, while SQL editing alone preserves the last result. Page/View Fetch use existing cache only, never execute/save/log SQL; explicit Load/View-query reads return SQL. This action adds no job, queue, scheduler, retry, rollback or recovery.
