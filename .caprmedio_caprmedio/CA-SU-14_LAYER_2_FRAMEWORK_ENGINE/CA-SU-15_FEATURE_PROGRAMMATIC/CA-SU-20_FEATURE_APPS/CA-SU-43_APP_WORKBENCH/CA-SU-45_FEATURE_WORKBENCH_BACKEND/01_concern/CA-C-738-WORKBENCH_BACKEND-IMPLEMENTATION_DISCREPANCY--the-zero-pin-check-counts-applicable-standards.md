---
identity:
  atom_id: CA-C-738
  ref_id: CA-C-738
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
  updated_at: '2026-11-13T15:59:08.882153+00:00'
destination:
  file:
    name: CA-C-738-WORKBENCH_BACKEND-IMPLEMENTATION_DISCREPANCY--the-zero-pin-check-counts-applicable-standards.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/01_concern
---
## Summary

The zero-pin check counts applicable standards

## Concern

CA-M-1015@1 excludes `applies` pins from implementation coverage. The draft test at `APP_WORKBENCH/tests/test_spec_trace_e2e.py` checks zero pins without filtering to `implements`. Its fixture lacks an Applies-only Package, so the check cannot distinguish coverage from applicability.