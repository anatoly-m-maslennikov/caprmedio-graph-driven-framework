---
atom_id: CA-D-502@7
content_role: Delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Carrier
  depends_on: []
version: 7
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
tier: 3
type: Eng Decision
---
# Summary

Exclude secrets from production logs

## Scope

production logs that can contain credentials **or** secret-bearing payloads.

## Claim

production logs **must not** contain passwords, API keys, access tokens, session secrets, cookies, private keys, complete credentials, **or** unredacted secret-bearing payloads.

## Details

this is the explicit secret-exposure boundary for production log records.
