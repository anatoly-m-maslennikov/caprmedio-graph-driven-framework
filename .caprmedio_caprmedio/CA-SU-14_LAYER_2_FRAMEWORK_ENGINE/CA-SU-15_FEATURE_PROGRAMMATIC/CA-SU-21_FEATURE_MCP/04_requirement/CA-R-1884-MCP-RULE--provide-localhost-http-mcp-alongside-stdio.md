---
atom_id: CA-R-1884
content_role: Requirement
current_scope_unit: MCP
status: Active
author: Anatoly Maslennikov
version: 14
updated_at: 2026-10-27 20:00:05 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
relations: {}
tier: 3
type: Rule
---
# Summary

provide localhost HTTP MCP alongside stdio

## Scope

the additional localhost HTTP transport for the existing Project MCP Gateway.

## Claim

MCP **must** provide an explicitly started localhost HTTP endpoint alongside the existing stdio connection, exposing the same admitted Tool capabilities through the existing hot-reload Gateway.

## Details

1. keep stdio available with its current default behavior; HTTP is an additional transport, not another Tool registry or implementation server.
2. preserve generation routing, in-flight draining, reload control and truthful client-refresh status across HTTP calls.
3. starting the endpoint provides a capability; it does not start a Workflow or infer its completion.
