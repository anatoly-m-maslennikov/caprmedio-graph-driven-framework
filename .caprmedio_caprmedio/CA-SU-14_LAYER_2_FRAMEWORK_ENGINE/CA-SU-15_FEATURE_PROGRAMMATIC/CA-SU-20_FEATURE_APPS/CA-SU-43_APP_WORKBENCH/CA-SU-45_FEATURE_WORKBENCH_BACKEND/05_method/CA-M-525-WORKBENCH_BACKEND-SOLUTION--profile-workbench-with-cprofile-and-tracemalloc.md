---
identity:
  atom_id: CA-M-525
  ref_id: CA-M-525
context:
  container:
    scope_unit: CA-SU-45
  role: Method
  form: Solution
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
      <+ Performance <+ Measurement and Profiling
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 4
state:
  status: Active
  version: 1
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-525-WORKBENCH_BACKEND-SOLUTION--profile-workbench-with-cprofile-and-tracemalloc.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method
relations:
  method_for:
  - CA-R-2998
author: Anatoly Maslennikov
---
## Summary

Profile Workbench with cProfile and tracemalloc

## Claim

### Prose Claim

Run the diagnostic through an explicit development CLI with the selected Project root and optional output directory constrained beneath its configured temporary root. Write `cpu.pstats` and `report.json` there. Use cProfile and tracemalloc in a separate CLI run over the current reader, materializer and QueryStore with an isolated disposable database; measure initial indexing and three full rebuild cycles, closing superseded owners. Add no dependency, endpoint, background profiler or automatic instrumentation. Keep disposable databases separate from sources/live runtime and attempt bounded cleanup; if cleanup is interrupted or denied, report the confined retained path without retrying or modifying sources.
