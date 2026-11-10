---
atom_id: CA-R-1115
ref_id: CA-R-1115
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Data Handling <+ Source Selection
  dependencies:
  - MODEL//CAPRMEDIO <+ Project
tier: 1
status: Active
version: 25
updated_at: 2026-11-10 20:47:54 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-R-1115-MCP-RULE--bind-mcp-operation-to-the-current-project-frontier.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement
---
## Summary

Bind MCP operation to the current project frontier

## Claim

### Prose Claim

A legacy one-Project MCP service instance **must** bind **to** exactly one resolved CAPRMEDIO Project root, selected installed Tool release, and generated code/configuration MCP registry revision. In the shared service, native Tool execution/invocation **must** bind **to** exactly one validated Project identity and installed code/configuration frontier. Host-scoped Tool discovery **may** publish the initial union of compatible Project frontiers with per-Project source/revision provenance, but the union is not a selected Project. Discovery and results expose enough installed-code and generated-registry provenance to diagnose currentness; cross-project path escape, unresolved identity, or stale-registry invocation fails explicitly.

The legacy launcher remains one-Project; shared discovery union is not a selected Project and each native execution remains bound to one validated identity/frontier. Registration and generic invocation do not reread source Atoms to prove currentness; each backend operation retains its own source/business validation.
