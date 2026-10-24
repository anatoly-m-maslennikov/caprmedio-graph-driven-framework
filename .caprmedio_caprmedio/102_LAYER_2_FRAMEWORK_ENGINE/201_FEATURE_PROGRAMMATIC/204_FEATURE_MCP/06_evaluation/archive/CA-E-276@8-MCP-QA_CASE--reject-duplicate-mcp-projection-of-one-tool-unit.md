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
  - CA-M-170
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-276@8
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: MCP
---
# Reject duplicate MCP projection of one Tool unit

## Claim checked

One validated immediate Tool unit yields exactly one callable MCP identity.

## Test case

Attempt **to** publish two callable MCP identities from one valid source Tool.

## Acceptance criteria

Publication fails with a duplicate-projection diagnostic **and** exposes neither alias as current.

## Failure disposition

Stop registry publication **until** the one-to-one mapping is restored.
