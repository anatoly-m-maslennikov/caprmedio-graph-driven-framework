---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
version: 20
updated_at: 2026-11-03 23:17:14 +0400
relations: {}
atom_id: CA-R-1187
content_role: Requirement
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: APPS
status: Active
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary

Own Operator-Facing Application Products and Agent-Host Plugins

## Scope

PROGRAMMATIC behavior governing APPS.

## Claim

APPS **must** own CAPRMEDIO application services, optional Operator-facing interfaces, Workflow orchestration, **and** agent-host plugin packages. A headless application service **must not** depend on its optional UI.

APPS **must** contain the unordered WORKBENCH, GRAPH_UI, WORKFLOW_ORCHESTRATOR, MCP and AGENT_HOST_PLUGINS Scope Units. MCP and WORKFLOW_ORCHESTRATOR are peers: MCP supplies discovery and transport; WORKFLOW_ORCHESTRATOR owns Workflow execution and coordination. GRAPH_UI remains optional at runtime; WORKBENCH supports headless use.

## Details
