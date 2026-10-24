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
  - CA-M-167
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-273@6
status: Archived
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
