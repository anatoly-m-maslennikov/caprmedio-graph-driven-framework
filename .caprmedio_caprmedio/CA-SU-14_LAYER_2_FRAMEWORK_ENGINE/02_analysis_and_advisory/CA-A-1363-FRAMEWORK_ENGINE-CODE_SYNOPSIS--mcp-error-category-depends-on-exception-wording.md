---
identity:
  atom_id: CA-A-1363
  ref_id: CA-A-1363
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
  updated_at: '2026-11-12T12:53:45.141616+00:00'
destination:
  file:
    name: CA-A-1363-FRAMEWORK_ENGINE-CODE_SYNOPSIS--mcp-error-category-depends-on-exception-wording.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

MCP error category depends on exception wording

## Claim

### Prose Claim

CA-M-396@17 prohibits classifying failure by arbitrary human-message substrings. `FEATURE_MCP/shared_gateway.py` maps a HostRuntimeConfigError to an outside-project category when its text contains `outside`. The same exception type carries prose from `FEATURE_TOOLS/host_runtime_config.py`. Wording changes can alter the machine-readable error category.
