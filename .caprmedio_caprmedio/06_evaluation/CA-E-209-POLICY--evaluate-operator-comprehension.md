---
atom_id: CA-E-209
ref_id: CA-E-209
container:
  scope_unit: CA-SU-00
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Project
tier: 2
relations:
  child_of:
  - CA-M-263
  evaluation_for:
  - CA-M-263
status: Active
version: 25
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-E-209-CAPRMEDIO-EVAL_POLICY--evaluate-operator-comprehension.md
    path: .caprmedio_caprmedio/06_evaluation
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: caprmedio
---
## Summary

Evaluate operator comprehension

## Claim

### Prose Claim


the intended Operator can identify the represented meaning, available controls, **and** material consequences.

## Applicable conditions

apply **when** governed meaning is exposed **to** a Project Operator.

## Acceptance

pass **only** **when** the intended Operator can identify the represented meaning, the controls available **to** them, **and** the material consequences of using those controls.

## Failure

treat the representation as failed for that Operator **and** report **every** unidentified meaning, control, **or** material consequence.
