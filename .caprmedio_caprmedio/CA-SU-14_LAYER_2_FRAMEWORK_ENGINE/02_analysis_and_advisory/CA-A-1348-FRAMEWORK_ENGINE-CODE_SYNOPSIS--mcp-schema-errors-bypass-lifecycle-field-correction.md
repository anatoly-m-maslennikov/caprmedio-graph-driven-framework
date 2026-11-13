---
identity:
  atom_id: CA-A-1348
  ref_id: CA-A-1348
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
  updated_at: '2026-11-12T12:49:04.420687+00:00'
destination:
  file:
    name: CA-A-1348-FRAMEWORK_ENGINE-CODE_SYNOPSIS--mcp-schema-errors-bypass-lifecycle-field-correction.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

MCP schema errors bypass lifecycle field correction

## Claim

### Prose Claim

In the CAPRMEDIO working tree based on `c0b983cb27`, `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/tool_registry_runtime.py`, `ActiveToolRegistry.call`, validates the outer schema before invoking the lifecycle provider. `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/direct_gateway.py`, `_input_rejection`, returns generic `tool_input_invalid` for an unknown field or an invalid outer field type. Those requests never reach the pending-input path in `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/registry_lifecycle_provider.py`. CA-R-1105@31 and CA-M-167@26 require field-level errors and correction input in the MCP response. Business field correction reaches that path, while outer schema rejection does not.
