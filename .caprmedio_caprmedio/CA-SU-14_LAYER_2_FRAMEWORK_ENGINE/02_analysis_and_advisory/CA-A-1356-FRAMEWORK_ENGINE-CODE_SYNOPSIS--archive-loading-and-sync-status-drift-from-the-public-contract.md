---
identity:
  atom_id: CA-A-1356
  ref_id: CA-A-1356
context:
  role: analysis_and_advisory
  form: code_synopsis
  tier: 4
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Architecture <+ Communication <+ Interface Contracts
  container:
    scope_unit: FRAMEWORK_ENGINE
state:
  version: 1
  status: active
  updated_at: '2026-11-12T12:53:23.967662+00:00'
destination:
  file:
    name: CA-A-1356-FRAMEWORK_ENGINE-CODE_SYNOPSIS--archive-loading-and-sync-status-drift-from-the-public-contract.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Archive loading and sync status drift from the public contract

## Claim

### Prose Claim

CA-D-718@1 names `/api/archive-load` below the Project page. `FEATURE_MCP/workbench_web.py` and the browser transport both use `/archive-load`. CA-R-2952@4 and CA-E-781@4 require a two-field status response, while CA-D-715@3 and CA-D-718@1 require additional audit and Archive coverage fields. `FEATURE_WORKBENCH_BACKEND/service.py` returns the additive shape. Consumers following the route stated in the Delivery cannot invoke Archive loading through it.
