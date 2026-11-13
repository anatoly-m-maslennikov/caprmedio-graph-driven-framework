---
identity:
  atom_id: CA-P-3027
  ref_id: CA-P-3027
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
  - CA-P-3016
state:
  version: 1
  status: canceled
  updated_at: '2026-11-12T02:41:19.089256+00:00'
destination:
  file:
    name: CA-P-3027-WORK_REPORT--move-workbench-audits-off-lifecycle-responses.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/040_canceled
---
## Summary

Move Workbench audits off lifecycle responses

## Details

On the ungrouped 50-Atom fixture, synchronous audit work accounted for 0.95 s in Archive and 3.00 s in Promote. The Workbench worker now computes the issue rows in the background and publishes the latest generation. Publishing briefly holds the DuckDB lock. Verified that a blocked audit does not hold a lifecycle response and that the issue tables populate once the audit completes. A full audit finishes once while changed paths queue behind it. The live Update median fell from 8.40 s during repeated full audits to 0.65 s on the final image.

Verified image `sha256:7607f7793de81d53b1d68b31c49ebe97c5dde9d2214b2318b44142dec92599f1`.
