---
atom_id: CA-E-585
ref_id: CA-E-585
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect
    Authorization
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication/API
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
tier: 5
relations:
  evaluation_for:
  - CA-R-1885
  - CA-M-357
status: Active
version: 11
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-E-585-MCP-EVAL_CASE--verify-http-mcp-access-and-secret-boundaries.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
current_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

verify HTTP MCP access and secret boundaries

## Claim

### Prose Claim

the Evaluation **must** verify that HTTP access failures occur before MCP handling and preserve the existing permission and secret boundaries.

## Details

### Scope

the additional localhost HTTP transport for the existing Project MCP Gateway.

1. include good Requests with absent, valid-looking, and arbitrary Authorization values, hostile Host/Origin cases, absent Origin, and Session continuations.
2. verify Host/Origin rejection and no Tool invocation or reload receipt on rejected Requests; Authorization values do not grant, deny, or otherwise alter admitted localhost access.
3. verify readiness requires the loopback Host/Origin and MCP initialization boundary, not password, bearer, Token, credential configuration, or rotation.
4. check localhost-only Compose mapping, no Docker socket, no HTTP credential configuration, no secret-bearing command arguments or logs, and unchanged stdio/default worker startup.
