---
identity:
  id: CA-P-2970
  ref_id: CA-P-2970@1
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
  status: Archived
  version: 1
  updated_at: 2026-11-11 09:10:46 +0400
destination:
  file:
    name: CA-P-2970@1-WORK_REPORT--prepare-lifecycle-placement-and-status-evaluations.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/archive
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2934
author: Anatoly Maslennikov
---

## Summary

Prepare lifecycle placement and Status evaluations

## Details

Prepared pinned cases for Change Status, Archive and Current Move. The cases resolve through the retained Project reader and bind exact carrier bytes. Change Status and Archive preserve the version metadata. Move binds its source and destination and preserves unrelated files. These are disposable test inputs.

The retained adapters read and pin bytes when given a path. They lack a logical Atom resolver and a Role/Form Status resolver. CA-R-1521 requires Status selection from the applicable model. Sent the declaration check to the Model owner. The fixtures are under `.caprmedio_tmp/CA-P-2791/CA-P-2934/`.
