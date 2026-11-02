---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Type
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - Entity/Carrier
version: 21
updated_at: 2026-10-29 07:45:30 +0400
relations:
  child_of:
  - CA-R-1690
atom_id: CA-D-393@21
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Decision
---
## Summary

Derive default external Type names

## Claim scope

external Type names derived from internal Types.

## Claim

**when** an external Type name is derived from an internal Type, the derivation uses `external_<internal_type_name>`. **when** the internal Type is the Content Role's default, the derived name uses that registered default Type. a separately registered explicit external Type name is non-default **and** does **not** modify this derivation rule.

## Details
