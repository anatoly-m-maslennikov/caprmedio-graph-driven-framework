---
atom_id: CA-E-385
ref_id: CA-E-385
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
    <+ Verification <+ Static Analysis
  dependencies: []
tier: 6
relations:
  evaluation_for:
  - CA-M-427
  - CA-E-540
  DERIVED_FROM:
  - CA-A-053
status: Active
version: 22
updated_at: 2026-11-10 20:47:54 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
carrier_destination:
  file:
    name: CA-E-385-PROGRAMMATIC-EVAL_CASE--verify-changed-python-with-mypy.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Verify changed Python with Mypy

## Claim

### Prose Claim

New Python must pass strict admitted Mypy; changed Python must not regress below passing baseline. An incompatible return and unexplained broad suppression both reject the target; only a narrow explained accepted suppression can remain.
