---
atom_id: CA-M-177@20
ref_id: CA-M-177@20
container:
  scope_unit: CA-SU-21
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
tier: 2
relations:
  method_for:
  - CA-R-1115
  derived_from:
  - CA-A-057
status: Archived
version: 20
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-M-177@20-MCP-ENG_DECISION--bind-one-mcp-invocation-to-its-current-project-frontier.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method/archive
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
