---
atom_id: CA-E-674
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
author: Anatoly Maslennikov
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
version: 3
role: Evaluation
form: Eval Case
tier: 5
carrier_destination:
  file:
    name: CA-E-674@3-WORKBENCH-EVAL_CASE--enforce-native-read-only-and-exclusive-owner-handoff.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation/archive
relations:
  evaluation_for: [CA-R-2728, CA-M-462, CA-M-463]
updated_at: 2026-11-04 05:16:33 +0400
---
## Summary

Enforce native read-only access and exclusive owner handoff

## Claim scope

The public-SQL guard for the in-memory DuckDB Projection.

## Claim

### Prose Claim

The selected native public-SQL guard for in-memory DuckDB and DuckPGQ rejects Projection-changing SQL, including data-modifying CTEs and side-effecting graph-management or graph-cache calls, and leaves rows and the registered graph unchanged. A single SELECT classification alone is not sufficient evidence. External access is disabled and locked before public SQL, so file and network reads fail. The query holds database access until it completes or fails, then releases it for the indexer. This handoff is between query and indexing work, without hot reload or owner replacement.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Valid `SELECT` and read-only `GRAPH_TABLE` query | Both pass native parsing and execution without changing a projected row or the registered graph. |
| Graph creation, graph deletion, or graph-cache mutation, including a side-effecting function called from `SELECT` | The public request is rejected; graph state and later traversal results remain unchanged. |
| `INSERT`, `UPDATE`, `DELETE`, or data-modifying CTE | The native guard rejects it; no state change is visible. |
| File/network read or configuration-enable attempt | It fails; external access remains disabled. |
| Failed query followed by valid query | The failure reaches its caller and does not corrupt the in-memory Projection. |
| Multi-statement SQL, DDL, DML, SET, COPY or ATTACH | Native statement classification rejects it before execution. |
| Memory-heavy public query under a bounded test memory limit | It either completes in memory or returns an explicit out-of-memory error; no temporary spill, database or intermediate file is created. |
| Query completion or failure followed by index refresh | Database access is released; the indexer applies its update atomically and later queries see the committed result. |
