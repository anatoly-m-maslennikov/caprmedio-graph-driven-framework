---
atom_id: CA-E-584@11
ref_id: CA-E-584@11
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
    Structure
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Dynamic Testing
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime/Session
tier: 5
relations:
  evaluation_for:
  - CA-R-1884
  - CA-M-341
status: Archived
version: 11
updated_at: 2026-10-27 19:59:37 +0400
carrier_destination:
  file:
    name: CA-E-584@11-MCP-EVAL_CASE--verify-http-mcp-gateway-and-stdio-preservation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation/archive
current_scope_unit: MCP
author: Anatoly Maslennikov
---
# Summary

verify HTTP MCP Gateway and stdio preservation

## Scope

the additional localhost HTTP transport for the existing Project MCP Gateway.

## Claim

the Evaluation **must** verify that real MCP HTTP initialization, discovery, calls and reload use the existing Gateway without breaking stdio behavior.

## Details

1. build e2e fixtures first with a real Gateway and disposable mock implementation. Exercise handshake, Tool discovery and a Tool call through the real Streamable HTTP application.
2. reload the mock implementation on the same HTTP connection and verify the new registry and result; preserve an in-flight old-generation call until it drains.
3. exit the HTTP lifespan and verify Session and generation cleanup. Run the existing stdio hot-reload tests unchanged.
4. verify the Docker service's localhost URL through an actual container when Docker is available; a mock or host-ASGI pass is not that Docker gate.
