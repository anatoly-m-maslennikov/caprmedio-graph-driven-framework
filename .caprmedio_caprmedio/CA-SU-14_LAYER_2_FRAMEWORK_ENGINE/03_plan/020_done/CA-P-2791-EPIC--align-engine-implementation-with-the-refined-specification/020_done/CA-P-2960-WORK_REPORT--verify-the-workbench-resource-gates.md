---
identity:
  id: CA-P-2960
  ref_id: CA-P-2960
context:
  container:
    atom: CA-P-2791
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Atom
  tier: 4
state:
  status: Done
  version: 1
  updated_at: 2026-11-11 08:17:35 +0400
destination:
  file:
    name: CA-P-2960-WORK_REPORT--verify-the-workbench-resource-gates.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2817
author: Anatoly Maslennikov
---

## Summary

Verify the Workbench resource gates

## Details

All nine Docker cases passed against image `sha256:87f745f425bcb3eed2fc8222ff6eaf377d1e6cb6549203cdb6b59bbf342040d2`. Watcher mutations became query-visible in 242.2–316.5 ms on the 5,000-Atom fixture. The 500-Atom and cold-rebuild gates also passed.

The profiler-off soak ran 179 cycles over 1800.00 seconds with the same owner. Peak RAM was 575.2 MiB across all phases, growth above the settled baseline was 43.2 MiB, and idle CPU was 0.027 CPU-seconds over 15 seconds. No OOM kills, retained result tables, pins or watcher work remained. The test used the one-core cap and provides no uncapped peak CPU measurement.

The exact results and limits are in `.caprmedio_tmp/CA-P-2791/CA-P-2817/`.
