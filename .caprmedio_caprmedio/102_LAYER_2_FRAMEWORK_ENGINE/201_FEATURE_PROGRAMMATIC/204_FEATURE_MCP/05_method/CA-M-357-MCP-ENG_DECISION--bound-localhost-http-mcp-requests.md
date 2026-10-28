---
atom_id: CA-M-357
content_role: Method
current_scope_unit: MCP
status: Active
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-27 19:59:42 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication/API
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime/Session
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
