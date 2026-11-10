---
atom_id: CA-M-504
ref_id: CA-M-504@3
container:
  scope_unit: CA-SU-21
role: Method
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
tier: 4
status: Archived
version: 3
updated_at: 2026-11-09 07:45:15 +0400
carrier_destination:
  file:
    name: CA-M-504@3-MCP-DECISION--remove-ai-agent-orchestration-from-the-runtime.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method/archive
current_scope_unit: MCP
claim_target_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

Remove AI Agent orchestration from the runtime

## Claim

### Prose Claim

Remove automatic AI Agent dispatch and its Codex CLI adapters, AI-Agent transport, mock runners, agentic handlers, AI-Agent Docker service/image stage and credentials setup. Keep the main Docker runtime and MCP transports, the general Workflow engine, durable queue, deterministic Action handlers, MCP, Workbench and host Release commands. Retain RMED source Atoms and persisted historical Run data. A request requiring removed Agent execution must stop with an explicit unsupported result before it is queued or starts effects; never substitute a mock Agent.
