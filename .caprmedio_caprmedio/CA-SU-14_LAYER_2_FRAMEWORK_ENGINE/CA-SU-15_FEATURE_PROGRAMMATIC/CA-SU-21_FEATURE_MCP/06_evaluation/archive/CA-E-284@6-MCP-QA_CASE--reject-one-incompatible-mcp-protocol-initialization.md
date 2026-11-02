---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: framework-engine-mcp
  depends_on: []
version: 6
updated_at: 2026-10-23 03:17:34 +0400
relations:
  evaluation_for:
  - CA-M-178
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-284@6
status: Archived
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
