---
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Entry
version: 23
updated_at: 2026-11-05 13:48:40 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1113
ref_id: CA-R-1113
status: Active
role: Requirement
author: Anatoly Maslennikov
current_scope_unit: MCP
form: Rule
tier: 1
carrier_destination:
  file:
    name: CA-R-1113-MCP-RULE--provide-one-project-local-provider-neutral-mcp-service.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement
container:
  scope_unit: CA-SU-21
---

## Summary

Provide one project-local provider-neutral MCP service

## Claim

One project-local provider-neutral MCP service **must** expose the complete active callable surface for Tools, Prompts and Workflows; CAPRMEDIO **must not** require one MCP server per capability. Programmatic calls return their results. Prompt calls return the selected prompt plus its invocation envelope for the main session. Workflow calls start or resume the applicable Workflow Run and return the next programmatic result, interactive Step invocation, Operator request, completion or failure state. Every exposed capability **must** remain usable headlessly without GRAPH_UI or an agent-host plugin. Agent-host plugins **may** package or connect to MCP but **must not** become the owner of provider-neutral MCP, Tool, Prompt or Workflow behavior.

Each MCP Tool call **must** be bound to the one trusted ProjectSelection of the service before native Tool dispatch. The Codex hook may carry a top-level project_root assertion. In single-Project mode it is optional for compatibility: omission uses the fixed bound Project, while a supplied value must match that Project's canonical host/container mapping and identity. In shared mode project_root is required and must select the already admitted ProjectSelection. A malformed or mismatched value is rejected before Tool execution and never switches the Project. The MCP boundary removes this hook field before passing native Tool arguments. MCP protocol operations such as initialize and tools/list are not treated as Tool-call argument envelopes; Workflow and Prompt wrappers keep their normal native dispatch.

Scope check: one project-local binds each service operation to one resolved Project frontier. A shared host may serve multiple explicit Project bindings through one service under CA-R-2008; this requirement does not impose a process-global one-Project restriction or a global current_project.
