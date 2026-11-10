---
atom_id: CA-M-324
ref_id: CA-M-324
container:
  scope_unit: CA-SU-20
role: Method
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime
tier: 4
status: Archived
version: 14
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-M-324@14-APPS-DECISION--manage-the-runtime-with-docker-compose.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/05_method/archive
current_scope_unit: APPS
author: Anatoly Maslennikov
relations:
  method_for:
  - CA-R-1818
---

## Summary

manage the runtime **with** Docker Compose

## Claim

### Prose Claim

Manage the deterministic runtime through Docker Compose using one image and separate MCP and worker services with explicit persistent-state boundaries.

## Details

### Scope

the Docker runtime's implementation **and** lifecycle management.

1. build from admitted Engine sources **and** pinned runtime dependencies; exclude Project data, credentials **and** generated state from the build context.
2. use non-root services, a read-only image filesystem **and** **only** the mounts required by their responsibilities.
3. give the worker a separate Docker scheduler namespace. keep the shared Journal **and** report locations unchanged.
4. publish Docker routing **only** **after** worker readiness. queue calls **must** fail visibly **if** the selected runtime is unavailable; they **must not** fall back **to** another queue.
5. preserve saved dispatch evidence across restart. after uncertain dispatch, require reconciliation rather than another Agent call.
6. keep automatic restart disabled. provide explicit restart **and** a stdio MCP launcher; lifecycle commands do **not** create Workflow requests.

## Semantics

The retained AI-Agent service and its credentials are conditional on separately admitted AI-Agent execution. They do not require the current deterministic runtime to start or restore that service. The MCP and worker boundaries remain applicable to retained deterministic execution.

### Conditional future AI-Agent execution

implement runtime management through Docker Compose using **=1** image **and** separate MCP, worker **and** Agent services with explicit persistent-state boundaries.

The Agent-service part of this retained design applies only to separately admitted AI-Agent execution; it does not require that service in the current deterministic runtime.
