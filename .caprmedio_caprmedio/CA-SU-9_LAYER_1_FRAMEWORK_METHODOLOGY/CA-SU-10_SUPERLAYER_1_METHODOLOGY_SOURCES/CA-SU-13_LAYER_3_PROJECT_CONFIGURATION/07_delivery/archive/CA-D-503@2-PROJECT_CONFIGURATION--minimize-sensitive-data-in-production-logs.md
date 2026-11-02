---
atom_id: CA-D-503@2
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
global_tier: 11
status: Archived
author: "Anatoly Maslennikov"
subjects:
  governs: "Entity/Carrier"
  depends_on: []
version: 2
updated_at: "2026-10-18 03:35:01 +0400"
relations: {}
---
# Summary

Minimize sensitive data in production logs

## Scope

production logs that can contain personal, customer, **or** commercially sensitive data.

## Claim

personal, customer, **and** commercially sensitive data in production logs **must** be omitted, masked, hashed, tokenized, **or** **otherwise** minimized according to the applicable boundary.

## Details

the applicable boundary selects the permitted minimization treatment for sensitive log data.
