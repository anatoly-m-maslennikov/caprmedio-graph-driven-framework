---
atom_id: CA-E-455
ref_id: CA-E-455
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
    <+ Verification <+ Static Analysis
  dependencies:
  - MODEL//CAPRMEDIO <+ Package/Project Package
tier: 5
relations:
  evaluation_for:
  - CA-M-420
  DERIVED_FROM:
  - CA-A-053
status: Active
version: 22
updated_at: 2026-11-10 20:47:54 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
destination:
  file:
    name: CA-E-455-PROGRAMMATIC-EVAL_CASE--evaluate-changed-python-targets-under-one-configuration.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Evaluate changed Python targets under one configuration

## Claim

### Prose Claim

Every changed Python target retains separate syntax, Ruff, Mypy and relevant behavioral evidence under one declared interpreter/configuration. A failed mechanism fails aggregate gate with target, diagnostic, boundary and replay command; no masking.
