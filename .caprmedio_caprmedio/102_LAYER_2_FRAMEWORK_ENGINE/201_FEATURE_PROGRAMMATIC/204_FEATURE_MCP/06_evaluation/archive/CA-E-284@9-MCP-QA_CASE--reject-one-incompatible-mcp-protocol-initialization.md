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
  - CA-M-178
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-284@9
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: MCP
type: Eval Case
---
# Reject one incompatible MCP protocol initialization

## Claim checked

MCP initialization admits **only** a declared compatible protocol revision **and** capability set.

## Test case

Initialize with one unsupported required protocol capability.

## Acceptance criteria

Initialization fails with a machine-readable incompatibility diagnostic **and** no undefined compatibility mode.

## Failure disposition

Stop the session **before** registry use **or** Tool dispatch.
