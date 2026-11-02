---
atom_id: CA-R-1818
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Active
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-27 20:00:03 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
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
