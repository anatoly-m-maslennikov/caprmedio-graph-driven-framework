---
atom_id: CA-E-262
ref_id: CA-E-262
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution
    Control <+ Effect Authorization
tier: 5
relations:
  evaluation_for:
  - CA-M-404
  - CA-M-409
  DERIVED_FROM:
  - CA-A-053
status: Active
version: 25
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
    name: CA-E-262-PROGRAMMATIC-EVAL_CASE--reject-file-mutation-with-unmet-precondition.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Reject file mutation with unmet precondition

## Claim



### Prose Claim
#### Claim checked

one PROGRAMMATIC file mutation stops **before** writing, replacing, **or** removing a
file **when** its declared target **or** precondition is invalid.

#### Applicable conditions

apply **when** a component writes, replaces, **or** removes a file.

#### Test case

request one file mutation with a declared precondition that does **not** hold.

#### Acceptance criteria

pass **only** **when** the operation returns the precondition failure **and** leaves the
target bytes unchanged.

#### Failure disposition

reject the mutation **and** preserve the existing target for diagnosis.

#### Sources

- [CA-M-409 — Bound file and subprocess effects](../05_method/CA-M-409-PROGRAMMATIC-ENG_POLICY--bound-file-and-subprocess-effects.md)
