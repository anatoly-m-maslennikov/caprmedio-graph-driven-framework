---
atom_id: CA-M-357@11
content_role: Method
current_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-26 00:46:35 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Architecture/Communication
  depends_on:
  - Subject/Graph Node/Engineering/MCP
  - Subject/Graph Node/Engineering/HTTP
  - Subject/Graph Node/Engineering/HTTP/Request
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Engineering/Permission
  - Subject/Graph Node/Engineering/Occurrent/Session
relations:
  method_for:
  - CA-R-1885
type: Eng Decision
tier: 4
---
# Summary

bound localhost HTTP MCP Requests

## Scope

the additional localhost HTTP transport for the existing Project MCP Gateway.

## Claim

the HTTP access implementation **must** validate the loopback Host/Origin boundary before the existing MCP handlers receive a Request, without password, bearer, or other HTTP authentication.

## Details

1. use a narrow ASGI loopback Host/Origin guard for every HTTP Request, including Session continuations. Forward lifespan unchanged.
2. enable the MCP SDK's DNS-rebinding protection explicitly; a container bind address of `0.0.0.0` does not disable Host/Origin validation.
3. do not read, require, validate, rotate, inject, or report an HTTP password, bearer Token, Authorization value, or credential configuration. Such a header does not grant, deny, or otherwise alter admitted localhost access.
4. health checks and host-side MCP initialization use the same loopback Host/Origin boundary and report readiness without starting a Workflow.

## Lineage

this Method replaces CA-M-342, whose fixed Summary identifies the retired bearer-authentication procedure.
