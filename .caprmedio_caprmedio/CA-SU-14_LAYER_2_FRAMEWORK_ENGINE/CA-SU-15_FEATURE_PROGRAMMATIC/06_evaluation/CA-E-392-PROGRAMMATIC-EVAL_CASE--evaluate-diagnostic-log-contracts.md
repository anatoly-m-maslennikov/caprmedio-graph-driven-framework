---
atom_id: CA-E-392
ref_id: CA-E-392
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control
  dependencies:
  - MODEL//CAPRMEDIO <+ Package/Project Package
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Observability
    <+ Logging
tier: 5
relations:
  evaluation_for:
  - CA-M-414
  DERIVED_FROM:
  - CA-A-053
status: Active
version: 21
updated_at: 2026-11-10 20:47:54 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
destination:
  file:
    name: CA-E-392-PROGRAMMATIC-EVAL_CASE--evaluate-diagnostic-log-contracts.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Evaluate diagnostic log contracts

## Claim

### Prose Claim

Across normal, recoverable abnormal, failed and DEBUG diagnostics, require timestamp, level, component, operation, outcome and available action identity; enforce Logging Policy levels, redaction and separation from Journal meaning. Reject schema, level or redaction defects.
