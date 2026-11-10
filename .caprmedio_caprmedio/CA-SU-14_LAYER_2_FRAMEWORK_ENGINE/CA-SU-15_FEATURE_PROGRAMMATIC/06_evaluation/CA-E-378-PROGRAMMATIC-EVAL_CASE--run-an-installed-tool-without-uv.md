---
atom_id: CA-E-378
ref_id: CA-E-378
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control
  dependencies:
  - MODEL//CAPRMEDIO <+ Package/Project Package
tier: 5
relations:
  evaluation_for:
  - CA-M-429
  DERIVED_FROM:
  - CA-A-053
status: Active
version: 23
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
    name: CA-E-378-PROGRAMMATIC-EVAL_CASE--run-an-installed-tool-without-uv.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Run an installed Tool without uv

## Claim

### Prose Claim

In a clean process without uv or project environment, an installed Tool must reach its declared entry boundary solely from `.caprmedio_runtime/tools` and admitted host prerequisites.
