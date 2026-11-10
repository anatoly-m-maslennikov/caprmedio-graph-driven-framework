---
atom_id: CA-E-395
ref_id: CA-E-395
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
    <+ Verification <+ Dynamic Testing
  dependencies:
  - MODEL//CAPRMEDIO <+ Package/Project Package
tier: 5
relations:
  evaluation_for:
  - CA-M-424
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
    name: CA-E-395-PROGRAMMATIC-EVAL_CASE--fuzz-parsers-and-stateful-boundaries.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Fuzz parsers and stateful boundaries

## Claim

### Prose Claim

A bounded property/state-machine campaign over valid, invalid and ordered cases preserves seed and minimal failing input/sequence. Explicitly accept or reject each defect; accepted defects gain deterministic regression. Reject unreplayable evidence and keep campaigns out of synchronous Hooks.
