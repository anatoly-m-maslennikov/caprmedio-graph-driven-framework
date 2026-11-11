---
atom_id: CA-E-799
ref_id: CA-E-799@2
container:
  scope_unit: CA-SU-43
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 6
relations:
  is_evaluation_for:
  - CA-M-508
  - CA-R-2723
  relates_to:
  - CA-E-677
status: Archived
version: 2
updated_at: 2026-11-07 13:56:40 +0000
carrier_destination:
  file:
    name: CA-E-799@2-WORKBENCH-EVAL_CASE--verify-profiler-off-workbench-resource-regression-guards.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation/archived
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Verify profiler-off Workbench resource regression guards

## Claim

Run the existing disposable 5,000-Atom Workbench Docker fixture with `tracemalloc` and CPU profiling disabled. Take cgroup snapshots immediately before and after cold index, warm full reread and a true 15-second idle interval. Verify frozen controlled-fixture limits for those CPU interval deltas and current RAM values, plus the separate cumulative peak-RAM ceiling. Verify no cgroup OOM kill.

Run a bounded View lifecycle that reruns one View and removes it. Confirm each rerun drops the previous result immediately. After removal, confirm the result is unpinned and remains only while it is younger than the configured TTL; after TTL cleanup, confirm no result table or pin remains. Preserve the existing latency and throughput assertions unchanged.

## Details

Record every measured limit, value, fixture size, image and phase in test output. A calibration run may propose limits but does not pass or change the frozen limits. The test does not use the opt-in profiler or a production diagnostic endpoint.

Keep an anchor View open beyond the short fixture TTL and verify that its owned result table remains available. Closing that View releases its pin; only after TTL cleanup must its table disappear.
