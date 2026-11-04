---
atom_id: CA-D-499
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier
version: 13
updated_at: 2026-11-02 19:44:26 +0400
relations: {}
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery/CA-D-499-PROJECT_CONFIGURATION-ENG_DECISION--require-actionable-error-and-warning-records.md
  source_atom_id: CA-D-499
  source_atom_revision: 13
  source_sha256: a6b6406f2d42ff53720a45103f417961805c62c731621bb3cb608df0d4e7391e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Require actionable ERROR and WARNING records

## Claim

### Prose Claim


ERROR **and** WARNING production log records.


an `ERROR` **or** `WARNING` record **must** be actionable: it identifies the failed **or** degraded condition, affected scope, expected operator **or** automated response, **and** whether retry is safe.

## Details

the required context makes the response **and** retry disposition explicit for the failed **or** degraded condition.
