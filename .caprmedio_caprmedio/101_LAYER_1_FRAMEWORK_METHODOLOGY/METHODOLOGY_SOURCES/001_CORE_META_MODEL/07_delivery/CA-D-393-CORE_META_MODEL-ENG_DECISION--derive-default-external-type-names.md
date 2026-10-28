---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Type
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
  - Subject/CAPRMEDIO/Carrier
version: 19
updated_at: 2026-10-27 19:59:24 +0400
relations:
  child_of:
  - CA-R-1690
atom_id: CA-D-393
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Derive default external Type names

## Scope

external Type names derived from internal Types.

## Claim

**when** an external Type name is derived from an internal Type, the derivation uses `external_<internal_type_name>`. **when** the internal Type is the Content Role's default, the derived name uses that registered default Type. a separately registered explicit external Type name is non-default **and** does **not** modify this derivation rule.

## Details
