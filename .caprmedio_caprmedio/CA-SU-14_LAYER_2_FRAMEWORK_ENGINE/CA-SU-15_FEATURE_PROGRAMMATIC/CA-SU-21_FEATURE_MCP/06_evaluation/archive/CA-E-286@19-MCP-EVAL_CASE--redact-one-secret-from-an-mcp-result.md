---
atom_id: CA-E-286
ref_id: CA-E-286@19
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
tier: 3
relations:
  evaluation_for:
  - CA-R-1118
  derived_from:
  - CA-A-057
status: Archived
version: 19
updated_at: 2026-11-09 21:15:45 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-E-286@19-MCP-EVAL_CASE--redact-one-secret-from-an-mcp-result.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation/archive
---

## Summary

Redact one secret from an MCP result

## Claim

### Prose Claim

MCP does **not** expose a secret through a projected capability result **or** diagnostic.

## Details

### Test case

Inject one secret-bearing diagnostic value into a Tool result fixture.

### Acceptance criteria

the public MCP representation excludes that value while retaining the classified failure meaning.

### Failure disposition

Stop the affected capability **and** treat the representation as a secret-boundary defect.
