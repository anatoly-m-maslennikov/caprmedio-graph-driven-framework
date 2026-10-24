---
atom_id: CA-D-526@6
content_role: Delivery
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-24 00:38:25 +0400
subjects:
  governs: Subject/Engineering/Runtime/Docker Control Adapter
  depends_on:
  - Subject/Engineering/Carrier
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Implementation
  - Subject/Engineering/Runtime/Docker Control Adapter
relations:
  relates_to:
  - CA-D-525
  - CA-R-1818
type: Eng Decision
tier: 3
---
# Summary

encode explicit Docker runtime controls

## Scope

the Project-local Docker control adapter **and** existing MCP queue adapter.

## Claim

`docker/runtime.py` **must** carry explicit `build`, `start`, `stop`, `restart`, `status`, `logs` **and** `mcp` commands using the Project root **and** optional credential-file input.

## Details

- successful start writes `.caprmedio_install/workflow_orchestrator/docker/transport.json`, selecting Docker queue routing for the existing MCP adapter.
- queue calls use fixed argument arrays **and** JSON stdin through `docker compose exec`; they do **not** interpolate shell text from requests.
- start/restart status distinguishes container existence, worker readiness **and** Agent readiness. no automatic restart policy is carried.
- stop retains the routing selection **and** persistent state, so an enqueue cannot silently target the native worker.
- `mcp` starts an interactive stdio client service **without** starting worker services. local service management does **not** create Run inputs.
- rebuilding the image **and** explicitly recreating services applies updated runtime code; MCP hot reload alone does **not** reload the worker image.
