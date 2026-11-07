---
atom_id: CA-M-506
ref_id: CA-M-506
container:
  scope_unit: CA-SU-21
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
tier: 2
relations:
  method_for:
  - CA-R-1106
  - CA-R-1108
status: Active
version: 1
updated_at: 2026-11-07 13:08:03 +0400
carrier_destination:
  file:
    name: CA-M-506-MCP-ENG_DECISION--register-mcp-tools-from-installed-code-and-generated-configuration.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method
current_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

Register MCP tools from installed code and generated configuration

## Claim

### Prose Claim

MCP tool exposure comes from installed code and configuration. Keep an explicit code-owned provider inventory and generate its deterministic runtime registration asset on every local release and image rebuild, before the server starts. Derive provider descriptions and typed schemas from code; do not derive eligibility from Atom content, Tool folders, or a Project graph scan.

At startup, read the generated registration asset and register enabled providers and code-owned route names. Do not build a full Atom catalog, load a source-Workflow manifest to select exposed names, or reread an Atom catalog before a generic Tool call. A source Atom edit alone does not add, remove or change MCP exposure. Preserve Project selection, configured exclusions, duplicate-name checks, typed request/result validation and existing public call protocols.

Each operation retains its own input, source and business validation when it runs. Exposing a route does not claim that its business prerequisites are currently satisfied. Native Workbench tools and deterministic Workflow execution remain available through their existing code-owned registrations.

A missing or invalid generated registration asset is an explicit configuration error; do not fall back to Atom discovery. Keep generated tools/list discovery output separate: it describes the actual released MCP surface after readiness and does not authorize registration. Code hot reload remains optional and disabled by default.
