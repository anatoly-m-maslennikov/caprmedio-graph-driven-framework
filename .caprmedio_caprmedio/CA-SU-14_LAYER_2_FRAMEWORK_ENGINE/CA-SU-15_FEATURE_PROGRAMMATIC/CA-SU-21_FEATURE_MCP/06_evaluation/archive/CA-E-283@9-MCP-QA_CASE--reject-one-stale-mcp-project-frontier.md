---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: framework-engine-mcp
  depends_on: []
version: 9
updated_at: 2026-10-24 01:18:03 +0400
relations:
  evaluation_for:
  - CA-M-177
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-283@9
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: MCP
type: Eval Case
---
# Reject one stale MCP project frontier

## Claim checked

An MCP invocation **must** bind **to** one current project, installed release, graph frontier, **and** registry revision.

## Test case

Invoke one Tool through a registry made stale by a changed project frontier.

## Acceptance criteria

MCP rejects the invocation explicitly **and** exposes enough provenance **to** identify the stale boundary.

## Failure disposition

Stop **before** Tool execution; do **not** guess a current release **or** project root.
