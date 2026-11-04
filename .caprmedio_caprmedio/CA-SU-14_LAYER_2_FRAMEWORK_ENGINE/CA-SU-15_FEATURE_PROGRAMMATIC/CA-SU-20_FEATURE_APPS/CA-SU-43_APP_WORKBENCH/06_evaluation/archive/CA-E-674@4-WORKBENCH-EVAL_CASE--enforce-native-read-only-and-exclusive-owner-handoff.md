---
atom_id: CA-E-674
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
author: Anatoly Maslennikov
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
version: 4
role: Evaluation
form: Eval Case
tier: 5
carrier_destination:
  file:
    name: CA-E-674@4-WORKBENCH-EVAL_CASE--enforce-native-read-only-and-exclusive-owner-handoff.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation/archive
relations:
  evaluation_for: [CA-R-2728, CA-M-462, CA-M-463]
updated_at: 2026-11-04 07:39:08 +0400
---
## Summary

Enforce native read-only access and exclusive owner handoff

## Claim scope

The public-SQL guard for the in-memory DuckDB Projection.

## Claim

### Prose Claim

Trusted public SQL uses native single-query admission and native read-only transactions, executes the exact SQL once, returns complete results or explicit errors, and shares serialized access with indexing. It creates no file or network access, application retry, rollback, or recovery layer. DuckPGQ internal management functions are unsupported; their connection-invalidating failures are an explicit MVP limitation, not a promised function-capability sandbox.

## Details

| Fixture | Expected outcome |
| --- | --- |
| SELECT, CTE, and native GRAPH_TABLE query | Each executes once and returns the requested result without changing projected source rows. |
| Multiple statements or INSERT/UPDATE/DELETE/DDL/SET/COPY/ATTACH request | Rejected as unsupported or by the native read-only boundary; no source file changes. |
| File/network read or external-access enable attempt | It fails; external access remains disabled. |
| Ordinary invalid SQL followed by a valid query | The first returns its query error, the next returns valid rows; no query is retried. |
| Unsupported DuckPGQ management function that invalidates the connection | Explicit engine/unavailable error reaches the caller and stderr; the source files stay unchanged and no automatic recovery occurs. |
| Memory-heavy query under a bounded native test memory limit | Completes in memory or returns its memory error; no database, temporary-spill, or intermediate file is created. |
| Query completion followed by source refresh | Owner access is released; queries see the successful refreshed state. |
