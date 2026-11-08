---
identity:
  atom_id: CA-D-675
  ref_id: CA-D-675
context:
  container:
    scope_unit: CA-SU-43
  role: Delivery
  form: Decision
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 4
relations:
  delivery_for:
  - CA-R-2723
  - CA-R-2728
state:
  status: Active
  version: 14
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-D-675-WORKBENCH-DECISION--place-duckdb-projection-in-rebuildable-runtime-state.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Place the DuckDB Projection in rebuildable runtime state

## Claim scope

The Project-local DuckDB runtime files, bundled dependencies and container delivery.

## Claim

### Prose Claim

Deliver the rebuildable DuckDB database at `.caprmedio_runtime/workbench/projection.duckdb` in the selected repository. Keep internal materialized query results and owned spill data in that runtime directory. Rebuild source tables and clear old results at startup. Do not store source-byte copies, intermediate schema files or a second source of truth. Use one shared Workbench backend/result owner for MCP and the web frontend; do not add a second result cache or service.

Expose `main.atoms` and `main.scope_units` as public source tables and `main.change_log` as the technical watcher log. Internal graph mappings and generated result tables are disposable implementation state. Source files remain authoritative and unchanged by queries.

Retain each transient result table while its monotonic age is below the configured TTL or its owning View remains open. Opening a View pins its result; closing it unpins the result, while a young unpinned result remains until the TTL. A Workbench restart discards all transient tables and results. Rerunning a View drops the prior result before attempting the replacement, and a failed replacement does not restore it. No heartbeat, cross-process lease, crash recovery, scheduler or new service is added.

Read the editable `.caprmedio_runtime/caprmedio_runtime_settings.toml` at Workbench start. For example:

```toml
[workbench]
result_ttl_seconds = 3600
```

`result_ttl_seconds` must be a positive integer; a missing file uses the 3,600-second default for this delivery, while an existing invalid file is a startup configuration failure reported on stderr rather than silently defaulted. An explicit `workbench_restart`/reread is required to apply an edited file; no hot reload is required. The runtime settings file is outside the watcher `control_root` and does not create a `change_log` event. MCP setting editing and new configuration Tools are deferred.

Bundle DuckDB `2.0.0` and its compatible DuckPGQ extension in the existing application image. Load the extension and grammar at trusted startup without downloading it at runtime. Disable external access and lock public configuration after startup. Admit native read queries only; trusted internal source refresh and result materialization use native write transactions with COMMIT. Do not add application retries, rollback or automatic recovery.

Build Svelte + TypeScript + Vite assets during image construction and serve the static output through Python. No Node server is needed at runtime. Deliver `/caprmedio/workbench/<project_name>`, `/caprmedio/mcp` and `/caprmedio/health` on the configured listener.

The current Project container has a `1536m` memory budget. Keep query delivery bounded and let DuckDB spill within the owned runtime directory. Measure real-repository queries and refreshes against this budget; increasing RAM alone is not a substitute for paging. Report storage and engine errors explicitly. A failed owner requires an explicit restart.

Include the locked `pytz` dependency in the Workbench runtime group so native DuckDB timestamp-with-time-zone results can be fetched and encoded as ISO strings.

Exclude the frontend’s local `node_modules` dependency cache from release packages. Deliver its package manifest, lockfile and source, and build production assets in the image. Dependency-cache symlinks are not authored package input.
