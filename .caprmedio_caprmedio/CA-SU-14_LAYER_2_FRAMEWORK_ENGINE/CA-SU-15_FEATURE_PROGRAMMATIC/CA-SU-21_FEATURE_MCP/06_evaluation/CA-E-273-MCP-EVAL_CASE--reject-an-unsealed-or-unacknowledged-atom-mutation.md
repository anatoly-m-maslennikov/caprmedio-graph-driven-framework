---
atom_id: CA-E-273
ref_id: CA-E-273
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
status: Active
version: 20
updated_at: 2026-11-11 17:36:58 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-E-273-MCP-EVAL_CASE--reject-an-unsealed-or-unacknowledged-atom-mutation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
---

## Summary

Reject an unsealed or unacknowledged Atom mutation

## Claim scope

Initiative-bound Atom Tools. The six direct Project Atom Lifecycle Tools use the lifecycle contract in CA-R-1105.

## Claim

### Prose Claim

For an Initiative-bound Atom Tool, MCP delegates the mutation with one authorized Initiative and returns success only from the canonical Tool's acknowledged outcome.

## Details

### Test case

Submit one mutation request with a missing Initiative, **then** a request whose canonical Tool returns an unacknowledged result.

### Acceptance criteria

Both requests fail explicitly; MCP neither resolves a target nor reports success.

### Failure disposition

Reject the MCP mutation boundary **and** retain the canonical Tool as the operation owner.
