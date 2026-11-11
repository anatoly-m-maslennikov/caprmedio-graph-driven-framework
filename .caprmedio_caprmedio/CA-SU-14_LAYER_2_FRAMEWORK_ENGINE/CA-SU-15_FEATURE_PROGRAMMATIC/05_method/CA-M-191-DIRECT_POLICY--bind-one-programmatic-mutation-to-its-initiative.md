---
identity:
  atom_id: CA-M-191
  ref_id: CA-M-191
context:
  container:
    scope_unit: CA-SU-15
  role: method
  form: direct_policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
      <+ Traceability
  tier: 4
relations:
  DERIVED_FROM:
  - CA-A-058
  method_for:
  - CA-R-1094
state:
  status: Active
  version: 26
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-191-DIRECT_POLICY--bind-one-programmatic-mutation-to-its-initiative.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---

## Summary

Bind one programmatic mutation to its Initiative

## Claim



### Prose Claim
##### Applicable when

apply **before** accepting **or** dispatching a programmatic mutation.

##### Procedure

1. resolve **or** create **=1** sealed Initiative from the accepted human
   instruction. it **may** bind **to** a persisted Plan **or** Task **or** remain an ephemeral
   session task.
2. assign one stable action identity **and** preserve a short instruction-derived
   summary plus enough structured context **to** identify the instruction.
3. attach the Initiative **and** action identities **before** **any** Hook, queue, worker,
   retry, Git, Journal, **or** reconciliation handoff.
4. propagate both identities unchanged through **every** handoff. a process,
   thread, adapter, queue, **or** worker identity **may** be linked as execution
   context but **must not** replace them.
5. return an explicit blocked outcome **before** mutation **when** either identity is
   missing, ambiguous, changed, **or** bound **to** more than one Initiative.

##### Failure or stop

stop **before** mutation **when** the Initiative is unsealed, the action identity is
absent **or** reused for another Initiative, **or** a handoff cannot preserve both
identities.

##### Sources

- [CA-A-058 — Validate PROGRAMMATIC Method and Evaluation closure](../02_analysis_and_advisory/CA-A-058-PROGRAMMATIC-ANALYSIS_RPRT--validate-programmatic-method-and-evaluation-closure.md)
