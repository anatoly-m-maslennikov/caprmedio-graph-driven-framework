---
subjects:
  governs: Subject/Graph Node/Engineering/MCP
  depends_on: []
version: 19
updated_at: 2026-10-25 17:32:27 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1115@19
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: MCP
type: Rule
tier: 1
---
# Bind MCP operation to the current project frontier

A legacy one-Project MCP service instance **must** bind **to** exactly one
resolved CAPRMEDIO Project root, selected installed Tool release, current
project-graph frontier, **and** generated MCP registry revision. In the shared
service, native Tool execution and invocation **must** bind **to** exactly one
validated Project identity and frontier. Host-scoped Tool discovery **may**
publish the initial union of compatible Project frontiers, with per-Project
source and revision provenance; the union is not a selected Project and must
not be treated as one. Discovery **and** results **must** expose sufficient
source **and** revision provenance **to** diagnose currentness; cross-project
path escape, unresolved project identity, **and** invocation through a stale
registry **must** fail explicitly.

Scope check: the legacy launcher’s service instance remains one-Project. The
shared service’s host-scoped discovery union is not a selected Project; every
native execution/invocation remains bound to one validated Project
identity/frontier.
