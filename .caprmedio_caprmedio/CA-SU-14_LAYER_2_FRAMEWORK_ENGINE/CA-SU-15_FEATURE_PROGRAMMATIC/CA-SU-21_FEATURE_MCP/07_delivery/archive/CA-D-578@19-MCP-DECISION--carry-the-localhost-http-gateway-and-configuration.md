---
atom_id: CA-D-578
ref_id: CA-D-578@19
container:
  scope_unit: CA-SU-21
role: Delivery
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
    Structure
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication/API
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime/Session
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime/Container Run
tier: 5
relations:
  delivery_for:
  - CA-R-1884
  - CA-R-1885
  - CA-M-341
  - CA-M-357
status: Archived
version: 19
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-D-578@19-MCP-DECISION--carry-the-localhost-http-gateway-and-configuration.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/07_delivery/archive
current_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

carry the localhost HTTP Gateway and configuration

## Claim

### Prose Claim

the additional HTTP endpoint **must** be carried by the existing MCP Gateway entrypoint and an opt-in Docker service, with explicit-or-Docker-owned-loopback publication and runtime-secret configuration.

## Details

### Scope

the HTTP server, opt-in Docker service, configuration and connection carriers.

1. deliver HTTP support beside `hot_reload.py` under `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/`; `server.py --transport stdio` remains the default. The additional transport is `streamable-http`, with path `/caprmedio/mcp` and container port `8092`.
2. keep the existing `mcp` Compose service unchanged; add `mcp-http` with the same restricted image and Project mounts, no Docker socket, and a dedicated loopback Host/Origin-protected health check.
3. the opt-in `docker/mcp-http.compose.yaml` overlay publishes only `mcp-http` on host loopback. A direct lifecycle request may carry an explicitly selected integer host port in `1..65535`; the bounded Project MCP launcher may instead request Docker's dynamic publication form `127.0.0.1::8092`, with no implicit fixed public-port default. Docker owns that allocation atomically; the launcher does not pre-bind, probe-reserve, or infer the port. Attach **only** `mcp-http` to a dedicated non-internal `http_publication` bridge alongside the existing internal `runtime` network, so Docker can activate the host binding. This bridge permits HTTP-service outbound traffic; it is not an ingress-only isolation guarantee. Keep worker, Agent and stdio network attachments unchanged. Loading this overlay is explicit and does not change normal worker/stdio startup.
4. do not configure, read, inject, rotate, or persist an HTTP password, bearer Token, Authorization value, secret file, or credential environment variable for this transport.
5. support explicit `mcp-http-start`, `mcp-http-stop` and `mcp-http-status` lifecycle operations in the existing Docker runtime adapter. Return the safe connection URL `http://127.0.0.1:<port>/caprmedio/mcp` and readiness/service state. After startup, report ready **only** when Docker reports **=1** running, healthy `mcp-http` service with **=1** TCP publisher: target port `8092`, either the caller-selected or Docker-observed dynamically assigned host port, and bind address `127.0.0.1`. Missing, ambiguous or mismatched publication is a failed startup, even when the container health check passes. A Project launcher reports a ready URL only after its separate Host/Origin-protected host-side MCP readiness exchange. HTTP startup does not require or implicitly start the Codex Agent service, worker, queue, Agent, or Workflow.
6. permit loopback Host values and loopback HTTP Origins; no Origin is required for non-browser clients. Do not require or validate an Authorization header. Rejections expose no credential value.
7. test delivery belongs in `204_MCP/tests/test_hot_reload_http.py` and a Docker HTTP configuration/lifecycle test module. Existing stdio tests are retained. Docker absence or denial remains a failed/incomplete real-container gate, not a successful fixture result.
