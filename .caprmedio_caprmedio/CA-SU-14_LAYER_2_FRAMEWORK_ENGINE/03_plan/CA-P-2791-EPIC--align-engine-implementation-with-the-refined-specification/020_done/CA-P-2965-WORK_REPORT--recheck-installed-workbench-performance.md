---
identity:
  id: CA-P-2965
  ref_id: CA-P-2965
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
  updated_at: 2026-11-11 08:58:17 +0400
destination:
  file:
    name: CA-P-2965-WORK_REPORT--recheck-installed-workbench-performance.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2817
author: Anatoly Maslennikov
---

## Summary

Recheck installed Workbench performance

## Details

All three targeted Docker checks passed on the installed 0.4.4.43 image. The 12 watcher mutations became query-visible in 238.7–318.0 ms. The 500-Atom batches, cold index and reread passed their fixed limits. Scope rename took 32.6 seconds against its 60-second limit.

The short guard peaked at 505.0 MiB with no OOM, result table, pin or watcher-work leak. The 30-minute soak is recorded separately in P2960. Evidence is in `.caprmedio_tmp/CA-P-2791/CA-P-2817/installed-v5-resource-acceptance.json`.
