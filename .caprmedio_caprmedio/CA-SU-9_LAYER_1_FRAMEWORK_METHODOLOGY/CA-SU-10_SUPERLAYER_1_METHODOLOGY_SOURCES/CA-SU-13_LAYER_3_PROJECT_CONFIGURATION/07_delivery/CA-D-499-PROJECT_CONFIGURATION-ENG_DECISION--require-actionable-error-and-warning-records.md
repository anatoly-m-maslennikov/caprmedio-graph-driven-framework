---
atom_id: CA-D-499
ref_id: CA-D-499
container:
  scope_unit: CA-SU-13
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier
tier: 3
status: Active
version: 13
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-D-499-PROJECT_CONFIGURATION-DECISION--require-actionable-error-and-warning-records.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
---
## Summary

Require actionable ERROR and WARNING records

## Claim

### Prose Claim


ERROR **and** WARNING production log records.


an `ERROR` **or** `WARNING` record **must** be actionable: it identifies the failed **or** degraded condition, affected scope, expected operator **or** automated response, **and** whether retry is safe.

## Details

the required context makes the response **and** retry disposition explicit for the failed **or** degraded condition.
