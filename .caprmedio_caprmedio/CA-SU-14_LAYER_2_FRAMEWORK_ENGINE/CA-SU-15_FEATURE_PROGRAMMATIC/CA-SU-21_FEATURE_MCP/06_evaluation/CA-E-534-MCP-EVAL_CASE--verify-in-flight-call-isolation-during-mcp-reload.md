---
atom_id: CA-E-534
ref_id: CA-E-534
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control
  dependencies:
  - MODEL//CAPRMEDIO <+ Package/Project Package
  - MODEL//CAPRMEDIO <+ Actor/Operator
  - MODEL//CAPRMEDIO <+ Project
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Operations)/Workflow
  - MODEL//CAPRMEDIO <+ Atom
tier: 3
status: Active
version: 12
updated_at: 2026-11-10 20:47:54 +0400
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

These in-flight generation checks apply only with optional hot reload explicitly enabled for the Project-local MCP gateway.

- Hold a call on A while publishing B; old call completes on A and a new call executes on B. Old generations remain alive while admitted calls run.
- Fail the child process after a mutating call starts; return an explicit uncertain outcome and never replay automatically.
- Exercise concurrent reloads, duplicate request IDs, and drain limits; verify serialized publication and bounded explicit diagnostics.
- Verify reload starts no Workflow, Codex Agent, independent worker, or source mutation; get_mcp_reload_status is read-only generation metadata with no reload/persistence; reload_mcp_implementation remains state-changing, rejects operation status, and does not alter client permission settings.
- Retain MCP request-validation and Project-boundary regression tests.
