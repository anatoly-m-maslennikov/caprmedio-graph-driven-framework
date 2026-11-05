---
atom_id: CA-R-1818
ref_id: CA-R-1818
container:
  scope_unit: CA-SU-2
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
tier: 3
status: Active
version: 12
updated_at: 2026-10-27 20:00:03 +0400
carrier_destination:
  file:
    name: CA-R-1818-WORKFLOW_ORCHESTRATOR-RULE--provide-an-explicitly-managed-docker-runtime.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/04_requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
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
