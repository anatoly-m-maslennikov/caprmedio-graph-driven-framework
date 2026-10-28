---
atom_id: CA-E-585
content_role: Evaluation
type: Eval Case
current_scope_unit: MCP
status: Active
author: Anatoly Maslennikov
version: 10
updated_at: 2026-10-27 19:59:37 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication/API
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
relations:
  evaluation_for:
  - CA-R-1885
  - CA-M-357
tier: 5
---
# Summary

verify HTTP MCP access and secret boundaries

## Scope

the additional localhost HTTP transport for the existing Project MCP Gateway.

## Claim

the Evaluation **must** verify that HTTP access failures occur before MCP handling and preserve the existing permission and secret boundaries.

## Details

1. include good Requests with absent, valid-looking, and arbitrary Authorization values, hostile Host/Origin cases, absent Origin, and Session continuations.
2. verify Host/Origin rejection and no Tool invocation or reload receipt on rejected Requests; Authorization values do not grant, deny, or otherwise alter admitted localhost access.
3. verify readiness requires the loopback Host/Origin and MCP initialization boundary, not password, bearer, Token, credential configuration, or rotation.
4. check localhost-only Compose mapping, no Docker socket, no HTTP credential configuration, no secret-bearing command arguments or logs, and unchanged stdio/default worker startup.
