---
atom_id: CA-E-370
ref_id: CA-E-370
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
    name: CA-E-370-PROGRAMMATIC-EVAL_CASE--verify-logging-lifecycle-materialization.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Verify logging lifecycle materialization

## Claim

### Prose Claim

Reject deployment until a production-relevant component materializes active Logging Policy sink, retention, access, sampling, rotation, size, back-pressure, unavailable-sink and disk-pressure boundaries; implementation/delivery do not claim policy authority. For the selected Docker runtime, verify structured technical diagnostics go to stderr, local rotation uses `max-size=10m` and `max-file=3`, and non-blocking mode uses `max-buffer-size=1m`; when the buffer is full, new technical messages may be dropped without stalling primary work.
