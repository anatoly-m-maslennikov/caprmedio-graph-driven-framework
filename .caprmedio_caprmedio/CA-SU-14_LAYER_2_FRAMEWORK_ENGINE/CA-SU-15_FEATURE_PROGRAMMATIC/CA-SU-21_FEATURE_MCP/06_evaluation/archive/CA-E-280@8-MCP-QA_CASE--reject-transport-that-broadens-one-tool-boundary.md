---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: framework-engine-mcp
  depends_on: []
version: 8
updated_at: 2026-10-24 00:51:05 +0400
relations:
  evaluation_for:
  - CA-M-174
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-280@8
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: MCP
---
# Reject transport that broadens one Tool boundary

## Claim checked

MCP cannot alter a canonical Tool's authority, cardinality, failure, **or** side-effect boundary.

## Test case

Forward one Atom Doer request while attempting **to** substitute a broader target set **or** success for a partial Tool outcome.

## Acceptance criteria

the request is rejected **or** the exact Tool outcome is retained; no broader **or** fabricated success crosses the boundary.

## Failure disposition

Stop the invocation **and** record the attempted semantic alteration.
