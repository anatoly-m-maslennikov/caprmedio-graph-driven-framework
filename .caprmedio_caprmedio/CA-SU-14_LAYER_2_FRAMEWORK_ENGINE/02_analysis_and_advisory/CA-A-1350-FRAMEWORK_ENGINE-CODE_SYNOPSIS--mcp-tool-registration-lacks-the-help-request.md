---
identity:
  atom_id: CA-A-1350
  ref_id: CA-A-1350
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
  version: 2
  status: active
  updated_at: '2026-11-12T12:58:26.948837+00:00'
destination:
  file:
    name: CA-A-1350-FRAMEWORK_ENGINE-CODE_SYNOPSIS--mcp-tool-registration-lacks-the-help-request.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

MCP Tool registration lacks the help request

## Claim

### Prose Claim

In the CAPRMEDIO working tree based on `c0b983cb27`, `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/shared_tool_contract.py`, `public_tool`, and `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/tool_registry_runtime.py`, `ActiveToolRegistry.call`, expose and validate normal Tool arguments. The generated Tool registry and dispatch have no separate `help: true` request. CA-R-3065@1, CA-M-548@1 and CA-D-714@1 require Tool help before normal business validation. An ordinary MCP Tool request with help is rejected by the current schema.
