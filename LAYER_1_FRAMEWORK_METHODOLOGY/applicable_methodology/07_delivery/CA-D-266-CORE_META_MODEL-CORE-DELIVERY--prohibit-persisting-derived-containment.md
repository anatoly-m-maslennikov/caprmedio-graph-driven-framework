---
subjects:
  governs: "Structural Entity Containment Relations"
  depends_on:
    ["Containment Relation Pair", "Directory Carrier Nesting"]
version: 15
updated_at: "2026-10-20 00:10:59 +0400"
relations: {}
atom_id: "CA-D-266"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-266-CORE_META_MODEL-CORE-DELIVERY--prohibit-persisting-derived-containment.md
  source_atom_id: CA-D-266
  source_atom_revision: 15
  source_sha256: b213870566432b1c96ad8d7e65ab9f03b8516fdaff3f1a2fbc99d158ad9fb662
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Prohibit Persisting Derived Containment

## Scope

`CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting.

## Claim

`CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting **must not** be persisted as independent relation declarations.

## Details

This prohibition applies when canonical Carrier nesting already owns the containment fact. It does not ban an independently authored direct IS_CONTAINED_BY fact whose authority is the child's admitted relation declaration rather than nesting. Do not maintain both as independent sources for the same fact. CONTAINS remains a derived inverse in either representation and is not independently authored.
