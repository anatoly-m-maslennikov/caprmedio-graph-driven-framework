---
atom_id: CA-E-228
ref_id: CA-E-228
container:
  scope_unit: CA-SU-00
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Product
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Project
tier: 5
relations:
  child_of:
  - CA-R-004
  evaluation_for:
  - CA-R-004
status: Active
version: 28
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-E-228-CAPRMEDIO-EVAL_POLICY--evaluate-operator-control-over-the-caprmedio-instance.md
    path: .caprmedio_caprmedio/06_evaluation
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: caprmedio
---
## Summary

Evaluate Operator control over the CAPRMEDIO instance

## Claim

### Prose Claim


the declared Operators collectively retain control over **every** governed part of the CAPRMEDIO instance **and** can use the instance **to** change the Project within their current authority.

## Applicable conditions

apply **after** a material change **to** the CAPRMEDIO instance, its authority, **or** the mechanisms through which Operators change the Project.

## Check

enumerate **every** governed part of the current CAPRMEDIO instance **and** **every** Operator-authorized Project-change operation exposed through it. for **every** part, demonstrate that the declared Operators can collectively inspect **and** direct it under their current authority. for **every** operation, demonstrate that **`>=1`** admissible Operator-controlled path can apply the change **to** the Project.

## Acceptance

pass **only** **when** **every** governed instance part is collectively inspectable **and** directable by the declared Operators **and** **every** admitted Project-change operation has an admissible Operator-controlled execution path.

## Failure

fail **and** report **every** uncontrolled instance part **or** unavailable Operator-controlled Project-change path.
