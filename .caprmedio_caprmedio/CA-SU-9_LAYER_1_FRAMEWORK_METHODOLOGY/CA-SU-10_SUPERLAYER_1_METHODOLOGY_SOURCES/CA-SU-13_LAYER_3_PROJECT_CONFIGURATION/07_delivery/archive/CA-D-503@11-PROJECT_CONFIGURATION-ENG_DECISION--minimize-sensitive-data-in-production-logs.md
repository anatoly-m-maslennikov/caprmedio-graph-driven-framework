---
atom_id: CA-D-503@11
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

Minimize sensitive data in production logs

## Claim scope

production logs that can contain personal, customer, **or** commercially sensitive data.

## Claim

personal, customer, **and** commercially sensitive data in production logs **must** be omitted, masked, hashed, tokenized, **or** **otherwise** minimized according to the applicable boundary.

## Details

the applicable boundary selects the permitted minimization treatment for sensitive log data.
