---
atom_id: CA-R-1884
ref_id: CA-R-1884@14
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
    Structure
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
tier: 3
status: Archived
version: 14
updated_at: 2026-10-27 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-1884@14-MCP-RULE--provide-localhost-http-mcp-alongside-stdio.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement/archive
current_scope_unit: MCP
author: Anatoly Maslennikov
---
## Summary

provide localhost HTTP MCP alongside stdio

## Claim scope

the additional localhost HTTP transport for the existing Project MCP Gateway.

## Claim

### Prose Claim

MCP **must** provide an explicitly started localhost HTTP endpoint alongside the existing stdio connection, exposing the same admitted Tool capabilities through the existing hot-reload Gateway.

## Details

1. keep stdio available with its current default behavior; HTTP is an additional transport, not another Tool registry or implementation server.
2. preserve generation routing, in-flight draining, reload control and truthful client-refresh status across HTTP calls.
3. starting the endpoint provides a capability; it does not start a Workflow or infer its completion.
