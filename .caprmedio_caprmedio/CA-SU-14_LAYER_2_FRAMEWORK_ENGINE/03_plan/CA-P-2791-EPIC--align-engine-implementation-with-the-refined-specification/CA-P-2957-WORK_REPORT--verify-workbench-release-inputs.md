---
identity:
  id: CA-P-2957
  ref_id: CA-P-2957
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
  updated_at: 2026-11-11 07:57:14 +0400
destination:
  file:
    name: CA-P-2957-WORK_REPORT--verify-workbench-release-inputs.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2818
author: Anatoly Maslennikov
---

## Summary

Verify Workbench release inputs

## Details

Recompiled the schema and canonical relation registry from the current checkout. The schema modes and relation registry match the tested image. Schema input provenance changed. All 175 Engine Python modules from the tested build have matching executable syntax.

The installed Workbench served its page but lacked the declared Content columns. The post-release check now covers those columns, native Declarations and both containment directions through Workbench HTTP and MCP query_run. The assets and check are in `.caprmedio_tmp/CA-P-2791/CA-P-2818/`.
