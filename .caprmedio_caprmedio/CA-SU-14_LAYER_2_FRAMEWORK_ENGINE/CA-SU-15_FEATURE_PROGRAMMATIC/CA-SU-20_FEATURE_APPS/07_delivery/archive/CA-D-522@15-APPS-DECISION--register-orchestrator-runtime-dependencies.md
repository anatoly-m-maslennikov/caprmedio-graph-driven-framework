---
atom_id: CA-D-522
ref_id: CA-D-522
container:
  scope_unit: CA-SU-20
role: Delivery
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
tier: 3
status: Archived
version: 15
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-D-522@15-APPS-DECISION--register-orchestrator-runtime-dependencies.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/07_delivery/archive
current_scope_unit: APPS
author: Anatoly Maslennikov
---

## Summary

Register orchestrator runtime dependencies

## Claim

### Prose Claim

the WORKFLOW_ORCHESTRATOR runtime **must** declare its selected DBOS, Pydantic **and** PyYAML dependencies **in** the workflow-orchestrator dependency group.

## Details

### Scope

WORKFLOW_ORCHESTRATOR's initial local execution capability.

- DBOS provides durable orchestration with a local SQLite backend.
- Pydantic admits strict JSON requests **and** Agent results; PyYAML supports safe Atom Carrier parsing.
- Codex CLI is a separately installed executable selected through the runner boundary; no Claude backend is implemented yet.
- versions are pinned **after** compatibility verification with the repository's supported Python series. runtime installation does **not** launch a worker **or** execute a Project Run.

### Conditional future AI-Agent execution

Agent-result parsing, mock-Agent scheduling and Agent dispatch, where mentioned above, apply only to separately admitted AI-Agent execution. The retained deterministic contract does not start or restore an Agent runtime.
