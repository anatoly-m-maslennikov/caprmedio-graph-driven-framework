---
atom_id: CA-E-534
ref_id: CA-E-534
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
tier: 3
status: Active
version: 11
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-E-534-MCP-EVAL_CASE--verify-in-flight-call-isolation-during-mcp-reload.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
current_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

Verify in-flight call isolation during MCP reload

## Claim

### Prose Claim

the MCP Evaluation **must** verify that reload preserves admitted call identity, authority **and** truthful outcomes.

## Details

### Scope

These in-flight generation checks apply only with optional hot reload explicitly enabled.

server-side hot reload for the Project-local MCP gateway.

- hold a call on A while publishing B; verify that the old call completes on A **and** a new call executes on B.
- verify that old generations remain alive while their admitted calls are running.
- simulate child-process failure **after** a mutating call starts; verify an explicit uncertain outcome **and** no automatic replay.
- exercise concurrent reload requests, duplicate request IDs **and** drain limits; verify serialized publication **and** bounded explicit diagnostics.
- verify that reload does **not** start a Workflow, Codex Agent, independent worker **or** source mutation.
- verify that get_mcp_reload_status advertises read-only metadata **and** returns generation state without reload **or** persistence.
- verify that reload_mcp_implementation remains state-changing, rejects operation status **and** does **not** alter client permission settings.
- retain existing MCP request validation **and** Project-boundary regression tests.
