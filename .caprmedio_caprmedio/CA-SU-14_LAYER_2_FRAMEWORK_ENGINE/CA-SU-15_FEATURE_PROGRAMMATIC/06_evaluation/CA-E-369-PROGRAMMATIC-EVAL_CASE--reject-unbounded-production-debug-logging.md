---
atom_id: CA-E-369
ref_id: CA-E-369
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control
  dependencies:
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Requirement)
  - MODEL//CAPRMEDIO <+ Carrier
tier: 5
relations:
  evaluation_for:
  - CA-M-414
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
    name: CA-E-369-PROGRAMMATIC-EVAL_CASE--reject-unbounded-production-debug-logging.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Reject unbounded production DEBUG logging

## Claim

### Prose Claim

Reject production DEBUG enabled globally without automatic expiry. Any enablement requires bounded component/subject/run/entity-or-equivalent scope and unchanged redaction.
