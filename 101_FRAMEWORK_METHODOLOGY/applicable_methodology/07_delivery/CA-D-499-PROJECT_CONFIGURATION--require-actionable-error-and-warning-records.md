---
atom_id: "CA-D-499"
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
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-499-PROJECT_CONFIGURATION--require-actionable-error-and-warning-records.md
  source_atom_id: CA-D-499
  source_atom_revision: 2
  source_sha256: ce427f16fc8ce46e5026774279f7fd89f25c905e239818549aab155f9844ee67
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Require actionable ERROR and WARNING records

## Scope

ERROR **and** WARNING production log records.

## Claim

an `ERROR` **or** `WARNING` record **must** be actionable: it identifies the failed **or** degraded condition, affected scope, expected operator **or** automated response, **and** whether retry is safe.

## Details

the required context makes the response **and** retry disposition explicit for the failed **or** degraded condition.
