---
identity:
  atom_id: CA-R-1811
  ref_id: CA-R-1811
context:
  container:
    scope_unit: CA-SU-21
  role: requirement
  form: rule
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Discovery and Navigation
    dependencies:
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Operations)/Action
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Operations)/Workflow
    - MODEL//CAPRMEDIO <+ Atom
    - MODEL//CAPRMEDIO <+ Scope Unit
    - MODEL//CAPRMEDIO <+ Package/Project Package
    - MODEL//CAPRMEDIO <+ Execution/Workflow Run
    - MODEL//CAPRMEDIO <+ Journal
  tier: 3
state:
  status: Active
  version: 14
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-1811-MCP-RULE--expose-discovery-and-execution-observation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement
current_scope_unit: MCP
author: Anatoly Maslennikov
---
## Summary

Expose discovery and execution observation

## Claim scope

the MCP capability for MCP.

## Claim

### Prose Claim

the MCP interface **must** expose the declared discovery, context **and** execution-observation Tools with the canonical Implementation's input schemas **and** results.

## Details

- expose discover_tools, discover_operations, get_execution_context, get_execution_status, resume_execution_context **and** watch_execution.
- call the same canonical Tool code used by direct invocation.
- watch_execution provides caller-requested updates through a bounded wait; an idle MCP connection does **not** independently deliver a new chat message.
- report supported Run backends explicitly; unsupported Workflow **or** standalone Action Runs remain explicit rather than fabricated.
