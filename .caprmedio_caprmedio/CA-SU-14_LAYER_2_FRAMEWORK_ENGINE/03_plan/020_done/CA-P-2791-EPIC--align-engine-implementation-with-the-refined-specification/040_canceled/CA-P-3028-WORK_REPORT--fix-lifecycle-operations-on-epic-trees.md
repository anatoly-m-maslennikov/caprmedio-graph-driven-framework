---
identity:
  atom_id: CA-P-3028
  ref_id: CA-P-3028
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
  - CA-P-3023
state:
  version: 2
  status: canceled
  updated_at: '2026-11-12T02:48:00.186230+00:00'
destination:
  file:
    name: CA-P-3028-WORK_REPORT--fix-lifecycle-operations-on-epic-trees.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/040_canceled
---
## Summary

Fix lifecycle operations on Epic trees

## Details

Verified through MCP in a disposable Project. Changing an Epic from Backlog to Active activated a direct and a nested Current Task. A separate Epic with a Draft child became Active, with the child remaining Draft. A content-only Update created the next Epic Version and preserved both Current children.

Verified image `sha256:7607f7793de81d53b1d68b31c49ebe97c5dde9d2214b2318b44142dec92599f1`.

The full disposable Project also updated CA-P-2791@46 to @47 with 126 Current children. The exact predecessor was loaded while older Archives stayed unloaded. Verified image `sha256:9de655db6d16dc6dd9832b01f5d48d3b50ad072d9d58621774afef84165886ce`.
