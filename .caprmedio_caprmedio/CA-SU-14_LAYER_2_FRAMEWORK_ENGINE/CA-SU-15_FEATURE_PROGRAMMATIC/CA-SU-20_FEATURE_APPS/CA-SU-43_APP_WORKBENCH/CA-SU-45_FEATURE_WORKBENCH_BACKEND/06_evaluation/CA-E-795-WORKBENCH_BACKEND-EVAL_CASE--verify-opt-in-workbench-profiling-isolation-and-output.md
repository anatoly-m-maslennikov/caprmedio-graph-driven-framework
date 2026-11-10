---
identity:
  atom_id: CA-E-795
  ref_id: CA-E-795
context:
  container:
    scope_unit: CA-SU-45
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
      <+ Performance <+ Measurement and Profiling
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 5
relations:
  evaluation_for:
  - CA-R-2998
  - CA-M-525
state:
  status: Active
  version: 5
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-795-WORKBENCH_BACKEND-EVAL_CASE--verify-opt-in-workbench-profiling-isolation-and-output.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Verify Workbench profiling isolation and output

## Claim

### Prose Claim

Run the profiler through the actual DuckDB/DuckPGQ path on a small valid disposable Project. Verify readable cProfile statistics, nonempty allocation diagnostics, dataset/cycle counts, explicit instrumented labels, correct RSS/native-memory labels and identical source hashes before/after. Output remains beneath the selected Project temporary root; bounded cleanup removes the disposable database, or reports its confined retained path without retrying or losing the original failure. Normal performance gates run without cProfile/tracemalloc, and profiler duration never satisfies latency/throughput assertions.
