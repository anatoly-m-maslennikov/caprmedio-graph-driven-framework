---
subjects:
  governs: "Structural Entity Containment Relations"
  depends_on:
    ["Containment Relation Pair", "Directory Carrier Nesting"]
version: 14
updated_at: "2026-10-15 12:17:53 +0000"
relations: {}
atom_id: "CA-D-266"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Prohibit Persisting Derived Containment

## Scope

`CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting.

## Claim

`CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting **must not** be persisted as independent relation declarations.

## Details
