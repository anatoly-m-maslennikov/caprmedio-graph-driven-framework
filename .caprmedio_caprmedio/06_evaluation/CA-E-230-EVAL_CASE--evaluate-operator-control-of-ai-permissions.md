---
atom_id: CA-E-230
ref_id: CA-E-230
container:
  scope_unit: CA-SU-00
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent.Permissions
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Effect Authorization"
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  - CAPRMEDIO_MODEL <+ Carrier
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Dynamic Testing"
tier: 5
relations:
  child_of:
  - CA-R-846
  evaluation_for:
  - CA-R-846
status: Active
version: 27
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-E-230-CAPRMEDIO-EVAL_CASE--evaluate-operator-control-of-ai-permissions.md
    path: .caprmedio_caprmedio/06_evaluation
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: caprmedio
---
## Summary

Evaluate Operator control of AI permissions

## Claim

### Prose Claim


the Operator can create, inspect, limit, modify, suspend, **and** revoke AI Agent Delegations **and** mandatory authorization rules for identified AI Agents.

## Applicable conditions

apply **to** **every** supported delegation **or** mandatory-authorization-rule Carrier **and** **after** a material change **to** their governance **or** Implementation.

## Check

for one identified AI Agent, exercise creation, inspection, limitation, modification, suspension, **and** revocation on one test AI Agent Delegation **and** one test mandatory authorization rule through Operator-controlled paths. **after** **every** operation, inspect the effective state of the affected delegation **or** rule **and** verify that it matches the Operator action. check **every** applicable control operation for the test delegation **and** the test authorization rule; successful delegation control **must not** substitute for authorization-rule control.

## Acceptance

pass **only** **when** **every** required operation for delegations **and** mandatory authorization rules is available **to** the authorized Operator **and** produces the inspected effective state requested by that Operator.

## Failure

fail **and** report **every** unavailable operation, unauthorized state change, **or** mismatch between requested **and** effective delegation **or** authorization-rule state.
