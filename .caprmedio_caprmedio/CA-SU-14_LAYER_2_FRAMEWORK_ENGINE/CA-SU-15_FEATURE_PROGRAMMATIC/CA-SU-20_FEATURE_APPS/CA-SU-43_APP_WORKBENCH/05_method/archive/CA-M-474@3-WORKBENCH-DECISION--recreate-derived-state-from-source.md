---
identity:
  atom_id: CA-M-474@3
  ref_id: CA-M-474@3
context:
  container:
    scope_unit: CA-SU-43
  role: Method
  form: Decision
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data
      Handling <+ Indexing
    dependencies:
    - CAPRMEDIO_MODEL <+ Projection
  tier: 5
relations:
  method_for:
  - CA-R-2786
state:
  status: Archived
  version: 3
  updated_at: 2026-11-09 07:45:15 +0400
destination:
  file:
    name: CA-M-474@3-WORKBENCH-DECISION--recreate-derived-state-from-source.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method/archive
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Recreate Workbench derived state from source

## Claim

### Prose Claim

For `workbench_reread`, close the active Workbench owner, remove the dedicated DuckDB database and its WAL and temporary files, create a new database, create the current Atom and Scope Unit tables and all derived relation, graph and query-result tables, then parse the governed Current and Draft source files directly. Materialize the current derived relations and graph data before reporting readiness. Do not truncate rows in place, retain stale columns, keep the old derived database, delete source files or saved items, or retry automatically. An invalid Scope Unit Declaration prevents readiness; an invalid non-Declaration source follows the existing reader error behavior.

## Details

The operation is one synchronous Workbench service operation. It uses the existing Workbench operation boundary and does not add a scheduler, queue, generic service registry, backup store or business Journal event.
