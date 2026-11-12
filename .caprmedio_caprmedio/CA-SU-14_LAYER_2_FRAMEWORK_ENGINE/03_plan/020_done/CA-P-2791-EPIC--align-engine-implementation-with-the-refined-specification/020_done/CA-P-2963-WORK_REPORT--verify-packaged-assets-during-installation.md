---
identity:
  id: CA-P-2963
  ref_id: CA-P-2963
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
  updated_at: 2026-11-11 08:43:36 +0400
destination:
  file:
    name: CA-P-2963-WORK_REPORT--verify-packaged-assets-during-installation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2818
author: Anatoly Maslennikov
---

## Summary

Verify packaged assets during installation

## Details

The v4 image passed its build. Installed verification stopped because it recompiled the schema and relation registry after copying the derived Framework. The new bytes differed from the exact candidate's packaged assets.

No-build verification now checks the packaged assets against the immutable image. The release checks that match before replacing the installed Framework or runtime. The corrected verifier accepted the exact v4 image after the copy. Focused tests cover changed, missing and unsafe assets. Evidence is under `.caprmedio_tmp/CA-P-2791/CA-P-2818/release-preflight/`.
