---
atom_id: CA-M-341
ref_id: CA-M-341@13
container:
  scope_unit: CA-SU-21
role: Method
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
    Structure
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime/Session
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Recovery
tier: 4
relations:
  method_for:
  - CA-R-1884
status: Archived
version: 13
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-M-341@13-MCP-DECISION--reuse-the-hot-reload-gateway-for-http.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method/archive
current_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

reuse the hot-reload Gateway for HTTP

## Claim

### Prose Claim

the HTTP transport implementation **must** reuse the Gateway's existing server handlers and generation lifecycle, so transport selection does not independently redefine Tool behavior.

## Details

### Scope

the additional localhost HTTP transport for the existing Project MCP Gateway.

1. factor one server-construction boundary for stdio and HTTP; keep implementation generations on their existing subprocess stdio connection.
2. use the installed MCP SDK's Streamable HTTP ASGI application and forward its lifespan; preserve stateful Sessions and the existing reload notifications.
3. close HTTP Sessions and all Gateway generations on shutdown. Do not replay interrupted Tool calls during reload or shutdown.
