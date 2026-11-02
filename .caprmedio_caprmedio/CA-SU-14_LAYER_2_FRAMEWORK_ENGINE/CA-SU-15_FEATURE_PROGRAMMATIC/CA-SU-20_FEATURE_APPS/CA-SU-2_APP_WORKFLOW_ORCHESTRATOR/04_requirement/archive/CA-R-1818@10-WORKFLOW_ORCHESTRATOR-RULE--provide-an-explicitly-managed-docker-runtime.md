---
atom_id: CA-R-1818@10
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 10
updated_at: 2026-10-26 05:59:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Execution Control
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Engineering/Occurrent/Runtime/Docker Workflow Execution
  - Subject/Graph Node/Engineering/Journal Operations
  - Subject/Graph Node/Domain/Continuant/Atom
relations: {}
type: Rule
tier: 3
---
# Summary

provide an explicitly managed Docker runtime

## Scope

the Docker execution option for WORKFLOW_ORCHESTRATOR **and** its MCP **and** Tool capabilities.

## Claim

the Docker runtime **must** preserve authorized Workflow behavior **and** durable execution evidence while providing explicit build, start, stop, restart, status **and** log capabilities.

## Details

- installation starts no Run. starting services is a separate Operator-authorized operation.
- stopping **or** replacing a container preserves the queue, admitted proposals, source Atoms, shared Journal **and** full reports.
- readiness, queue admission, Agent completion **and** accepted Workflow completion remain separate results.
- a new Docker queue does **not** silently import **or** execute a native queue's requests. an authorized pending request can be admitted explicitly with fresh source **and** rule bindings.
- interruption preserves uncertain dispatches for reconciliation rather than automatically repeating them.
