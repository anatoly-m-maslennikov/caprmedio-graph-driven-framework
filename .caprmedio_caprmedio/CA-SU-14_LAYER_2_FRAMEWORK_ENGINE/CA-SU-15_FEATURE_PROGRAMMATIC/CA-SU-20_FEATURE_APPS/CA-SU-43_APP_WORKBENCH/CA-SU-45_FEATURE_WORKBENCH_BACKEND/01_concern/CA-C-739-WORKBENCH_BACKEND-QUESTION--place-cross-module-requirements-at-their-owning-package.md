---
identity:
  atom_id: CA-C-739
  ref_id: CA-C-739
context:
  role: concern
  form: Question
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
  - CA-M-526@3
state:
  version: 1
  status: active
  updated_at: '2026-11-13T15:59:15.894221+00:00'
destination:
  file:
    name: CA-C-739-WORKBENCH_BACKEND-QUESTION--place-cross-module-requirements-at-their-owning-package.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/01_concern
---
## Summary

Place cross-module Requirements at their owning Package

## Concern

How should the pilot trace a Requirement whose behavior is split across several Modules? CA-R-2727@20 spans `App.svelte` and `ViewTabs.svelte`; CA-R-2776@10 spans `App.svelte` and `SavedPanel.svelte`. Pinning both Requirements in every contributing Module produces many-to-many links. The reviewed policy allows a shared Claim to be pinned once in the smallest owning Package. Should the pilot use that rule for this cluster and reserve Module pins for independently implemented Claims?