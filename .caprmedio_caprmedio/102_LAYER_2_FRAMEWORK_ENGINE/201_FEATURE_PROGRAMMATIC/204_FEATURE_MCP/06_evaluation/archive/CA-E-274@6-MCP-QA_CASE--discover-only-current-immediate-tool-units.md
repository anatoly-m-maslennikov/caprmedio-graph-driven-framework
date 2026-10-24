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
  - CA-M-168
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-274@6
status: Archived
---
# Discover only current immediate Tool units

## Claim checked

MCP derives its source set from current immediate Tool units rather than helper folders.

## Test case

Add one enabled immediate Tool, one disabled immediate Tool, **and** one nested helper **to** a resolved test topology.

## Acceptance criteria

Discovery includes **only** the enabled immediate Tool **and** reports the other two dispositions explicitly.

## Failure disposition

Stop registry generation on an unresolved source identity.
