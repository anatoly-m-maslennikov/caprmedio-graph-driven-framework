---
atom_id: CA-E-585@4
content_role: Evaluation
type: Eval Case
current_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-24 00:38:25 +0400
subjects:
  governs: Subject/Engineering/MCP/HTTP Access Boundary Evaluation
  depends_on:
  - Subject/Engineering/MCP
  - Subject/Engineering/HTTP
  - Subject/Engineering/HTTP/Request
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Engineering/Permission
  - Subject/Domain/Node/Occurrent/Execution
  - Subject/Engineering/Agentic Instruction/Tool Call Execution Detail
relations:
  evaluation_for:
  - CA-R-1885
  - CA-M-357
tier: 3
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
