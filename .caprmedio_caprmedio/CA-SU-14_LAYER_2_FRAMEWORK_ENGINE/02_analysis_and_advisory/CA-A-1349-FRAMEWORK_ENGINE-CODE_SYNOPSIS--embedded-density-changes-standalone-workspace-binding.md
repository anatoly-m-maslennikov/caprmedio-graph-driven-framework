---
identity:
  atom_id: CA-A-1349
  ref_id: CA-A-1349
context:
  role: analysis_and_advisory
  form: code_synopsis
  tier: 4
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Frontend Engineering
  container:
    scope_unit: FRAMEWORK_ENGINE
state:
  version: 1
  status: active
  updated_at: '2026-11-12T12:49:08.170980+00:00'
destination:
  file:
    name: CA-A-1349-FRAMEWORK_ENGINE-CODE_SYNOPSIS--embedded-density-changes-standalone-workspace-binding.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Embedded density changes standalone Workspace binding

## Claim

### Prose Claim

In the CAPRMEDIO working tree based on `c0b983cb27`, `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_FRONTEND/src/App.svelte`, `standaloneContext`, uses `embedded=1` when deciding whether to persist or create a standalone Workspace ID. It also derives the displayed Project name from the URL path. Workspace initialization renders that name without requiring the name returned by Workspace Open or Get. CA-R-2902@9 requires `embedded=1` to set density only and requires the response Project name as the display source. With no explicit Workspace ID, the density marker can change binding and a missing response name is not reported.
