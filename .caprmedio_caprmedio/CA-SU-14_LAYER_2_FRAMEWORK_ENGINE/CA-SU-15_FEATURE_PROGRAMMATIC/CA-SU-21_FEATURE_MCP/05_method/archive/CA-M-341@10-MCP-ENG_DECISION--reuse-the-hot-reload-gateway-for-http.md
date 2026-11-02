---
atom_id: CA-M-341@10
content_role: Method
current_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 10
updated_at: 2026-10-26 00:46:35 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Architecture/Communication
  depends_on:
  - Subject/Graph Node/Engineering/MCP
  - Subject/Graph Node/Engineering/HTTP
  - Subject/Graph Node/Engineering/Gateway
  - Subject/Graph Node/Engineering/MCP.HTTP Transport
  - Subject/Graph Node/Engineering/Generation
  - Subject/Graph Node/Engineering/Occurrent/Session
  - Subject/Graph Node/Engineering/MCP/Implementation Reload
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
