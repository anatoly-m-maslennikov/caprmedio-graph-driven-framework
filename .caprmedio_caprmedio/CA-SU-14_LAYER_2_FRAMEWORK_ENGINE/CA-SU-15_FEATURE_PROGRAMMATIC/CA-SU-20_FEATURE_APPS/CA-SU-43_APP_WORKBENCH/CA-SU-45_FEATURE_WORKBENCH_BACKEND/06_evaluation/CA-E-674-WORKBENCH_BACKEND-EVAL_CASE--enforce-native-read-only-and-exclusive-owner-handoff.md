---
identity:
  atom_id: CA-E-674
  ref_id: CA-E-674
context:
  container:
    scope_unit: CA-SU-45
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Query Processing
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 5
relations:
  evaluation_for:
  - CA-R-2728
  - CA-M-462
  - CA-M-463
state:
  status: Active
  version: 9
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-674-WORKBENCH_BACKEND-EVAL_CASE--enforce-native-read-only-and-exclusive-owner-handoff.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Enforce native read-only access and exclusive owner handoff

## Claim scope

The public-SQL guard for the file-backed DuckDB Projection.

## Claim

### Prose Claim

Trusted public SQL uses native single-query admission and trusted internal materialization, executes exact SQL once, returns complete bounded results or explicit errors, and shares serialized access with indexing. Public SQL cannot edit sources or projected source rows; owned database/spill writes are permitted. External file/network access, retry, rollback and recovery are unsupported. DuckPGQ management functions may invalidate the connection; that is an explicit MVP limitation, not a promised function sandbox.

## Details

Exercise native SELECT/CTE/GRAPH_TABLE success, multi-statement and DDL/DML/SET/COPY/ATTACH rejection, external-access failure, invalid-SQL recovery, connection-invalidating management failure, bounded-memory spill/resource error, and completion followed by source refresh. Each case preserves source bytes; owner release makes successful refreshed state visible.
