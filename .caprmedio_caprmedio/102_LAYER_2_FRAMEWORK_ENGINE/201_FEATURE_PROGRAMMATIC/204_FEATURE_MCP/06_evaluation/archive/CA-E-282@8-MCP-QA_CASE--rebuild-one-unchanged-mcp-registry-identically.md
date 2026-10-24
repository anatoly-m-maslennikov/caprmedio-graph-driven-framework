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
  - CA-M-176
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-282@8
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: MCP
---
# Rebuild one unchanged MCP registry identically

## Claim checked

Repeated MCP registry generation over one unchanged sealed frontier is semantically idempotent.

## Test case

Generate the registry twice from the same Tool-contract **and** project frontier.

## Acceptance criteria

the two registries have the same capability identities **and** schemas; volatile execution metadata does **not** change that result.

## Failure disposition

Stop publication **and** report the first nondeterministic source **or** ordering defect.
