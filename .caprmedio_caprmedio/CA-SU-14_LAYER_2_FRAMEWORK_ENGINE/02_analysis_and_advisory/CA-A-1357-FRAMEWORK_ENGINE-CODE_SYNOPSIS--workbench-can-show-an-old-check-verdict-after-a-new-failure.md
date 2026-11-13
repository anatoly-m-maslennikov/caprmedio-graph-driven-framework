---
identity:
  atom_id: CA-A-1357
  ref_id: CA-A-1357
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
  updated_at: '2026-11-12T12:53:27.079173+00:00'
destination:
  file:
    name: CA-A-1357-FRAMEWORK_ENGINE-CODE_SYNOPSIS--workbench-can-show-an-old-check-verdict-after-a-new-failure.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Workbench can show an old Check verdict after a new failure

## Claim

### Prose Claim

CA-M-466@9 requires truthful stale and error states. `FEATURE_WORKBENCH_FRONTEND/src/App.svelte` keeps and displays the previous Check verdict across a query edit and a failed Check. A View can show a Valid verdict alongside an error for the current query.
