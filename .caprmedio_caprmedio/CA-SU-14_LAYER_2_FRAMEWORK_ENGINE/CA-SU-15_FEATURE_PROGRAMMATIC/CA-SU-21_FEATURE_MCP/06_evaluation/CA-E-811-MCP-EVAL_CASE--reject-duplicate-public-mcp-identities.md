---
atom_id: CA-E-811
ref_id: CA-E-811
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
tier: 3
relations:
  evaluation_for:
  - CA-R-1108
  derived_from:
  - CA-A-057
  IS_REPLACEMENT_FOR:
  - CA-E-276
status: Active
version: 2
updated_at: 2026-11-09 21:15:45 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-E-811-MCP-EVAL_CASE--reject-duplicate-public-mcp-identities.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
---

## Summary

Reject duplicate public MCP identities

## Claim

### Prose Claim

Verify that each enabled code-owned registration entry yields one callable MCP identity and duplicate public identities refuse publication.

## Details

Attempt to publish two generated entries with the same public MCP identity. Reject the duplicate identity with an explicit diagnostic and expose neither conflicting entry as current.
