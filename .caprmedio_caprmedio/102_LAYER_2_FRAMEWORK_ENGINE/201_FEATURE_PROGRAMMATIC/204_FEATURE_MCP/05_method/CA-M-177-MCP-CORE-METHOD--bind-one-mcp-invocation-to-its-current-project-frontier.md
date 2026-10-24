---
cce_version: cce_1
cce_form: method
subjects:
  governs: framework-engine-mcp
  depends_on: []
version: 12
updated_at: 2026-10-24 02:14:24 +0400
relations:
  method_for:
  - CA-R-1115
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-M-177
status: Active
content_role: Method
author: Anatoly Maslennikov
current_scope_unit: MCP
type: Eng Decision
tier: 2
---
# Bind one MCP invocation to its current project frontier

## Applicable when

Apply **when** an MCP service instance discovers **or** invokes an exposed Tool.

## Procedure

1. Resolve exactly one explicit Project identity, project root, selected
   installed Tool release, project-graph frontier, **and** MCP registry
   revision for each call.
2. Include sufficient source **and** revision provenance **in** discovery
   **and** result records; carry the outer project root only at the native
   request schema root while preserving the native request and result.
3. Reject cross-project path escape, unresolved identity, **or** a stale registry **before** Tool invocation.

## Outcome

**every** MCP operation is attributable **to** one current Project **and** Tool
frontier, even when one shared service publishes a union of valid Project
frontiers.

## Failure or stop

Stop at an unresolved **or** stale frontier; do **not** guess a project **or** release.
