---
atom_id: CA-D-525@3
content_role: Delivery
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: 2026-10-23 01:47:30 +0400
subjects:
  governs: Subject/Engineering/Runtime/Docker Persistent-State Carrier
  depends_on:
  - Carrier
  - Implementation
  - Workflow Run
  - Atom
  - Journal
  - Operator
  - Action
  - AI Agent
  - Subject/Engineering/Runtime/Docker Persistent-State Carrier
relations:
  relates_to: [CA-D-521, CA-D-522, CA-R-1818, CA-R-1819]
type: Engineering Decision
---
# Summary

carry the Docker runtime **and** persistent state

## Scope

WORKFLOW_ORCHESTRATOR's Docker image, configuration **and** persistent Carriers.

## Claim

the Docker runtime **must** be carried by Dockerfile, a restrictive build-context ignore file, Compose configuration **and** explicit runtime adapters.

## Details

- Dockerfile, build-context ignore file, Compose configurations, lifecycle controller **and** service entrypoints: `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/`.
- shared proposal, namespace **and** host bridge adapters: `remote_agent.py`, `runtime_config.py` **and** `docker_bridge.py` beside the existing orchestrator executor.
- image: supported Python 3.14, pinned uv **and** Codex CLI, Engine source **and** locked dependency groups; no Project source Atoms, credentials **or** generated state.
- services: `worker`, `agent` **and** optional stdio `mcp`; one Project-scoped Compose name, no host ports **or** Docker socket mounts.
- worker/MCP: one Project filesystem mounted at `/project`; authority, installed execution state, Temporary State, runtime state **and** reports retain their existing relative paths. this preserves atomic publication from `.caprmedio_tmp/` to admitted destinations.
- Git metadata **and** the Project's Engine mirror are read-only. executable code **and** locked dependencies remain in the immutable image at `/workspace`; the Agent receives no Project mount.
- Docker scheduler, worker control **and** frozen requests: `.caprmedio_install/workflow_orchestrator/docker/`. native scheduler files remain separate.
- Action request: `context`, `phase`, `timeout`; response: `report_json`, `candidate_content`, `confidence`. HTTP endpoints are `/health` **and** `/execute` **only** on the private container network.
- Agent authentication: explicit read-only credential seed **and** private persistent authentication volume, excluded from the image; mock configuration uses no credentials.
- complete Workflow reports remain `tmp/RMED Atoms Base Revise/<run_id>.md`; confirmed events use the existing shared Journal.
