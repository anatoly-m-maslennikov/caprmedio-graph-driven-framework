---
atom_id: CA-E-273
ref_id: CA-E-273
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
tier: 3
relations:
  evaluation_for:
  - CA-M-167
  derived_from:
  - CA-A-057
status: Active
version: 17
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
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
