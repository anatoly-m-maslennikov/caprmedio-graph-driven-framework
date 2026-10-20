---
subjects:
  governs: "Entity/Relation/Type: NARROWER_THAN"
  depends_on:
    ["Entity/Node/Continuant/Projection/Type: Terms Graph", "Entity/Node/Continuant/Term"]
version: 19
updated_at: "2026-10-19 15:52:40 +0400"
relations: {}
atom_id: "CA-R-1244"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Allow multiple direct Term hierarchy parents

## Scope

Direct NARROWER_THAN parents of a Term.

## Claim

a Term **may** have **`>=0`** direct NARROWER_THAN parents.

## Details
