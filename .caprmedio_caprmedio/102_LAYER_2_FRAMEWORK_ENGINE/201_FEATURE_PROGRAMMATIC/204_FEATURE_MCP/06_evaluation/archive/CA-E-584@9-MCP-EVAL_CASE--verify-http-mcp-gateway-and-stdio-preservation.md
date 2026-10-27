---
atom_id: CA-E-584@9
content_role: Evaluation
type: Eval Case
current_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-26 00:46:35 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Architecture/Communication
  depends_on:
  - Subject/Graph Node/Engineering/MCP
  - Subject/Graph Node/Engineering/HTTP
  - Subject/Graph Node/Engineering/Gateway
  - Subject/Graph Node/Engineering/MCP.HTTP Gateway Evaluation
  - Subject/Graph Node/Engineering/Generation
  - Subject/Graph Node/Engineering/Occurrent/Session
  - Subject/Graph Node/Engineering/MCP/HTTP Access Boundary Evaluation
relations:
  evaluation_for:
  - CA-R-1884
  - CA-M-341
tier: 5
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
