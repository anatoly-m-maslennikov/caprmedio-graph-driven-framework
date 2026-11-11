---
identity:
  id: CA-P-2945
  ref_id: CA-P-2945
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
  updated_at: 2026-11-11 06:58:03 +0400
destination:
  file:
    name: CA-P-2945-WORK_REPORT--prepare-direct-update-verification-fixtures.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2934
author: Anatoly Maslennikov
---

## Summary

Prepare Direct Update verification fixtures

## Details

The disposable Draft, Current and Archived fixtures pin exact identity, Version, Updated At and source and expected readback hashes. The retained parser verified the source and in-memory replacements. Cases also cover invalid values, stale state and duplicate identity.

C730 records the Version and history conflict before a persisted effect can be verified. Evidence: `.caprmedio_tmp/CA-P-2791/CA-P-2934/direct-update-fixtures/manifest.json`.
