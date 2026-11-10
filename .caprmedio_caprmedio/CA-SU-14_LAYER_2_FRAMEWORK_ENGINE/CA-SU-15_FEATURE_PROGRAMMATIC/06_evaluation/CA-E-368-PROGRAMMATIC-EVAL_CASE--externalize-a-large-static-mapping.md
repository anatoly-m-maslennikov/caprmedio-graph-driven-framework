---
atom_id: CA-E-368
ref_id: CA-E-368
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
    <+ Verification <+ Static Analysis <+ Python Code
tier: 6
relations:
  evaluation_for:
  - CA-M-419
  - CA-E-539
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
    name: CA-E-368-PROGRAMMATIC-EVAL_CASE--externalize-a-large-static-mapping.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Externalize a large static mapping

## Claim

### Prose Claim

A changed Python module with a reusable static mapping over 20 entries or 25 lines must externalize it: TOML by default, JSON for schema/interchange, YAML only for a declared distinct feature. Its typed loader validates without changing meaning.
