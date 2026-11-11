---
identity:
  id: CA-P-2972
  ref_id: CA-P-2972
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
  updated_at: 2026-11-11 09:24:07 +0400
destination:
  file:
    name: CA-P-2972-WORK_REPORT--check-the-installed-schema-boundary-for-lifecycle-status.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2934
author: Anatoly Maslennikov
---

## Summary

Check the installed schema boundary for lifecycle Status

## Details

Tested the Workbench Header compiler with the native base and Code Synopsis declarations. It delivers a Status column format, but no allowed values or qualified Status domain. The separate graph projection extractor rejects the qualified literal and does not feed the lifecycle adapters. Installed query_run shows the two expected Status columns. Evidence is in `.caprmedio_tmp/CA-P-2791/CA-P-2934/status-formal-candidates/workbench-header-compiler-status.json`. CA-C-730 still tracks the required lifecycle Status input.
