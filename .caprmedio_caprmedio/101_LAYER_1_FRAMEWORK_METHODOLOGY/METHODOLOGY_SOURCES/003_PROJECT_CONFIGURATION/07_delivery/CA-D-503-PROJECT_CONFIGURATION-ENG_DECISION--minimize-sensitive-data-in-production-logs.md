---
atom_id: CA-D-503
content_role: Delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Carrier
  depends_on: []
version: 9
updated_at: 2026-10-27 19:59:26 +0400
relations: {}
tier: 3
type: Eng Decision
---
# Summary

Minimize sensitive data in production logs

## Scope

production logs that can contain personal, customer, **or** commercially sensitive data.

## Claim

personal, customer, **and** commercially sensitive data in production logs **must** be omitted, masked, hashed, tokenized, **or** **otherwise** minimized according to the applicable boundary.

## Details

the applicable boundary selects the permitted minimization treatment for sensitive log data.
