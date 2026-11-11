---
atom_id: CA-D-502
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier
version: 13
updated_at: 2026-11-02 19:44:26 +0400
relations: {}
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery/CA-D-502-PROJECT_CONFIGURATION-ENG_DECISION--exclude-secrets-from-production-logs.md
  source_atom_id: CA-D-502
  source_atom_revision: 13
  source_sha256: a18f0bafe5b541ce31fff2f3d0aaeaacc56c07aae9091c1c00dd6982899c780f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Exclude secrets from production logs

## Claim scope

production logs that can contain credentials **or** secret-bearing payloads.

## Claim

production logs **must not** contain passwords, API keys, access tokens, session secrets, cookies, private keys, complete credentials, **or** unredacted secret-bearing payloads.

## Details

this is the explicit secret-exposure boundary for production log records.
