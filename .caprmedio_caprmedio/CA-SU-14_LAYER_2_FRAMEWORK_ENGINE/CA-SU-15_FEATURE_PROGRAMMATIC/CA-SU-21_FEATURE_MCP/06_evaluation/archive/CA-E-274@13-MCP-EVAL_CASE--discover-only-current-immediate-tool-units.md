---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Graph Node/Engineering/MCP
  depends_on: []
version: 13
updated_at: 2026-10-25 17:32:27 +0400
relations:
  evaluation_for:
  - CA-M-168
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-274@13
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: MCP
type: Eval Case
tier: 3
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
