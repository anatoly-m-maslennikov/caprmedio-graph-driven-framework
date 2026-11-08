---
atom_id: CA-R-1187
ref_id: CA-R-1187@20
container:
  scope_unit: CA-SU-15
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component
    Structure
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
tier: 3
status: Archived
version: 20
updated_at: 2026-11-03 23:17:14 +0400
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: APPS
author: Anatoly Maslennikov
destination:
  file:
    name: CA-R-1187@20-PROGRAMMATIC-RULE-APPS--own-operator-facing-application-products-and-agent-host-plugins.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/archived
---
# Summary

Own Operator-Facing Application Products and Agent-Host Plugins

## Scope

PROGRAMMATIC behavior governing APPS.

## Claim

APPS **must** own CAPRMEDIO application services, optional Operator-facing interfaces, Workflow orchestration, **and** agent-host plugin packages. A headless application service **must not** depend on its optional UI.

APPS **must** contain the unordered WORKBENCH, GRAPH_UI, WORKFLOW_ORCHESTRATOR, MCP and AGENT_HOST_PLUGINS Scope Units. MCP and WORKFLOW_ORCHESTRATOR are peers: MCP supplies discovery and transport; WORKFLOW_ORCHESTRATOR owns Workflow execution and coordination. GRAPH_UI remains optional at runtime; WORKBENCH supports headless use.

## Details
