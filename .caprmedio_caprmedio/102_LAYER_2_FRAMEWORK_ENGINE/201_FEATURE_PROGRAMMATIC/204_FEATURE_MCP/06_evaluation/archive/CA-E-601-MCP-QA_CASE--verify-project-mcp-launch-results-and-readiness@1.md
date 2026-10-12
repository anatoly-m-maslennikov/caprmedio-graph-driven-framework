---
atom_id: CA-E-601
content_role: Evaluation
type: QA Case
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 00:42:28 +0000"
subjects:
  governs: "MCP/Project launcher/result evaluation"
  depends_on: [Action, Project, MCP, Gateway, Docker Runtime, Credential, HTTP, Carrier]
relations:
  evaluation_for: [CA-O-188]
  relates_to: [CA-E-599, CA-E-600, CA-E-584, CA-E-585]
---
# Summary

verify Project MCP launch results and readiness

## Scope

the observable output and authenticated host-side readiness boundary of the Project MCP launcher.

## Claim

the Evaluation **must** verify that every launcher disposition is structured, safe, and attributable, and that a success URL is returned only after actual authenticated host readiness.

## Details

- exercise each exact safe code in CA-O-188: `READY_STARTED`, `READY_REUSED`, `PROJECT_SELECTION_REFUSED`, `CREDENTIAL_SOURCE_REFUSED`, `IMAGE_INPUT_UNAVAILABLE`, `IMAGE_REFUSED`, `PROJECT_LOCK_BUSY`, `RUNTIME_MISMATCH`, `RUNTIME_UNHEALTHY`, `BUILD_FAILED`, `DOCKER_START_FAILED`, `DOCKER_PUBLICATION_FAILED`, and `READINESS_FAILED`. Each outcome has one matching disposition; only ready `started`/`reused` outcomes contain a URL. Verify default JSON result output and `--output url`, which emits no URL for every non-success.
- for a real-Docker gate, connect from the host to the exact Docker-reported `127.0.0.1` port and complete the authenticated MCP initialization/readiness exchange. Prove that container health, an open socket, an unauthenticated response, or a wrong Token cannot produce a success URL.
- assert the result contains only Project identity, safe selected root/control-root references, immutable image digest/fingerprint, service/publication/readiness facts, and bounded diagnostics. Search structured output and ordinary diagnostics for the credential value, bearer form, URL query/fragment credential, and secret-bearing environment value; none may occur.
- verify readiness and every failure case start no worker, queue, Agent, Workflow, Tool call, proxy, or Release action. Verify a failed or refused outcome preserves a live selected runtime and does not claim replacement or completion.
