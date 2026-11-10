---
atom_id: CA-M-320@2
content_role: Method
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: 2026-10-23 01:47:30 +0400
subjects:
  governs: Subject/Engineering/Workflow Orchestration/DBOS Queue and Worker Coordination
  depends_on:
  - Workflow
  - Action
  - Atom
  - Operator
  - Journal
  - Implementation
  - Subject/Engineering/Workflow Orchestration/DBOS Queue and Worker Coordination
relations:
  relates_to: [CA-R-1522, CA-R-1523, CA-R-1524, CA-O-104]
type: Engineering Decision
---
# Summary

Coordinate local Runs with DBOS

## Scope

WORKFLOW_ORCHESTRATOR's initial local execution capability.

## Claim

implement independent execution through DBOS durable queues **and** a separately started local worker.

## Details

1. validate **and** freeze the submitted request before queue admission; duplicate Run IDs accept **only** the same frozen request.
2. register **=1** Project queue with concurrency **=1** initially, preventing competing source edits.
3. use durable Steps for gather, Agent dispatch, admitted report recording **and** finalization; workflow ordering is gather, check, fix, with no recheck.
4. expose queue state through a client adapter; keep DBOS checkpoints operational, with confirmed Workflow events **in** the shared Journal.
5. start the worker explicitly. installation **or** discovery starts no Run **and** installs no hook.
