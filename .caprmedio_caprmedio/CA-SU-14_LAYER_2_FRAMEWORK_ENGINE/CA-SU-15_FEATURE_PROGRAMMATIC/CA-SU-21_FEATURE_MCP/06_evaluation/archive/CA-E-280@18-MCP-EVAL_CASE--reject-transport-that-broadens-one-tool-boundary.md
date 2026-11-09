---
atom_id: CA-E-280@18
ref_id: CA-E-280@18
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
tier: 3
relations:
  evaluation_for:
  - CA-M-174
  derived_from:
  - CA-A-057
status: Archived
version: 18
updated_at: 2026-11-09 07:45:15 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-E-280@18-MCP-EVAL_CASE--reject-transport-that-broadens-one-tool-boundary.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation/archive
---

## Summary

Reject transport that broadens one Tool boundary

## Claim

### Prose Claim

MCP cannot alter a canonical Tool's authority, cardinality, failure, **or** side-effect boundary.

## Details

### Test case

Forward one Atom Doer request while attempting **to** substitute a broader target set **or** success for a partial Tool outcome.

### Acceptance criteria

the request is rejected **or** the exact Tool outcome is retained; no broader **or** fabricated success crosses the boundary.

### Failure disposition

Stop the invocation **and** record the attempted semantic alteration.
