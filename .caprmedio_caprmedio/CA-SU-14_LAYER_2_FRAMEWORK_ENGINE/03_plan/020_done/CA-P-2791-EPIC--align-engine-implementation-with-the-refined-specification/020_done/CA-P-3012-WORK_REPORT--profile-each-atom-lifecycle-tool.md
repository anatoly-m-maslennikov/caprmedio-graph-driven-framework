---
identity:
  atom_id: CA-P-3012
  ref_id: CA-P-3012
context:
  role: plan
  form: work_report
  container:
    atom: CA-P-2791
  label: Work Report
  tier: 4
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-3009
state:
  version: 1
  status: done
  updated_at: '2026-11-11T23:42:36.747821+00:00'
destination:
  file:
    name: CA-P-3012-WORK_REPORT--profile-each-atom-lifecycle-tool.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
---
## Summary

Profile each Atom Lifecycle tool

## Details

Profiled all six tools in Docker against a disposable copy of the Project. The old same-ID and replacement Updates took 52.73 and 73.49 seconds. They took 1.29 and 1.56 seconds after the changes. The first Create Draft took 4.41 seconds while loading the carrier index. Other warm calls took 0.21–0.41 seconds. Repeated Project-boundary validation was the largest remaining measured cost.
