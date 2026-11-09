---
identity:
  atom_id: CA-R-2998
  ref_id: CA-R-2998
context:
  container:
    scope_unit: CA-SU-45
  role: Requirement
  form: Rule
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 3
state:
  status: Active
  version: 3
  updated_at: 2026-11-09 21:15:45 +0400
destination:
  file:
    name: CA-R-2998-WORKBENCH_BACKEND-RULE--profile-workbench-without-changing-source-files.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/04_requirement
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-D-703
  - CA-M-503
---

## Summary

Profile Workbench without changing source files

## Claim

### Prose Claim

An explicitly requested Workbench diagnostic run must report CPU hotspots, Python allocations, process memory and DuckDB-managed memory without changing source files, the live Workbench database or the live MCP process. Profiling is opt-in; ordinary latency, throughput and rebuild acceptance tests run without instrumentation.

## Details

### Profiling execution and artifacts

Run the diagnostic through an explicit development CLI with the selected Project root and an optional output directory constrained beneath that Project's configured temporary root. Write `cpu.pstats` and `report.json` there.

Use cProfile for CPU calls and tracemalloc for Python allocations in a separate diagnostic CLI run. Reuse the current Workbench reader, materializer and QueryStore with an isolated disposable database. Measure the initial index and three full rebuild cycles, closing superseded database owners.

The report includes runtime/build context, dataset and rebuild-cycle counts, instrumented timings, Python current/peak allocation bytes and top allocation traces, process high-water RSS with byte units, and DuckDB-managed buffer memory. State unavailable measurements explicitly; process high-water RSS is not current live memory. Label all profiled durations as instrumented diagnostics rather than performance-acceptance timings.

Add no dependency, background profiler, runtime endpoint or automatic instrumentation. Keep disposable databases separate from source files and the live runtime database, and attempt bounded cleanup on completion or failure. If cleanup is interrupted or denied, report the retained path under the Project temporary root; do not retry or modify source files.
