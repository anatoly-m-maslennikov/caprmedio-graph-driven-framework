---
atom_id: CA-E-264
ref_id: CA-E-264@24
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
tier: 5
relations:
  evaluation_for:
  - CA-M-409
  derived_from:
  - CA-A-053
status: Archived
version: 24
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
carrier_destination:
  file:
    name: CA-E-264@24-PROGRAMMATIC-EVAL_CASE--surface-one-nonzero-subprocess-result.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/archive
---
## Summary

Surface one nonzero subprocess result

## Claim

### Prose Claim

#### Claim checked

one PROGRAMMATIC subprocess boundary observes **and** returns a non-zero exit
status with the context required for diagnosis **or** recovery.

#### Applicable conditions

apply **only** **when** a component invokes a subprocess. components **without** a
subprocess boundary are **not** applicable.

#### Test case

invoke one declared subprocess that returns a non-zero exit status.

#### Acceptance criteria

pass **only** **when** the boundary reports the explicit status **and** declared input
context **without** treating the invocation as successful.

#### Failure disposition

stop the affected operation **and** return the failure **to** its caller **or** recovery
owner.

#### Sources

- [CA-M-409 — Bound file and subprocess effects](../05_method/CA-M-409-PROGRAMMATIC-ENG_POLICY--bound-file-and-subprocess-effects.md)
