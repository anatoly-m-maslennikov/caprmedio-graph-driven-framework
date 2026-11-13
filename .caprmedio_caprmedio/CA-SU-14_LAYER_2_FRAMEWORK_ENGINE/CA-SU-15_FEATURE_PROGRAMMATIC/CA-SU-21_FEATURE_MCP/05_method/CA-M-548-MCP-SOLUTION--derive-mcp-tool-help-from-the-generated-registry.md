---
atom_id: CA-M-548
ref_id: CA-M-548
container:
  scope_unit: CA-SU-21
role: Method
form: Solution
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Communication
tier: 2
relations:
  method_for:
  - CA-R-3065
  - CA-R-3013
status: active
version: 2
updated_at: '2026-11-12T16:57:31.214663+00:00'
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-M-548-MCP-SOLUTION--derive-mcp-tool-help-from-the-generated-registry.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method
---
## Summary

Derive mcp tool help from the generated registry

## Claim

### Prose Claim

Use the same generated registry to register public MCP Tools and expose their descriptions and input schemas through `tools/list`. Keep the metadata in the provider descriptors. Apply the global blacklist and Project exclusions when registering Tools.
