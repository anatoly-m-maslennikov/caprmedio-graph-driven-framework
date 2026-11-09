---
atom_id: CA-M-320
ref_id: CA-M-320
container:
  scope_unit: CA-SU-2
role: Method
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
    Structure
tier: 4
status: Active
version: 15
updated_at: 2026-11-09 19:30:15 +0400
carrier_destination:
  file:
    name: CA-M-320-WORKFLOW_ORCHESTRATOR-DECISION--coordinate-local-runs-with-dbos.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/05_method
current_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
relations:
  method_for:
  - CA-R-1605
---

## Summary

Coordinate local Runs with DBOS

## Claim

### Prose Claim

implement independent execution through DBOS durable queues **and** a separately started local worker.

## Details

### Scope

WORKFLOW_ORCHESTRATOR's initial local execution capability.

1. validate **and** freeze the submitted request before queue admission; duplicate Run IDs accept **only** the same frozen request.
2. register **=1** Project queue with concurrency **=1** initially, preventing competing source edits.
3. use durable Steps for gather, Agent dispatch, admitted report recording **and** finalization; workflow ordering is gather, check, fix, with no recheck.
4. expose queue state through a client adapter; keep DBOS checkpoints operational, with confirmed Workflow events **in** the shared Journal.
5. start the worker explicitly. installation **or** discovery starts no Run **and** installs no hook.

### Conditional future AI-Agent execution

Agent-result parsing, mock-Agent scheduling and Agent dispatch, where mentioned above, apply only to separately admitted AI-Agent execution. The retained deterministic contract does not start or restore an Agent runtime.
