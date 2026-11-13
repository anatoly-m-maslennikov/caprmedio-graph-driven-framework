---
identity:
  id: CA-P-2991
  ref_id: CA-P-2991
context:
  container:
    atom: CA-P-2791
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: canceled
  version: 1
  updated_at: 2026-11-11 18:11:27 +0400
destination:
  file:
    name: CA-P-2991-WORK_REPORT--select-lifecycle-placement-sources-by-main-subject-and-role.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/040_canceled
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2934
author: Anatoly Maslennikov
---

## Summary

Select lifecycle placement sources by Main Subject and Role

## Details

Used query_run to check the Active Delivery filter for Carrier and Atom Status Main Subjects. The image compiler applies these filters to the staged native Core and gets paths only from the selected Formal Claims. Atom IDs and versions record provenance. The live index can return older duplicate copies.

The local image rebuilt and its five packaged source hashes matched native carriers. All 85 lifecycle tests passed. All six Tools and the terminal Plan cascade passed through an isolated MCP gateway.
