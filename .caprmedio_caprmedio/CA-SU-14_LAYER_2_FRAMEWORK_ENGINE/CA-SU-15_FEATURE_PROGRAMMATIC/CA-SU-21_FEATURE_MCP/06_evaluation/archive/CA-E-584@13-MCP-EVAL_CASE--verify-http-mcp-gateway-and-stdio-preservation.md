---
atom_id: CA-E-584
ref_id: CA-E-584@13
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Communication
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture
    <+ Component Structure
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification
    <+ Dynamic Testing
  - MODEL//CAPRMEDIO <+ Package/Project Package
  - MODEL//CAPRMEDIO <+ Runtime/Session
tier: 5
relations:
  evaluation_for:
  - CA-R-1884
  - CA-M-341
status: Archived
version: 13
updated_at: 2026-11-10 20:47:54 +0400
carrier_destination:
  file:
    name: CA-E-584@13-MCP-EVAL_CASE--verify-http-mcp-gateway-and-stdio-preservation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation/archive
current_scope_unit: MCP
author: Anatoly Maslennikov
---
## Summary

verify HTTP MCP Gateway and stdio preservation

## Claim

### Prose Claim

the Evaluation **must** verify that real MCP HTTP initialization, discovery, calls and reload use the existing Gateway without breaking stdio behavior.

## Details

### Scope

the additional localhost HTTP transport for the existing Project MCP Gateway.

Use real-Gateway E2E fixtures with a disposable mock implementation to exercise Streamable HTTP initialization, discovery and a Tool call. Reload the mock on the same HTTP connection, verify the new registry/result, and keep an in-flight old-generation call until it drains. On lifespan exit, verify Session and generation cleanup; run existing stdio hot-reload tests unchanged. When Docker is available, verify the Docker service’s localhost URL in a container; a mock or host-ASGI pass does not satisfy that Docker gate.
