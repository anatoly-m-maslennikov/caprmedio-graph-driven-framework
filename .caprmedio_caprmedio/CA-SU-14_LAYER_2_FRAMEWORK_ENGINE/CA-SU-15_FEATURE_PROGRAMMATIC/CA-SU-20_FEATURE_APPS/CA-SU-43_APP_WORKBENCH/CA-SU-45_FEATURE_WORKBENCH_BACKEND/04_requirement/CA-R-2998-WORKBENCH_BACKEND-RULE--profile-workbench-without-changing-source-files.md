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
    main_subject: MODEL//CAPRMEDIO <+ Projection
  tier: 3
state:
  status: Active
  version: 4
  updated_at: 2026-11-10 20:47:54 +0400
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

The report records runtime/build context, dataset and rebuild-cycle counts, instrumented timings, Python current/peak allocation bytes and top traces, process high-water RSS with byte units, and DuckDB-managed buffer memory. State unavailable measurements explicitly; RSS is not current live memory, and profiled durations are diagnostics rather than performance-acceptance timings.
