---
atom_id: CA-D-525
ref_id: CA-D-525
role: Delivery
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Active
author: Anatoly Maslennikov
version: 16
updated_at: 2026-11-02 19:46:47 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Carrier
  dependencies:
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
form: Eng Decision
tier: 3
container:
  scope_unit: CA-SU-2
carrier_destination:
  file:
    name: CA-D-525-WORKFLOW_ORCHESTRATOR-ENG_DECISION--carry-the-docker-runtime-and-persistent-state.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/07_delivery
---
# Summary

carry the Docker runtime **and** persistent state

## Scope

WORKFLOW_ORCHESTRATOR's Docker image, configuration **and** persistent Carriers.

## Claim

the Docker runtime **must** be carried by Dockerfile, a restrictive build-context ignore file, Compose configuration **and** explicit runtime adapters.

## Details

- Dockerfile, build-context ignore file, Compose configurations, lifecycle controller **and** service entrypoints: `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/docker/`.
- shared proposal, namespace **and** host bridge adapters: `remote_agent.py`, `runtime_config.py` **and** `docker_bridge.py` beside the existing orchestrator executor.
- image: supported Python 3.14, pinned uv **and** Codex CLI, Engine source **and** locked dependency groups; no Project source Atoms, credentials **or** generated state.
- services: `worker`, `agent` **and** optional stdio `mcp`; one Project-scoped Compose name, no host ports **or** Docker socket mounts.
- worker/MCP: one Project filesystem mounted at `/project`; authority, installed execution state, Temporary State, runtime state **and** reports retain their existing relative paths. this preserves atomic publication from `.caprmedio_tmp/` to admitted destinations.
- Git metadata **and** the Project's Engine mirror are read-only. executable code **and** locked dependencies remain in the immutable image at `/workspace`; the Agent receives no Project mount.
- Docker scheduler, worker control **and** frozen requests: `.caprmedio_install/workflow_orchestrator/docker/`. native scheduler files remain separate.
- Action request: `context`, `phase`, `timeout`; response: `report_json`, `candidate_content`, `confidence`. HTTP endpoints are `/health` **and** `/execute` **only** on the private container network.
- Agent authentication: explicit read-only credential seed **and** private persistent authentication volume, excluded from the image; mock configuration uses no credentials.
- complete Workflow reports remain `tmp/RMED Atoms Base Revise/<run_id>.md`; confirmed events use the existing shared Journal.
