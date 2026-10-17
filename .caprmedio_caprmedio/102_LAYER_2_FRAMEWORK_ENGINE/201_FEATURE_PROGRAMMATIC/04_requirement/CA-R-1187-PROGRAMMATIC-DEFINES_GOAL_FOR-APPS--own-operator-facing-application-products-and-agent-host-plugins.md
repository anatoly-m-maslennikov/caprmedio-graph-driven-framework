---
subjects:
  governs: APPS/Goal
  depends_on:
  - PROGRAMMATIC
version: 11
updated_at: "2026-10-18 03:45:03 +0400"
relations: {}
atom_id: CA-R-1187
content_role: Requirement
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: APPS
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
---
# Summary

Own Operator-Facing Application Products and Agent-Host Plugins

## Scope

PROGRAMMATIC behavior governing APPS.

## Claim

APPS **must** own CAPRMEDIO application services, optional Operator-facing interfaces, Workflow orchestration, **and** agent-host plugin packages. A headless application service **must not** depend on its optional UI.

APPS **must** contain the unordered GRAPH_SERVER, GRAPH_UI, WORKFLOW_ORCHESTRATOR, MCP and AGENT_HOST_PLUGINS Scope Units. MCP and WORKFLOW_ORCHESTRATOR are peers: MCP supplies discovery and transport; WORKFLOW_ORCHESTRATOR owns Workflow execution and coordination. GRAPH_UI remains optional at runtime; GRAPH_SERVER supports headless use.

## Details
