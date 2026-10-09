---
atom_id: CA-M-357
content_role: Method
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 04:37:30 +0400"
subjects:
  governs: "MCP/HTTP endpoint/Access implementation"
  depends_on: [MCP, HTTP, Request, Operator, Permission, Session]
relations:
  method_for: [CA-R-1885]
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
