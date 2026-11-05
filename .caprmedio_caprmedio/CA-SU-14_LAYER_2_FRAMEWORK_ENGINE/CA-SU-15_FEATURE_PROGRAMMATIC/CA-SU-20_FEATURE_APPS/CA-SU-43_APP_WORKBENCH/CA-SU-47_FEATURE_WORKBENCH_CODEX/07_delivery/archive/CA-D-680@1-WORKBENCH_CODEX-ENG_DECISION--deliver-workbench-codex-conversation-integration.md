---
atom_id: CA-D-680
current_scope_unit: WORKBENCH_CODEX
claim_target_scope_unit: WORKBENCH_CODEX
status: Archived
version: 1
author: Anatoly Maslennikov
role: Delivery
form: Eng Decision
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Project
relations:
  delivery_for:
  - CA-R-2791
  - CA-M-475
  - CA-E-682
carrier_destination:
  file:
    name: CA-D-680@1-WORKBENCH_CODEX-ENG_DECISION--deliver-workbench-codex-conversation-integration.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-47_FEATURE_WORKBENCH_CODEX/07_delivery/archive
updated_at: 2026-11-05 14:23:38 +0400
---

## Summary

Deliver Workbench Codex conversation integration

## Claim

### Prose Claim

Deliver one Project Workspace with one Codex conversation in the existing Workbench Svelte panel and a small loopback host bridge to the official Codex app-server. The source-owned `WORKBENCH_CODEX/start_bridge.py` starts the bridge after local release reports MCP ready. The browser uses HTTP and SSE to the host bridge on an OS-assigned loopback port; the bridge uses stdio JSON-RPC to the app-server.

The Workbench Docker server exposes `GET /codex`, a same-origin safe-state route that returns bridge URL, readiness and the native thread ID. It reads only `.caprmedio_runtime/workbench/codex/bridge.json` for bridge URL and readiness and `.caprmedio_runtime/workbench/codex/thread.json` for the native thread ID. These files store no conversation history.

The loopback bridge exposes only these operations:

- `GET /conversation` opens or resumes the native thread and returns its native history.
- `POST /turn {message}` starts one turn and streams SSE. Its first event includes native `thread_id` and `turn_id`; every native event retains them and ends with one terminal `completed`, `failed` or `interrupted` status.
- `POST /respond {id, result}` forwards an interaction or approval response to the native app-server request ID.
- `POST /interrupt {turn_id}` interrupts only the matching active turn.
- `GET /health` returns bridge readiness for the launcher.

Pass `project_root` only to CAPRMEDIO requests. Reuse the local signed-in Codex session. Allow the bridge's browser origin only from the selected Project MCP endpoint's exact scheme, host and port; do not use wildcard CORS or mount credentials into Docker.

Persist the native app-server thread. Keep only its ID in the Workbench runtime state file; do not create a duplicate conversation-history store. Inherit enabled MCP servers from local Codex configuration. For CAPRMEDIO, use the generated root `discover_tools` catalog and current native frontier. For other enabled MCP servers, use native discovery. Do not use a Workbench-only allowlist or a unified Tool registry.

Do not deliver multiple-chat management, a generic code-editing agent, a duplicate Tool registry, a model picker, a generic service framework, a queue, scheduler, retry or rollback system.
