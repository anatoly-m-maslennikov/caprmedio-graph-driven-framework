---
atom_id: CA-R-1884@2
content_role: Requirement
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: 2026-10-23 03:06:32 +0400
subjects:
  governs: MCP/HTTP endpoint
  depends_on:
  - MCP
  - HTTP
  - Tool
  - Gateway
  - Implementation
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
relations:
  relates_to:
  - CA-R-1118
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
