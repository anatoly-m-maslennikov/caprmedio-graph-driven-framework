---
subjects:
  governs: Subject/Graph Node/Engineering/Execution Control
  depends_on: []
version: 21
updated_at: 2026-10-27 06:04:45 +0400
relations:
  method_for:
  - CA-R-1094
  derived_from:
  - CA-A-058
atom_id: CA-M-191
content_role: Method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Active
author: Anatoly Maslennikov
type: Eng Policy
tier: 4
---
# Summary

Bind one programmatic mutation to its Initiative

## Scope

## Claim

## Details

### Applicable when

apply **before** accepting **or** dispatching a programmatic mutation governed by
CA-R-1094.

### Procedure

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

### Outcome

**every** accepted mutation remains attributable **to** one human-origin Initiative
**and** one stable action across asynchronous execution **and** provenance systems.

### Failure or stop

stop **before** mutation **when** the Initiative is unsealed, the action identity is
absent **or** reused for another Initiative, **or** a handoff cannot preserve both
identities.

### Sources

- [CA-A-058 — Validate PROGRAMMATIC Method and Evaluation closure](../02_analysis/CA-A-058-PROGRAMMATIC-ANALYSIS_RPRT--validate-programmatic-method-and-evaluation-closure.md)
