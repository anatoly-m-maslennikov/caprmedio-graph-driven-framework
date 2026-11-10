---
atom_id: CA-M-357
ref_id: CA-M-357
container:
  scope_unit: CA-SU-21
role: Method
form: Decision
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Communication
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution
    Control <+ Effect Authorization
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture
    <+ Communication <+ API
  - MODEL//CAPRMEDIO <+ Actor/Operator
  - MODEL//CAPRMEDIO <+ Runtime/Session
tier: 4
relations:
  method_for:
  - CA-R-1885
status: Active
version: 15
updated_at: 2026-11-10 20:47:54 +0400
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

### Localhost transport boundary

1. Use a narrow ASGI loopback Host/Origin guard for every HTTP Request, including Session continuations; forward lifespan unchanged.
2. Enable MCP SDK DNS-rebinding protection explicitly; a container bind address of 0.0.0.0 does not disable validation.
3. Do not read, require, validate, rotate, inject, or report HTTP password, bearer Token, Authorization, or credential configuration; such a header cannot alter admitted localhost access.
4. Health checks and host-side MCP initialization use the same boundary and report readiness without starting a Workflow.

This Method replaces CA-M-342, whose fixed Summary identifies the retired bearer-authentication procedure.
