---
cce_version: cce_1
cce_form: evaluation
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Result and Status Presentation
version: 16
updated_at: 2026-11-02 19:44:26 +0400
relations:
  evaluation_for:
  - CA-M-181
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-287
ref_id: CA-E-287
status: Active
role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: MCP
form: Eval Case
tier: 3
container:
  scope_unit: CA-SU-21
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
