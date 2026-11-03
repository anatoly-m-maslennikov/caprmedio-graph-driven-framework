---
version: 28
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-R-827
  evaluation_for:
  - CA-R-827
subjects:
  active: CAPRMEDIO_MODEL <+ Project
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Product
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Evaluation)
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-229
status: Active
current_scope_unit: caprmedio
tier: 5
role: Evaluation
form: Eval Policy
---
## Summary

Evaluate Operator control outside the framework instance

## Claim

the Operator controls **every** governed Project part outside the CAPRMEDIO Framework Instance, **and** **every** material change **to** those parts is observable, steerable, interruptible, **and** recoverable under the Operator's current authority.

## Applicable conditions

apply **to** **every** admitted material change class affecting those outside-instance Project parts **and** **after** a material change **to** their authority **or** control mechanisms.

## Check

enumerate **every** governed Project part outside the CAPRMEDIO Framework Instance **and** **every** admitted material change class affecting those parts. for **every** part, demonstrate Operator inspection **and** direction. for **every** change class, demonstrate an Operator-visible state, an admissible steering action, an interruption boundary, **and** a recovery path. evaluate control of the CAPRMEDIO Framework Instance under CA-E-228 rather than including instance-only failures **in** this Evaluation.

## Acceptance

pass **only** **when** **every** governed outside-instance Project part is inspectable **and** directable by the Operator **and** **every** admitted material change class affecting those parts has demonstrated observability, steerability, interruptibility, **and** recoverability under current Operator authority.

## Failure

fail **and** report **every** uncontrolled outside-instance Project part **or** change class missing **any** required control property.
