---
identity:
  atom_id: CA-A-1374
  ref_id: CA-A-1374
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
  updated_at: '2026-11-12T12:59:07.219759+00:00'
destination:
  file:
    name: CA-A-1374-FRAMEWORK_ENGINE-CODE_SYNOPSIS--workbench-http-diagnostics-can-hide-a-logging-failure.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Workbench HTTP diagnostics can hide a logging failure

## Claim

### Prose Claim

CA-M-396@17 requires both the primary failure and a secondary diagnostics failure to remain observable. `FEATURE_MCP/workbench_web.py` calls `report_failure` but drops its secondary failure while building the HTTP response. The client sees the primary failure with no indication that its diagnostic could not be recorded.
