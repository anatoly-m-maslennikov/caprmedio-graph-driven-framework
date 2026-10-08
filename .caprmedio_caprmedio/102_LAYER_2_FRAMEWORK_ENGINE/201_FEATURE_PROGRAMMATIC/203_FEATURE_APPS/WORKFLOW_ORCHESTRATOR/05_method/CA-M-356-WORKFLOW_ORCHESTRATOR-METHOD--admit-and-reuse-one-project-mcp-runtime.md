---
atom_id: CA-M-356
content_role: Method
current_scope_unit: WORKFLOW_ORCHESTRATOR
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 00:27:39 +0400"
subjects:
  governs: "Workflow Orchestrator/Project MCP runtime admission method"
  depends_on: [Project, MCP, Docker Runtime, Image, Gateway, Credential, Carrier]
relations:
  method_for: [CA-R-1901]
  relates_to: [CA-M-324, CA-M-325, CA-M-341, CA-M-342]
---
# Summary

admit and reuse one Project MCP runtime

## Scope

the bounded start-or-reuse procedure for the selected Project's HTTP MCP service.

## Claim

the launcher **must** compute one source fingerprint, resolve one immutable image, and evaluate one selected Project runtime under its per-Project lock before it can expose a localhost MCP URL.

## Details

1. accept a validated `ProjectSelection` and separately explicit readable `--source-root`, calculate the ordered build-input manifest and its SHA-256 fingerprint, and retain the input manifest as safe evidence. `--source-root` is for Engine/Docker build closure only and never changes Project selection or causes repository/sibling inference. Include admitted Engine, dependency-lock, Dockerfile/ignore, platform, and fixed build-argument inputs exactly once; reject a changed, missing, or unadmitted input as `IMAGE_INPUT_UNAVAILABLE`.
2. inspect an explicit immutable image digest or a locally resolved labelled image. Require the declared label schema and exact fingerprint. If no matching image is present, the launcher invocation's `build_if_missing=true` default authorizes one build; `--no-build` sets it false and returns an image refusal. Capture the builder's immutable digest, then inspect the same labels before use. Do not accept a mutable tag as the result.
3. acquire the selected identity's lock, inspect only Compose resources labelled for that identity, and compare their immutable image digest and fingerprint. Reuse only one running, healthy matching `mcp-http` service after the host-side authenticated readiness check. A live mismatch or unhealthy service stops with its truthful disposition; it is not an instruction to stop, recreate, or replace it.
4. if no live selected runtime exists, launch only `mcp-http` with the selected Project mount and context. With no explicit port, request the Compose publication form `127.0.0.1::8092` so Docker atomically assigns the host port. With an explicit port, require `1..65535` and the same loopback binding. Read Docker's one published mapping after startup; never reserve or test-bind a host port separately.
5. obtain the readiness credential only from the explicit accepted environment credential source. It is supplied to the service and used for the host probe without entering an argument list, URL, result, diagnostic, log, image, or persistent launcher metadata. Bound the readiness wait and return its failure rather than guessing readiness.
6. release the per-Project lock after recording only safe metadata. This procedure performs no MCP Tool dispatch, Gateway proxying, worker/queue/Agent start, Workflow execution, or Release action.
