---
identity:
  atom_id: CA-E-674
  ref_id: CA-E-674
context:
  container:
    scope_unit: CA-SU-43
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 5
relations:
  evaluation_for:
  - CA-R-2728
  - CA-M-462
  - CA-M-463
state:
  status: Active
  version: 6
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-E-674-WORKBENCH-EVAL_CASE--enforce-native-read-only-and-exclusive-owner-handoff.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---
## Summary

Enforce native read-only access and exclusive owner handoff

## Claim scope

The public-SQL guard for the file-backed DuckDB Projection.

## Claim

### Prose Claim

Trusted public SQL uses native single-query admission and trusted internal materialization transactions, executes the exact SQL once, returns complete results through bounded pages or explicit errors, and shares serialized access with indexing. Public SQL cannot edit sources or projected source rows. Owned database and spill writes are permitted; external file/network access, application retry, rollback and recovery remain unsupported. DuckPGQ internal management functions are unsupported; their connection-invalidating failures are an explicit MVP limitation, not a promised function-capability sandbox.

## Details

| Fixture | Expected outcome |
| --- | --- |
| SELECT, CTE, and native GRAPH_TABLE query | Each executes once and returns the requested result without changing projected source rows. |
| Multiple statements or INSERT/UPDATE/DELETE/DDL/SET/COPY/ATTACH request | Rejected by native single-read-query admission; no source file changes. |
| File/network read or external-access enable attempt | It fails; external access remains disabled. |
| Ordinary invalid SQL followed by a valid query | The first returns its query error, the next returns valid rows; no query is retried. |
| Unsupported DuckPGQ management function that invalidates the connection | Explicit engine/unavailable error reaches the caller and stderr; the source files stay unchanged and no automatic recovery occurs. |
| Memory-heavy query under a bounded native test memory limit | Completes within the native memory budget using owned disk spill, or returns an explicit resource error. No source file is changed. |
| Query completion followed by source refresh | Owner access is released; queries see the successful refreshed state. |
