---
identity:
  atom_id: CA-M-1018
  ref_id: CA-M-1018
context:
  role: method
  form: decision
  container:
    scope_unit: CA-SU-46
  tier: 4
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Projection
relations:
  SPECIALIZES:
  - CA-R-2727@20
state:
  version: 1
  status: active
  updated_at: '2026-11-13T16:24:31.077676+00:00'
destination:
  file:
    name: CA-M-1018-WORKBENCH_FRONTEND-DECISION--render-workbench-view-tabs-in-one-component.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/05_method
---
## Summary

Render Workbench View tabs in one component

## Claim scope

The tab strip in the Workbench frontend.

## Claim

### Prose Claim

Use `ViewTabs.svelte` to render the tab strip and its controls. Pass selection, close, rename and duplicate requests to the Workspace handlers with the selected View ID. Pass New View to the create handler.