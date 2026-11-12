---
atom_id: CA-E-584
ref_id: CA-E-584@14
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Component Structure
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Dynamic Testing
  - MODEL//CAPRMEDIO <+ Package/Project Package
  - MODEL//CAPRMEDIO <+ Runtime/Session
tier: 5
relations:
  evaluation_for:
  - CA-R-1884
  - CA-M-341
status: Archived
version: 14
updated_at: 2026-11-11 06:09:13 +0400
carrier_destination:
  file:
    name: CA-E-584@14-MCP-EVAL_CASE--verify-http-mcp-gateway-and-stdio-preservation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation/099_archived
current_scope_unit: MCP
author: Anatoly Maslennikov
---
## Summary

verify HTTP MCP Gateway and stdio preservation

## Claim

### Prose Claim

the Evaluation **must** verify that real MCP HTTP initialization, discovery and calls use the existing Gateway without breaking stdio behavior.

## Details

### Scope

the additional localhost HTTP transport for the existing Project MCP Gateway.

Use real-Gateway E2E fixtures with a disposable mock implementation to exercise Streamable HTTP initialization, discovery and a Tool call. On lifespan exit, verify Session cleanup; run existing stdio transport tests. When Docker is available, verify the Docker service’s localhost URL in a container; a mock or host-ASGI pass does not satisfy that Docker gate.
