---
atom_id: CA-E-795
ref_id: CA-E-795@1
container:
  scope_unit: CA-SU-45
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 5
status: Archived
version: 1
updated_at: 2026-11-07 03:26:52 +0400
carrier_destination:
  file:
    name: CA-E-795@1-WORKBENCH_BACKEND-EVAL_CASE--verify-opt-in-workbench-profiling-isolation-and-output.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation/archived
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
relations:
  evaluation_for:
  - CA-R-2998
  - CA-M-503
  - CA-D-703
---

## Summary

Verify Workbench profiling isolation and output

## Claim

### Prose Claim

Run the profiler against a small valid disposable Project using the actual DuckDB/DuckPGQ path. Verify readable cProfile statistics, nonempty allocation diagnostics, dataset/cycle counts, explicit instrumented labels, correctly labelled RSS/native memory fields, and identical source-file hashes before and after. Verify output stays within the selected Project temporary root and the disposable database is removed when bounded cleanup succeeds. If cleanup fails, report the confined retained path explicitly; do not retry or lose the original failure. The normal performance gates must run without cProfile or tracemalloc enabled; profiler durations never satisfy their latency or throughput assertions.
