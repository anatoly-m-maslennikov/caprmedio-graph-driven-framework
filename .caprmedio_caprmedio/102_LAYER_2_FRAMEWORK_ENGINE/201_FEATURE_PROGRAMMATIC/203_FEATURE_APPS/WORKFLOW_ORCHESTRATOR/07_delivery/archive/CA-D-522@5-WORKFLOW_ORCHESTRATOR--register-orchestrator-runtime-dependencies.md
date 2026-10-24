---
atom_id: CA-D-522@5
content_role: Delivery
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-23 23:09:56 +0400
subjects:
  governs: Subject/Engineering/Workflow Orchestration/Dependency Declaration
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Continuant/Atom
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Journal
  - Implementation
  - Subject/Engineering/Workflow Orchestration/Dependency Declaration
relations:
  relates_to:
  - CA-R-1522
  - CA-R-1523
  - CA-R-1524
  - CA-O-104
type: Eng Decision
---
# Summary

Register orchestrator runtime dependencies

## Scope

WORKFLOW_ORCHESTRATOR's initial local execution capability.

## Claim

the WORKFLOW_ORCHESTRATOR runtime **must** declare its selected DBOS, Pydantic **and** PyYAML dependencies **in** the workflow-orchestrator dependency group.

## Details

- DBOS provides durable orchestration with a local SQLite backend.
- Pydantic admits strict JSON requests **and** Agent results; PyYAML supports safe Atom Carrier parsing.
- Codex CLI is a separately installed executable selected through the runner boundary; no Claude backend is implemented yet.
- versions are pinned **after** compatibility verification with the repository's supported Python series. runtime installation does **not** launch a worker **or** execute a Project Run.
