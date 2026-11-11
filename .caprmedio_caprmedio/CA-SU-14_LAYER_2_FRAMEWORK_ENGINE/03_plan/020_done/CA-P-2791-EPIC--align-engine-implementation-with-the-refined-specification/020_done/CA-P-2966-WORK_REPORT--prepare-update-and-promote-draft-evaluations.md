---
identity:
  id: CA-P-2966
  ref_id: CA-P-2966
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
  updated_at: 2026-11-11 08:58:18 +0400
destination:
  file:
    name: CA-P-2966-WORK_REPORT--prepare-update-and-promote-draft-evaluations.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2934
author: Anatoly Maslennikov
---

## Summary

Prepare Update and Promote Draft evaluations

## Details

Prepared two disposable lifecycle cases. A same-ID Update preserves the predecessor's Resolved status and publishes version 5 from version 4. A many-to-one promotion archives the Current target once, preserves the already Archived target and publishes the Draft.

The pinned inputs and validator are in `.caprmedio_tmp/CA-P-2791/CA-P-2934/promotion-fixtures/`. Fixture validation passed. Both cases still need to run through the admitted Tool interface.
