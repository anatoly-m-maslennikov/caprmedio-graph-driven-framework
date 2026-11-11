---
atom_id: CA-E-273
ref_id: CA-E-273@19
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Communication
tier: 3
relations:
  evaluation_for:
  - CA-M-167
  DERIVED_FROM:
  - CA-A-057
status: archived
version: 19
updated_at: 2026-11-10 20:47:54 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-E-273@19-MCP-EVAL_CASE--reject-an-unsealed-or-unacknowledged-atom-mutation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation/archive
---

## Summary

Reject an unsealed or unacknowledged Atom mutation

## Claim

### Prose Claim

MCP delegates an Atom mutation **only** with one authorized Initiative **and** returns success **only** from the canonical Tool's acknowledged outcome.

## Details

### Test case

Submit one mutation request with a missing Initiative, **then** a request whose canonical Tool returns an unacknowledged result.

### Acceptance criteria

Both requests fail explicitly; MCP neither resolves a target nor reports success.

### Failure disposition

Reject the MCP mutation boundary **and** retain the canonical Tool as the operation owner.
