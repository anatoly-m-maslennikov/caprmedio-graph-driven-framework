---
identity:
  atom_id: CA-M-508
  ref_id: CA-M-508@6
context:
  container:
    scope_unit: CA-SU-43
  role: Method
  form: Decision
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Quality <+ Performance
      <+ Measurement and Profiling
    dependencies:
    - CAPRMEDIO_MODEL <+ Projection
  tier: 5
relations:
  is_method_for:
  - CA-R-2723
  - CA-R-2786
state:
  status: Archived
  version: 6
  updated_at: 2026-11-09 07:45:15 +0400
destination:
  file:
    name: CA-M-508@6-WORKBENCH-DECISION--guard-workbench-resources-with-profiler-off-docker-checks.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method/archive
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Guard Workbench resources with profiler-off Docker checks

## Claim

### Prose Claim

Measure Workbench resource regressions in the existing controlled 5,000-Atom Docker fixture with allocation and CPU profiling disabled. Record cgroup CPU interval deltas and current RAM for cold index and warm full reread. Record the separate cumulative cgroup peak-RAM ceiling. Record cgroup CPU interval work and current RAM across a true 15-second idle interval without in-container polling.

Calibrate numeric resource limits once on that controlled fixture, then freeze them as the limits below. Do not raise a limit automatically from a later run. Preserve the existing 1.5-second single-operation, 500-Atom throughput, cold-index and full-reread gates.

Keep a short resource check in the normal Workbench Docker suite. Keep the 30-minute leak soak opt-in. Neither check adds a production endpoint, profiler, retry, scheduler or live Project source mutation.

## Details

The short check uses the existing disposable source fixture and Docker ownership boundary. It checks cgroup `oom_kill`, resource values at phase boundaries, and the current result-table inventory after View reruns and removal.

The opt-in soak keeps one identified Workbench owner and process alive continuously for at least 1,800 seconds. It creates, updates, renames, moves and removes fixture sources; changes schema; runs successful and failed queries; reruns and removes Views; then drains asynchronous work. It measures fixed quiescent windows without forced garbage collection or a reread/reset. It reports a stable plateau separately from allocator retention. A persistent growth trend, a nonempty orphan result-table inventory, retained pin after View removal, undrained watcher work, owner replacement or an OOM event fails the evaluation. Only after the final pre-reset ownership and resource assertions may the soak call `workbench_reread` through the real Workbench Tool boundary.

## Controlled-fixture limits

The selected 5,000-Atom fixture runs in a disposable Docker container capped at one CPU and 1,536 MiB RAM. Its fixed regression limits are:

- Cold index and each complete reread: at most 25 CPU-seconds and 45 wall-seconds.
- Current cgroup RAM: at most 576 MiB.
- Cumulative cgroup peak RAM: at most 640 MiB.
- True 15-second idle interval: at most 0.75 CPU-seconds.
- Positive current-RAM growth above the settled warm baseline: at most 64 MiB, without forced garbage collection.
- No OOM kills, unowned result tables, leaked View pins, leftover removed-source cache keys or undrained work.

These are regression limits for this recorded fixture and runtime cap, not universal Project limits. Calibrate before acceptance when the fixed workload or runtime boundary changes; never raise limits to turn a regression green. The 30-minute phase keeps the same process and owner throughout. Full reread follows its final leak check.

A fall in current RAM is not growth. Report the full high-to-low spread separately; it cannot fail the growth check merely because the allocator or kernel released memory. The current-RAM and cumulative peak ceilings still apply.
