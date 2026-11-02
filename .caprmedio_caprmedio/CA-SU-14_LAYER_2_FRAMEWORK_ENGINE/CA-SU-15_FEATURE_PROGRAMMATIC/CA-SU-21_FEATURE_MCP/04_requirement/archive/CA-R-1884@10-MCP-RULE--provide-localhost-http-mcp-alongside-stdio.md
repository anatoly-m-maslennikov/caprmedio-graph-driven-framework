---
atom_id: CA-R-1884@10
content_role: Requirement
current_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 10
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Engineering/MCP
  depends_on:
  - Subject/Graph Node/Engineering/MCP
  - Subject/Graph Node/Engineering/HTTP
  - Subject/Graph Node/Engineering/MCP.Localhost HTTP Transport
  - Subject/Graph Node/Engineering/Gateway
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
relations:
  relates_to:
  - CA-R-1118
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
