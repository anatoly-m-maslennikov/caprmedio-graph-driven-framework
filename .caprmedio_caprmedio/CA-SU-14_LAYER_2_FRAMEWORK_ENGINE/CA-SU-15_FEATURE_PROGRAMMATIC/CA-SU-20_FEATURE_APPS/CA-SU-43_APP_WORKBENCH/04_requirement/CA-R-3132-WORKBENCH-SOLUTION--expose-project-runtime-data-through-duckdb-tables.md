---
identity:
  atom_id: CA-R-3132
  ref_id: CA-R-3132
context:
  role: requirement
  form: solution
  tier: 3
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Projection
  container:
    scope_unit: WORKBENCH
state:
  version: 1
  status: active
  updated_at: '2026-11-13T10:44:52.059934+00:00'
destination:
  file:
    name: CA-R-3132-WORKBENCH-SOLUTION--expose-project-runtime-data-through-duckdb-tables.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
---
## Summary

Expose Project runtime data through DuckDB tables

## Claim scope

Read-only SQL over queryable runtime data for the selected Project.

## Claim

### Prose Claim

Expose queryable Project runtime data through DuckDB tables, `query_run` and `query_schema`. Include Atom and Scope Unit facts, direct and derived Relations, Archive allocation metadata, live Lifecycle Run list fields, query history, and published diagnostics. Reuse the same tables for runtime lookups where they serve the same data.

Apply the existing Project binding, retention and read-only rules. Keep pending Run input and private execution state out of SQL. Archive bodies load on demand.
