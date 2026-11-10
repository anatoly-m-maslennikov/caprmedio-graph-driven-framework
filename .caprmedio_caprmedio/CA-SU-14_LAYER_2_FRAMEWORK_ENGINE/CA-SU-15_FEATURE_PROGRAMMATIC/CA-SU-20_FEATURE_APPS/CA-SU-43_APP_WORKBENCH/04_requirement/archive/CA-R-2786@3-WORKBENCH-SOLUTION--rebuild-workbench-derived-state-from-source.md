---
identity:
  atom_id: CA-R-2786
  ref_id: CA-R-2786@3
context:
  container:
    scope_unit: CA-SU-43
  role: Requirement
  form: Solution
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 4
state:
  status: Archived
  version: 3
  updated_at: 2026-11-09 21:15:45 +0400
destination:
  file:
    name: CA-R-2786@3-WORKBENCH-SOLUTION--rebuild-workbench-derived-state-from-source.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-474
  - CA-D-679
---

## Summary

Rebuild Workbench derived state from source

## Claim

### Prose Claim

Workbench can perform a full reread of its governed source files. A full reread drops and recreates the dedicated DuckDB database, its WAL and temporary files, all Workbench schema, graph and query-result tables, and then reads the source again. It preserves source files, saved queries and Views, and does not delete source Journal records. It returns success only after the new Workbench state is ready. An invalid Scope Unit Declaration or startup failure returns an explicit failure and leaves Workbench unavailable until another explicit operation. The operation does not retry automatically.

## Details

#### Existing CA-R-2786 detail

Full reread may discard ephemeral query-result IDs because the derived result tables are recreated. It does not delete source Atoms, Scope Unit Declarations, saved items or Journal records.

### Full reread procedure

For `workbench_reread`, close the active Workbench owner, remove the dedicated DuckDB database and its WAL and temporary files, create a new database, create the current Atom and Scope Unit tables and all derived relation, graph and query-result tables, then parse the governed Current and Draft source files directly. Materialize the current derived relations and graph data before reporting readiness. Do not truncate rows in place, retain stale columns, keep the old derived database, delete source files or saved items, or retry automatically. An invalid Scope Unit Declaration prevents readiness; an invalid non-Declaration source follows the existing reader error behavior.


The operation is one synchronous Workbench service operation. It uses the existing Workbench operation boundary and does not add a scheduler, queue, generic service registry, backup store or business Journal event.

### Full reread interface

Expose the native MCP service tool `workbench_reread({})` and a health-page Full reread action through the same Workbench gateway operation. The operation has no generic service name, shell command, container argument or service registry. Add `workbench_reread` to the `Service` group of the generated `discover_tools` catalog. MCP and health use the same Project selection, operation and explicit failure boundary. The health page remains available when Workbench is unavailable. The operation does not restart MCP, another service or the container, and does not write a business Journal event.


The health action is an explicit POST to `/caprmedio/health/workbench-reread`; GET remains read-only. In shared mode it carries the existing explicit `project_root` form field; the single-Project action accepts no body. It reports success only after the full reread is ready and reports the same failure when source validation or startup fails.
