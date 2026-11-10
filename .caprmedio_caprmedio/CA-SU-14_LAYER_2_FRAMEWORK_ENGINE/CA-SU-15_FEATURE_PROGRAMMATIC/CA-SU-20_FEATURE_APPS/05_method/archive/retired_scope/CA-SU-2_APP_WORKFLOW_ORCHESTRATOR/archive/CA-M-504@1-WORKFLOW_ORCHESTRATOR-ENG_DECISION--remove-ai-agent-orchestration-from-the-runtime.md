---
atom_id: CA-M-504
ref_id: CA-M-504
container:
  scope_unit: CA-SU-2
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
tier: 4
status: Active
version: 1
updated_at: 2026-11-07 04:18:21 +0400
carrier_destination:
  file:
    name: CA-M-504-WORKFLOW_ORCHESTRATOR-ENG_DECISION--remove-ai-agent-orchestration-from-the-runtime.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/05_method
current_scope_unit: WORKFLOW_ORCHESTRATOR
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
---

## Summary

Remove AI Agent orchestration from the runtime

## Claim

### Prose Claim

Remove automatic AI Agent dispatch and its Codex CLI adapters, transport, mock runners, agentic handlers, Docker service and credentials setup. Keep the general Workflow engine, durable queue, deterministic Action handlers, MCP, Workbench and host Release commands. Retain RMED source Atoms and persisted historical Run data. A request requiring removed Agent execution must stop with an explicit unsupported result before it is queued or starts effects; never substitute a mock Agent.
