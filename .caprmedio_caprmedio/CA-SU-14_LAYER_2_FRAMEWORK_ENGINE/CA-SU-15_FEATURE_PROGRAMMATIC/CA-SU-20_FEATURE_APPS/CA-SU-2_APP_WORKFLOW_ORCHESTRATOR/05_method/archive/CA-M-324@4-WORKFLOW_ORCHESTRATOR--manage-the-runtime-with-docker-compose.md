---
atom_id: CA-M-324@4
content_role: Method
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-23 03:14:50 +0400
subjects:
  governs: Subject/Engineering/Runtime/Docker Compose Lifecycle
  depends_on:
  - Implementation
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Engineering/Carrier
  - Subject/Engineering/Journal Operations
  - Subject/Engineering/Runtime/Docker Compose Lifecycle
relations:
  relates_to:
  - CA-R-1818
  - CA-R-1819
  - CA-M-320
type: Engineering Decision
---
# Summary

manage the runtime **with** Docker Compose

## Scope

the Docker runtime's implementation **and** lifecycle management.

## Claim

implement runtime management through Docker Compose using **=1** image **and** separate MCP, worker **and** Agent services with explicit persistent-state boundaries.

## Details

1. build from admitted Engine sources **and** pinned runtime dependencies; exclude Project data, credentials **and** generated state from the build context.
2. use non-root services, a read-only image filesystem **and** **only** the mounts required by their responsibilities.
3. give the worker a separate Docker scheduler namespace. keep the shared Journal **and** report locations unchanged.
4. publish Docker routing **only** **after** worker readiness. queue calls **must** fail visibly **if** the selected runtime is unavailable; they **must not** fall back **to** another queue.
5. preserve saved dispatch evidence across restart. after uncertain dispatch, require reconciliation rather than another Agent call.
6. keep automatic restart disabled. provide explicit restart **and** a stdio MCP launcher; lifecycle commands do **not** create Workflow requests.
