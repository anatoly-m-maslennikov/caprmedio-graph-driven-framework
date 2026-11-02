---
atom_id: CA-D-502
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: Carrier
version: 13
updated_at: 2026-11-02 19:44:26 +0400
relations: {}
tier: 3
role: Delivery
form: Decision
---
## Summary

Exclude secrets from production logs

## Claim scope

production logs that can contain credentials **or** secret-bearing payloads.

## Claim

production logs **must not** contain passwords, API keys, access tokens, session secrets, cookies, private keys, complete credentials, **or** unredacted secret-bearing payloads.

## Details

this is the explicit secret-exposure boundary for production log records.
