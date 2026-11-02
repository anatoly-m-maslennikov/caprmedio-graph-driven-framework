---
atom_id: CA-D-522@12
content_role: Delivery
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-26 05:59:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Execution Control
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Engineering/Workflow Orchestration/Dependency Declaration
relations: {}
type: Eng Decision
tier: 3
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
