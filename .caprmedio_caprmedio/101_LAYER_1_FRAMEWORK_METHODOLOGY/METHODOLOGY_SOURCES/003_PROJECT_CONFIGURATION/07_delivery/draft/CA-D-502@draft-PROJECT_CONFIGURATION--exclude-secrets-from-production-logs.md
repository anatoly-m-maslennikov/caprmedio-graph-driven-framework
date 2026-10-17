---
atom_id: "CA-D-502@draft"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
global_tier: 11
status: "Draft"
author: "Anatoly Maslennikov"
subjects:
  governs: "Entity/Carrier"
  depends_on: []
version: 2
updated_at: "2026-10-17 23:29:02 +0000"
relations: {}
---
# Summary

Exclude secrets from production logs

## Scope

production logs that can contain credentials **or** secret-bearing payloads.

## Claim

production logs **must not** contain passwords, API keys, access tokens, session secrets, cookies, private keys, complete credentials, **or** unredacted secret-bearing payloads.

## Details

this is the explicit secret-exposure boundary for production log records.
