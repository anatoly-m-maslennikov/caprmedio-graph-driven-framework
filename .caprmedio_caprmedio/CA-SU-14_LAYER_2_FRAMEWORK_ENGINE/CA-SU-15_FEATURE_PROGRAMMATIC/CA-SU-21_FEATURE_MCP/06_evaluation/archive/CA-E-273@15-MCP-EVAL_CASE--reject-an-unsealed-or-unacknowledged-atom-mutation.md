---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Graph Node/Engineering/Architecture/Communication
  depends_on: []
version: 15
updated_at: 2026-10-27 06:04:45 +0400
relations:
  evaluation_for:
  - CA-M-167
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-273@15
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: MCP
type: Eval Case
tier: 3
---
# Reject an unsealed or unacknowledged Atom mutation

## Claim checked

MCP delegates an Atom mutation **only** with one authorized Initiative **and** returns success **only** from the canonical Tool's acknowledged outcome.

## Test case

Submit one mutation request with a missing Initiative, **then** a request whose canonical Tool returns an unacknowledged result.

## Acceptance criteria

Both requests fail explicitly; MCP neither resolves a target nor reports success.

## Failure disposition

Reject the MCP mutation boundary **and** retain the canonical Tool as the operation owner.
