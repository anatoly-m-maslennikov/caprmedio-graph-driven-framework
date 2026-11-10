---
atom_id: CA-E-373
ref_id: CA-E-373
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
    <+ Verification <+ Dynamic Testing
  dependencies:
  - MODEL//CAPRMEDIO <+ Package/Project Package
tier: 4
relations:
  evaluation_for:
  - CA-R-1095
  DERIVED_FROM:
  - CA-A-058
status: Active
version: 20
updated_at: 2026-11-10 20:47:54 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
destination:
  file:
    name: CA-E-373-PROGRAMMATIC-EVAL_CASE--reject-duplicate-or-mismatched-provenance-bindings.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Reject duplicate or mismatched provenance bindings

## Claim

### Prose Claim

Block reconciliation when canonical records or real-change commits duplicate, or revision/digest mismatch. Report the discrepancy without guessing a record; require deterministic repair to one binding.
