---
atom_id: CA-M-503
ref_id: CA-M-503@1
container:
  scope_unit: CA-SU-45
role: Method
form: Eng Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 4
status: Archived
version: 1
updated_at: 2026-11-07 03:26:51 +0400
carrier_destination:
  file:
    name: CA-M-503@1-WORKBENCH_BACKEND-ENG_DECISION--use-standard-library-opt-in-workbench-profiling.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method/archived
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
relations:
  method_for:
  - CA-R-2998
---

## Summary

Use standard-library opt-in Workbench profiling

## Claim

### Prose Claim

Use cProfile for CPU calls and tracemalloc for Python allocations in a separate diagnostic CLI run. Reuse the current Workbench reader, materializer and QueryStore with an isolated disposable database. Measure the initial index and three full rebuild cycles; close superseded database owners. Report tracemalloc current/peak Python allocation bytes, process high-water RSS bytes and DuckDB-managed buffer bytes separately. Mark unavailable native measurements unavailable; process high-water RSS is not current live memory. Label all profiled durations as instrumented diagnostics, not performance acceptance timings. Add no dependency, background profiler, runtime endpoint or automatic instrumentation.
