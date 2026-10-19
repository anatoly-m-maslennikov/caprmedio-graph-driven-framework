---
atom_id: "CA-D-502"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
subjects:
  governs: "Entity/Carrier"
  depends_on: []
version: 2
updated_at: "2026-10-18 03:35:01 +0400"
relations: {}
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-502-PROJECT_CONFIGURATION--exclude-secrets-from-production-logs.md
  source_atom_id: CA-D-502
  source_atom_revision: 2
  source_sha256: d5278784a4844f5f8db2c787c8501486477f7a6325cb8969748a319efa26214d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Exclude secrets from production logs

## Scope

production logs that can contain credentials **or** secret-bearing payloads.

## Claim

production logs **must not** contain passwords, API keys, access tokens, session secrets, cookies, private keys, complete credentials, **or** unredacted secret-bearing payloads.

## Details

this is the explicit secret-exposure boundary for production log records.
