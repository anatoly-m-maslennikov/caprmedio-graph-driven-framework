---
atom_id: CA-M-341
content_role: Method
current_scope_unit: MCP
status: Active
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Architecture/Communication
  depends_on:
  - Subject/Graph Node/Implementation
  - Subject/Graph Node/Engineering/Architecture/Communication
  - Subject/Graph Node/Engineering/Architecture/Component Structure
  - Subject/Graph Node/Runtime/Session
  - Subject/Graph Node/Engineering/Execution Control/Recovery
relations:
  method_for:
  - CA-R-1884
type: Eng Decision
tier: 4
---
# Summary

reuse the hot-reload Gateway for HTTP

## Scope

the additional localhost HTTP transport for the existing Project MCP Gateway.

## Claim

the HTTP transport implementation **must** reuse the Gateway's existing server handlers and generation lifecycle, so transport selection does not independently redefine Tool behavior.

## Details

1. factor one server-construction boundary for stdio and HTTP; keep implementation generations on their existing subprocess stdio connection.
2. use the installed MCP SDK's Streamable HTTP ASGI application and forward its lifespan; preserve stateful Sessions and the existing reload notifications.
3. close HTTP Sessions and all Gateway generations on shutdown. Do not replay interrupted Tool calls during reload or shutdown.
