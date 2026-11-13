---
identity:
  atom_id: CA-P-3011
  ref_id: CA-P-3011
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
  - CA-P-3008
state:
  version: 1
  status: canceled
  updated_at: '2026-11-11T23:42:33.311047+00:00'
destination:
  file:
    name: CA-P-3011-WORK_REPORT--apply-method-policies-to-atom-lifecycle.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/040_canceled
---
## Summary

Apply Method policies to Atom Lifecycle

## Details

All six MCP actions use the same Project-bound Workbench SQL backend. The shared reads handle exact and batched revisions, ID allocation, and containment. The action does not walk the Project to select Atom files.
