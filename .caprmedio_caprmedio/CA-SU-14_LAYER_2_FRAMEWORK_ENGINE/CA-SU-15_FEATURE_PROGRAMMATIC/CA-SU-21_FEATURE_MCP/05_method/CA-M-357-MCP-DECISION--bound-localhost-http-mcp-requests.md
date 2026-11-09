---
atom_id: CA-M-357
ref_id: CA-M-357
container:
  scope_unit: CA-SU-21
role: Method
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect
    Authorization
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication/API
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime/Session
tier: 4
relations:
  method_for:
  - CA-R-1885
status: Active
version: 14
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-M-357-MCP-DECISION--bound-localhost-http-mcp-requests.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method
current_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

bound localhost HTTP MCP Requests

## Claim

### Prose Claim

the HTTP access implementation **must** validate the loopback Host/Origin boundary before the existing MCP handlers receive a Request, without password, bearer, or other HTTP authentication.

## Details

### Scope

the additional localhost HTTP transport for the existing Project MCP Gateway.

1. use a narrow ASGI loopback Host/Origin guard for every HTTP Request, including Session continuations. Forward lifespan unchanged.
2. enable the MCP SDK's DNS-rebinding protection explicitly; a container bind address of `0.0.0.0` does not disable Host/Origin validation.
3. do not read, require, validate, rotate, inject, or report an HTTP password, bearer Token, Authorization value, or credential configuration. Such a header does not grant, deny, or otherwise alter admitted localhost access.
4. health checks and host-side MCP initialization use the same loopback Host/Origin boundary and report readiness without starting a Workflow.

### Lineage

this Method replaces CA-M-342, whose fixed Summary identifies the retired bearer-authentication procedure.
