---
atom_id: CA-D-502
ref_id: CA-D-502
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
    name: CA-D-502-PROJECT_CONFIGURATION-DECISION--exclude-secrets-from-production-logs.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery/CA-D-502-PROJECT_CONFIGURATION-ENG_DECISION--exclude-secrets-from-production-logs.md
  source_atom_id: CA-D-502
  source_atom_revision: 13
  source_sha256: d30efd04303fd4b2580ae486b8f571e3576530051b39ec416e6e86bae32d7d7a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Exclude secrets from production logs

## Claim

### Prose Claim


production logs that can contain credentials **or** secret-bearing payloads.


production logs **must not** contain passwords, API keys, access tokens, session secrets, cookies, private keys, complete credentials, **or** unredacted secret-bearing payloads.

## Details

this is the explicit secret-exposure boundary for production log records.
