---
version: 25
updated_at: 2026-10-29 10:13:48 +0400
relations:
  child_of:
  - CA-R-004
  evaluation_for:
  - CA-R-004
subjects:
  governs: 'Entity/Aspect/Product: CAPRMEDIO Framework'
  depends_on:
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-228@25
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Eval Policy
tier: 5
---
## Summary

Evaluate Operator control over the CAPRMEDIO instance

## Claim

the declared Operators collectively retain control over **every** governed part of the CAPRMEDIO instance **and** can use the instance **to** change the Project within their current authority.

## Applicable conditions

apply **after** a material change **to** the CAPRMEDIO instance, its authority, **or** the mechanisms through which Operators change the Project.

## Check

enumerate **every** governed part of the current CAPRMEDIO instance **and** **every** Operator-authorized Project-change operation exposed through it. for **every** part, demonstrate that the declared Operators can collectively inspect **and** direct it under their current authority. for **every** operation, demonstrate that **`>=1`** admissible Operator-controlled path can apply the change **to** the Project.

## Acceptance

pass **only** **when** **every** governed instance part is collectively inspectable **and** directable by the declared Operators **and** **every** admitted Project-change operation has an admissible Operator-controlled execution path.

## Failure

fail **and** report **every** uncontrolled instance part **or** unavailable Operator-controlled Project-change path.
