---
identity:
  atom_id: CA-C-737
  ref_id: CA-C-737
context:
  role: concern
  form: implementation_discrepancy
  concern:
    priority: Medium
  container:
    scope_unit: WORKBENCH_BACKEND
  tier: 3
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
      <+ Traceability
relations:
  CONCERN_ABOUT:
  - CA-P-3057
  - CA-M-1015@1
state:
  version: 1
  status: active
  updated_at: '2026-11-13T15:59:05.041408+00:00'
destination:
  file:
    name: CA-C-737-WORKBENCH_BACKEND-IMPLEMENTATION_DISCREPANCY--editing-a-package-trace-rereads-the-subtree.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/01_concern
---
## Summary

Editing a Package trace rereads the subtree

## Concern

CA-M-1015@1 limits ordinary refreshes to affected object and pin rows. In `FEATURE_WORKBENCH_BACKEND/spec_trace.py`, `refresh` maps a Package trace edit to its parent directory, deletes descendant rows, and rescans the entire Package subtree. One pin edit rereads unrelated descendant traces.