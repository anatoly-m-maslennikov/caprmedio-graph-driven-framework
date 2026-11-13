---
atom_id: CA-M-506
ref_id: CA-M-506
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
  - CA-R-3013
  - CA-R-1108
status: active
version: 8
updated_at: '2026-11-12T12:32:35.944897+00:00'
carrier_destination:
  file:
    name: CA-M-506-MCP-SOLUTION--register-mcp-tools-from-installed-code-and-generated-configuration.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method
current_scope_unit: MCP
author: Anatoly Maslennikov
---
## Summary

Register MCP tools from installed code and generated configuration

## Claim

### Prose Claim

MCP exposure comes from installed code and configuration. Maintain an explicit code-owned provider inventory and generate the deterministic registration asset in refresh mode before image assembly. In existing mode, use the checkout registration asset unchanged. Derive descriptions and typed schemas from provider code, never Atom content, Tool folders, Project scans, or source-Workflow manifests.

At startup load that asset and register enabled providers/routes. A source Atom edit alone cannot change exposure; preserve Project selection, global/configured exclusions, duplicate-name checks, typed request/result validation, and public protocols. Each operation retains its own business validation; route exposure does not assert prerequisites. Native Workbench tools remain available through installed registrations, while retired adapters stay absent.

A missing/invalid asset is an explicit configuration error: do not fall back to Atom discovery. tools/list describes admitted registration after exclusions and does not authorize providers. Code changes require a normal server/container restart. MCP and Workbench are transport adapters over the same in-process backend/canonical Tool APIs; MCP translates protocol data but adds no business copy, internal HTTP hop, or second server. Use the official MCP Python SDK.

Keep provider/factory and descriptor-factory bindings in the editable installed inventory. Generate names/schemas from installed provider code; adding or changing a provider and regenerating must not require a central gateway allowlist/dispatch branch. Apply global mcp_blacklist and bound Project exclusions at publication and on every invocation.
