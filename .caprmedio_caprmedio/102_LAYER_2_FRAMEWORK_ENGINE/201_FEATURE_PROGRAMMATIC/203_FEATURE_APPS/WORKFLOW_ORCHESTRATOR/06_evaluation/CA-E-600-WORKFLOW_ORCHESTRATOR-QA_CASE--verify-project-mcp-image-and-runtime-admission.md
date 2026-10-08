---
atom_id: CA-E-600
content_role: Evaluation
type: QA Case
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 00:27:39 +0400"
subjects:
  governs: "Workflow Orchestrator/Project MCP runtime admission evaluation"
  depends_on: [Project, MCP, Docker Runtime, Image, Gateway, Credential, Carrier]
relations:
  evaluation_for: [CA-R-1901, CA-M-356]
  relates_to: [CA-E-537, CA-E-584, CA-E-585]
---
# Summary

verify Project MCP image and runtime admission

## Scope

image-fingerprint, lock, Docker-publication, and runtime-reuse checks for the Project MCP launcher.

## Claim

the Evaluation **must** prove that only a matching immutable image and a healthy same-Project runtime can be used, and that dynamic loopback publication is Docker-owned.

## Details

- unit-test the ordered source manifest/fingerprint against a changed explicit `--source-root` Engine, dependency, Dockerfile/ignore, platform, or build argument; each change produces a different fingerprint. Verify Project Carriers, credentials, installed state, generated outputs, and any unrelated repository source do not enter the image fingerprint.
- test explicit image references that are mutable, missing, wrong-schema, fingerprint-mismatched, or correct. Verify missing matching images build under the invocation's default `build_if_missing=true`, refuse under `--no-build`, and capture/re-inspect an immutable digest without retagging or replacing another image.
- exercise a packaged launcher lacking a required Engine/Docker/dependency input. Verify `IMAGE_INPUT_UNAVAILABLE` safely requests `--source-root`, preserves installed runtime N, and does not begin a full Release, package replacement, or Framework promotion.
- simulate a held per-Project lock, a matching healthy runtime, a matching unhealthy runtime, and a live mismatched runtime. Only the healthy matching case is reusable; every other live case preserves the existing service and returns its non-success disposition.
- in a real-Docker gate when Docker is available, start one `mcp-http` service with no explicit host port and verify Docker reports exactly one `127.0.0.1` publication for container port `8092`, a real assigned host port, and no host-side pre-reservation. Verify an explicit port follows the same one-publication rule.
- verify the admitted launcher starts neither worker, queue, Agent, Workflow, Tool call, proxy, nor Release action. Docker absence or denial is incomplete/failed evidence for the real-Docker case, not a passing mock result.
