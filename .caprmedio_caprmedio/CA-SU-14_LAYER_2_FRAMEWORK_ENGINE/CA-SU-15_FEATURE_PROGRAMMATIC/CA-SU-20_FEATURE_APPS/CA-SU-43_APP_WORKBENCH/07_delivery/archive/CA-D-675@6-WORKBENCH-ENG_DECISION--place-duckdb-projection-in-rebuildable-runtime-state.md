---
atom_id: CA-D-675
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 6
author: Anatoly Maslennikov
role: Delivery
form: Eng Decision
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  delivery_for:
  - CA-R-2723
  - CA-R-2728
carrier_destination:
  file:
    name: CA-D-675@6-WORKBENCH-ENG_DECISION--place-duckdb-projection-in-rebuildable-runtime-state.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery/archive
updated_at: 2026-11-04 16:59:55 +0400
---

## Summary

Place the DuckDB Projection in rebuildable runtime state

## Claim scope

The Project-local DuckDB runtime files, bundled dependencies and container delivery.

## Claim

### Prose Claim

Deliver the rebuildable DuckDB database at `.caprmedio_runtime/workbench/projection.duckdb` in the selected repository. Keep internal materialized query results and owned spill data in that runtime directory. Rebuild source tables and clear old results at startup. Do not store source-byte copies, intermediate schema files or a second source of truth.

Expose only `main.atoms` and `main.scope_units` as public source tables. Internal graph mappings and generated result tables are disposable implementation state. Source files remain authoritative and unchanged by queries.

Bundle DuckDB `2.0.0` and its compatible DuckPGQ extension in the existing application image. Load the extension and grammar at trusted startup without downloading it at runtime. Disable external access and lock public configuration after startup. Admit native read queries only; trusted internal source refresh and result materialization use native write transactions with COMMIT. Do not add application retries, rollback or automatic recovery.

Build Svelte + TypeScript + Vite assets during image construction and serve the static output through Python. No Node server is needed at runtime. Deliver `/caprmedio/workbench`, `/caprmedio/mcp` and `/caprmedio/health` on the configured listener.

The current Project container has a `1536m` memory budget. Keep query delivery bounded and let DuckDB spill within the owned runtime directory. Measure real-repository queries and refreshes against this budget; increasing RAM alone is not a substitute for paging. Report storage and engine errors explicitly. A failed owner requires an explicit restart.
