---
atom_id: "CA-D-503"
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
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-503-PROJECT_CONFIGURATION--minimize-sensitive-data-in-production-logs.md
  source_atom_id: CA-D-503
  source_atom_revision: 2
  source_sha256: c98c27b8eea76ae3177356ad6730689525a321f1b9601231a124cb2876aae334
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Minimize sensitive data in production logs

## Scope

production logs that can contain personal, customer, **or** commercially sensitive data.

## Claim

personal, customer, **and** commercially sensitive data in production logs **must** be omitted, masked, hashed, tokenized, **or** **otherwise** minimized according to the applicable boundary.

## Details

the applicable boundary selects the permitted minimization treatment for sensitive log data.
