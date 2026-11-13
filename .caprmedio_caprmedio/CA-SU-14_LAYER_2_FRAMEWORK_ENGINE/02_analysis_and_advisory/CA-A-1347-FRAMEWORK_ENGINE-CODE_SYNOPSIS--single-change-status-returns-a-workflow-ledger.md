---
identity:
  atom_id: CA-A-1347
  ref_id: CA-A-1347
context:
  role: analysis_and_advisory
  form: code_synopsis
  tier: 4
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Atom
  container:
    scope_unit: FRAMEWORK_ENGINE
state:
  version: 1
  status: active
  updated_at: '2026-11-12T12:48:57.188890+00:00'
destination:
  file:
    name: CA-A-1347-FRAMEWORK_ENGINE-CODE_SYNOPSIS--single-change-status-returns-a-workflow-ledger.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Single Change Status returns a workflow ledger

## Claim

### Prose Claim

In the CAPRMEDIO working tree based on `c0b983cb27`, `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/registry_lifecycle_provider.py`, `_result`, includes the Workflow binding, Run ID, Action results, artifact and effects when a successful Change Status response has a Workflow binding. `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/ATOM_LIFECYCLE/status_cascade.py` supplies that binding for a single leaf as well as a cascade. CA-R-1105@31 limits successful single-Atom lifecycle responses to Status. The public response contains more fields even for the leaf case.
