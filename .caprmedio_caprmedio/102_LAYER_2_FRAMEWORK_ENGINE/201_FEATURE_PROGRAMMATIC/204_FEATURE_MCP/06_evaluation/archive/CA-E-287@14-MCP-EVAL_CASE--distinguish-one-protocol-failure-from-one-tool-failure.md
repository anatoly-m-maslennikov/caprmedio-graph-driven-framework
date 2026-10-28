---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Graph Node/UX/MCP Model-readable Result Interface
  depends_on: []
version: 14
updated_at: 2026-10-26 00:46:35 +0400
relations:
  evaluation_for:
  - CA-M-181
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-287@14
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: MCP
type: Eval Case
tier: 3
---
# Distinguish one protocol failure from one Tool failure

## Claim checked

MCP returns stable model-readable responses that distinguish a protocol failure from a canonical Tool failure.

## Test case

Produce one invalid protocol message **and** one valid message whose canonical Tool returns a structured failure.

## Acceptance criteria

the two responses are distinct, retain applicable provenance, **and** expose no internal implementation detail.

## Failure disposition

Reject the result adapter **until** it preserves the required distinction.
