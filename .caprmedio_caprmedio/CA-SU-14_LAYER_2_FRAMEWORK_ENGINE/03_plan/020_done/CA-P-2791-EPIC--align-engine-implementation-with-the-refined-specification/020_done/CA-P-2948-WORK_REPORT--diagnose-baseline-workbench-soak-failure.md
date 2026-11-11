---
identity:
  id: CA-P-2948
  ref_id: CA-P-2948
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
  updated_at: 2026-11-11 07:15:01 +0400
destination:
  file:
    name: CA-P-2948-WORK_REPORT--diagnose-baseline-workbench-soak-failure.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2817
author: Anatoly Maslennikov
---

## Summary

Diagnose baseline Workbench soak failure

## Details

The d520 soak failed its frozen memory guard after about 21 minutes. Last reported sample at cycle 120 was 554 MiB current and 605 MiB peak. Source and relation inventories, result ownership, threads and file descriptors remained stable. The next Scope Declaration refresh rebuilt 5,000 rows before the failure.

The runner now reports the exact failing sample. The diagnostic will distinguish process allocations from file cache. Evidence: `.caprmedio_tmp/CA-P-2791/CA-P-2817/soak-baseline-failure.json`.
