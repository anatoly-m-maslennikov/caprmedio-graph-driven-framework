---
atom_id: CA-E-376
ref_id: CA-E-376
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Authoring <+ Code Authoring <+ Python Code
  dependencies:
  - MODEL//CAPRMEDIO <+ Asset
tier: 5
relations:
  evaluation_for:
  - CA-M-423
  - CA-M-429
  DERIVED_FROM:
  - CA-A-053
status: Active
version: 24
updated_at: 2026-11-10 20:47:54 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
destination:
  file:
    name: CA-E-376-PROGRAMMATIC-EVAL_CASE--reproduce-a-locked-uv-environment.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Reproduce a locked uv environment

## Claim

### Prose Claim

From an empty environment, `uv sync --locked` then declared `uv run --locked` must use the selected Python boundary and Method-selected dependencies without changing `pyproject.toml` or `uv.lock`; stale lock, implicit resolution or unauthorized dependency rejects reproducibility.
