---
identity:
  id: CA-P-2973
  ref_id: CA-P-2973
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
  updated_at: 2026-11-11 09:26:28 +0400
destination:
  file:
    name: CA-P-2973-WORK_REPORT--verify-exact-atom-lookup-limits-in-workbench.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2934
author: Anatoly Maslennikov
---

## Summary

Verify exact Atom lookup limits in Workbench

## Details

Installed query_run returns installed copies for CA-R-1521 and CA-R-3010 even though native carriers exist. The same index omits the exact Archived CA-C-730@6 carrier. The retained exact-path reader is suitable after an authority-bound carrier has been selected. The lifecycle Tool still needs authority-bound logical selection for Current, Draft and Archived Atoms. Evidence is in `.caprmedio_tmp/CA-P-2791/CA-P-2934/exact-reference-readback.json`.
