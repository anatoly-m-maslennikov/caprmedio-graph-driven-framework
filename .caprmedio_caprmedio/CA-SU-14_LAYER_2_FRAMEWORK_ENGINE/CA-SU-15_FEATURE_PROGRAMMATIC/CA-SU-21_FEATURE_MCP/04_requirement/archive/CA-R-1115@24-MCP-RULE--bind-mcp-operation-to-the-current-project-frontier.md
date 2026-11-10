---
atom_id: CA-R-1115
ref_id: CA-R-1115@24
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source
    Selection
  dependencies:
  - CAPRMEDIO_MODEL <+ Project
tier: 1
status: Archived
version: 24
updated_at: 2026-11-07 13:19:43 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
carrier_destination:
  file:
    name: CA-R-1115@24-MCP-RULE--bind-mcp-operation-to-the-current-project-frontier.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement/archive
---
## Summary

Bind MCP operation to the current project frontier

## Claim

### Prose Claim

A legacy one-Project MCP service instance **must** bind **to** exactly one
resolved CAPRMEDIO Project root, selected installed Tool release, **and** generated code/configuration MCP registry revision. In the shared
service, native Tool execution and invocation **must** bind **to** exactly one
validated Project identity and installed code/configuration frontier. Host-scoped Tool discovery **may**
publish the initial union of compatible Project frontiers, with per-Project
source and revision provenance; the union is not a selected Project and must
not be treated as one. Discovery **and** results **must** expose sufficient
installed-code **and** generated-registry provenance **to** diagnose currentness; cross-project
path escape, unresolved project identity, **and** invocation through a stale
registry **must** fail explicitly.

Scope check: the legacy launcher’s service instance remains one-Project. The
shared service’s host-scoped discovery union is not a selected Project; every
native execution/invocation remains bound to one validated Project
identity/frontier.

Registration and generic invocation do not reread source Atoms to prove registry currentness. Each backend operation retains its own source and business validation when needed.
