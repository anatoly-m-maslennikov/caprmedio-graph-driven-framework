---
atom_id: CA-E-813
ref_id: CA-E-813
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source
    Selection
tier: 3
relations:
  evaluation_for:
  - CA-M-512
  derived_from:
  - CA-A-057
  IS_REPLACEMENT_FOR:
  - CA-E-283
status: Active
version: 1
updated_at: 2026-11-09 07:45:15 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-E-813-MCP-EVAL_CASE--reject-invalid-mcp-project-and-registration-bindings.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
---

## Summary


Reject invalid MCP Project and registration bindings

## Claim

### Prose Claim

Verify that an MCP invocation binds to one validated ProjectSelection and current generated registration revision. Reject a foreign, missing or stale selected binding before Tool invocation.

## Details

Invoke through a foreign Project binding and a stale registration revision. Both fail before Tool execution with provenance identifying the failed boundary; no root or revision is guessed.
