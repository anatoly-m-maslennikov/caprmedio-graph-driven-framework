---
atom_id: CA-E-584
content_role: Evaluation
type: Eval Case
current_scope_unit: MCP
status: Active
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-24 04:47:50 +0400
subjects:
  governs: Subject/Engineering/MCP/HTTP endpoint/Functional evaluation
  depends_on:
  - Subject/Engineering/MCP
  - Subject/Engineering/HTTP
  - Subject/Engineering/Gateway
  - Subject/Engineering/MCP.HTTP Gateway Evaluation
  - Subject/Engineering/Generation
  - Subject/Domain/Node/Occurrent/Session
  - Subject/Engineering/MCP/HTTP Access Boundary Evaluation
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
