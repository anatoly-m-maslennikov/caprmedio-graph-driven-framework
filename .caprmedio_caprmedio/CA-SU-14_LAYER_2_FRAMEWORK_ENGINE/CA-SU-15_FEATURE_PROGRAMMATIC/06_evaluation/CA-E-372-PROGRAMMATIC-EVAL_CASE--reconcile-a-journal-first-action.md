---
atom_id: CA-E-372
ref_id: CA-E-372
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
    name: CA-E-372-PROGRAMMATIC-EVAL_CASE--reconcile-a-journal-first-action.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Reconcile a Journal-first action

## Claim

### Prose Claim

A Journal-first action remains `journal_recorded_git_pending` after exactly one canonical record binds one reachable real-change commit SHA until a later separate Git commit versions the Journal carrier containing that record. Verify pending before that carrier commit and `reconciled` after it; otherwise preserve pending and prohibit provenance reliance. The record does not embed the SHA of the commit containing itself.
