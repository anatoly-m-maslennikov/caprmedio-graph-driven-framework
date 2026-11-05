---
atom_id: CA-D-502
ref_id: CA-D-502
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier
version: 13
updated_at: 2026-11-02 19:44:26 +0400
tier: 3
role: Delivery
form: Decision
container:
  scope_unit: CA-SU-13
carrier_destination:
  file:
    name: CA-D-502-PROJECT_CONFIGURATION-DECISION--exclude-secrets-from-production-logs.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery
---
## Summary

Exclude secrets from production logs

## Claim

### Prose Claim


production logs that can contain credentials **or** secret-bearing payloads.


production logs **must not** contain passwords, API keys, access tokens, session secrets, cookies, private keys, complete credentials, **or** unredacted secret-bearing payloads.

## Details

this is the explicit secret-exposure boundary for production log records.
