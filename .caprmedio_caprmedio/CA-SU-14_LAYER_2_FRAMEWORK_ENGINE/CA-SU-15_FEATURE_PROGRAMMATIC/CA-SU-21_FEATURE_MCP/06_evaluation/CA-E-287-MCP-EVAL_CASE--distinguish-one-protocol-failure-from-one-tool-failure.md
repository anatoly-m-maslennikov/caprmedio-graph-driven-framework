---
atom_id: CA-E-287
ref_id: CA-E-287
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Result and Status
    Presentation
tier: 3
relations:
  evaluation_for:
  - CA-R-1119
  DERIVED_FROM:
  - CA-A-057
status: Active
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
    name: CA-E-287-MCP-EVAL_CASE--distinguish-one-protocol-failure-from-one-tool-failure.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
---

## Summary

Distinguish one protocol failure from one Tool failure

## Claim

### Prose Claim

MCP returns stable model-readable responses that distinguish a protocol failure from a canonical Tool failure.

## Details

### Test case

Produce one invalid protocol message **and** one valid message whose canonical Tool returns a structured failure.

### Acceptance criteria

the two responses are distinct, retain applicable provenance, **and** expose no internal implementation detail.

### Failure disposition

Reject the result adapter **until** it preserves the required distinction.
