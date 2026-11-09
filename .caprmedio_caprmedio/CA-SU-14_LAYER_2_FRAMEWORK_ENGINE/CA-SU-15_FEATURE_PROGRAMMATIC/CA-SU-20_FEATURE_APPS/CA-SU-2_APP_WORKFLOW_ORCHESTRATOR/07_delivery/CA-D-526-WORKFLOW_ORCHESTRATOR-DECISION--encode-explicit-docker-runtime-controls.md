---
atom_id: CA-D-526
ref_id: CA-D-526
container:
  scope_unit: CA-SU-2
role: Delivery
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
  dependencies:
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
tier: 5
status: Active
version: 14
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-D-526-WORKFLOW_ORCHESTRATOR-DECISION--encode-explicit-docker-runtime-controls.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/07_delivery
current_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
relations:
  delivery_for:
  - CA-R-1818
  - CA-M-324
---

## Summary

encode explicit Docker runtime controls

## Claim

### Prose Claim

`docker/runtime.py` **must** carry explicit `build`, `start`, `stop`, `restart`, `status`, `logs` **and** `mcp` commands using the Project root **and** optional credential-file input.

## Details

### Scope

the Project-local Docker control adapter **and** existing MCP queue adapter.

- successful start writes `.caprmedio_install/workflow_orchestrator/docker/transport.json`, selecting Docker queue routing for the existing MCP adapter.
- queue calls use fixed argument arrays **and** JSON stdin through `docker compose exec`; they do **not** interpolate shell text from requests.
- start/restart status distinguishes container existence, worker readiness **and** Agent readiness. no automatic restart policy is carried.
- stop retains the routing selection **and** persistent state, so an enqueue cannot silently target the native worker.
- `mcp` starts an interactive stdio client service **without** starting worker services. local service management does **not** create Run inputs.
- rebuilding the image **and** explicitly recreating services applies updated runtime code; MCP hot reload alone does **not** reload the worker image.

## Semantics

The retained AI-Agent service and its credentials are conditional on separately admitted AI-Agent execution. They do not require the current deterministic runtime to start or restore that service. The MCP and worker boundaries remain applicable to retained deterministic execution.
