---
identity:
  atom_id: CA-R-1187
  ref_id: CA-R-1187@21-draft
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Solution
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component
      Structure
    dependencies:
    - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
  tier: 3
state:
  status: Draft
  version: 21
  updated_at: 2026-11-08 20:40:58 +0400
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: APPS
author: Anatoly Maslennikov
---
## Summary

Own Operator-Facing Application Products and Agent-Host Plugins

## Scope

PROGRAMMATIC behavior governing APPS.

## Claim

APPS **must** own CAPRMEDIO application services, optional Operator-facing interfaces, Workflow orchestration, **and** agent-host plugin packages. A headless application service **must not** depend on its optional UI.

MCP supplies discovery and transport; Workflow orchestration owns Workflow execution and coordination. GRAPH_UI remains optional at runtime; WORKBENCH supports headless use. Structural placement remains governed by the unchanged Current Scope Declarations.

## Details
