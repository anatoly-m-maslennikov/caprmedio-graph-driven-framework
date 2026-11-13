---
identity:
  atom_id: CA-C-735
  ref_id: CA-C-735
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
  updated_at: '2026-11-13T15:58:31.899009+00:00'
destination:
  file:
    name: CA-C-735-WORKBENCH_BACKEND-IMPLEMENTATION_DISCREPANCY--workbench-does-not-publish-spec-trace-tables.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/01_concern
---
## Summary

Workbench does not publish spec trace tables

## Concern

CA-M-1015@1 requires Workbench to publish Implementation objects and RMEDO pins through its query interface and keep them current as files change. The checkout defines a draft store in `FEATURE_WORKBENCH_BACKEND/spec_trace.py`. The startup and watcher in `service_indexing.py` do not call it, and `query_schema.py` omits both trace tables.