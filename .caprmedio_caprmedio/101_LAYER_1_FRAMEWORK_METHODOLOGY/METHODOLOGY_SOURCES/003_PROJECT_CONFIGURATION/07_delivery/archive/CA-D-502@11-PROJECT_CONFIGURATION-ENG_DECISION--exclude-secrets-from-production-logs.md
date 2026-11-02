---
atom_id: CA-D-502@11
content_role: Delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Carrier
  depends_on: []
version: 11
updated_at: 2026-10-29 07:45:31 +0400
relations: {}
tier: 3
type: Decision
---
## Summary

Exclude secrets from production logs

## Claim scope

production logs that can contain credentials **or** secret-bearing payloads.

## Claim

production logs **must not** contain passwords, API keys, access tokens, session secrets, cookies, private keys, complete credentials, **or** unredacted secret-bearing payloads.

## Details

this is the explicit secret-exposure boundary for production log records.
