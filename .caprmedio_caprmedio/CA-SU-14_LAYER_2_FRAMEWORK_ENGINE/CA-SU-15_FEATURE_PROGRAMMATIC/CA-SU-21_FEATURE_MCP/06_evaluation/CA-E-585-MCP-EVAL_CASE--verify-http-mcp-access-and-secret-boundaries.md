---
atom_id: CA-E-585
ref_id: CA-E-585
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Communication
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution
    Control <+ Effect Authorization
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture
    <+ Communication <+ API
  - MODEL//CAPRMEDIO <+ Actor/Operator
  - MODEL//CAPRMEDIO <+ Execution
tier: 5
relations:
  evaluation_for:
  - CA-R-1885
  - CA-M-357
status: Active
version: 12
updated_at: 2026-11-10 20:47:54 +0400
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

Exercise absent, valid-looking and arbitrary Authorization values; hostile Host/Origin cases; absent Origin; and Session continuations. Rejected Host/Origin requests must invoke no Tool and produce no reload receipt; Authorization neither changes localhost admission nor supplies authority. Verify readiness depends on loopback Host/Origin and MCP initialization, not password, bearer, Token, credential configuration or rotation. Check loopback-only Compose mapping, no Docker socket or HTTP credential configuration, no secret-bearing arguments/logs, and unchanged stdio/default worker startup.
