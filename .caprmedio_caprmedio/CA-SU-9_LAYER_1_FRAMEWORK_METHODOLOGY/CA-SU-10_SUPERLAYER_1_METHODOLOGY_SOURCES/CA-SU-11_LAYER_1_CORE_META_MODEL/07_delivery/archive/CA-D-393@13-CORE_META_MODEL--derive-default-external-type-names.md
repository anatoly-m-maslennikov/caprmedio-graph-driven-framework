---
subjects:
  governs: Subject/Domain/Node.Type
  depends_on:
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - Subject/Engineering/Carrier
version: 13
updated_at: 2026-10-24 01:18:03 +0400
relations:
  child_of:
  - CA-R-1690
  - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
  - CAPRMEDIO-META-REQU-742--permit-one-internal-default-type-per-content-role
atom_id: CA-D-393@13
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Derive default external Type names

## Scope

external Type names derived from internal Types.

## Claim

**when** an external Type name is derived from an internal Type, the derivation uses `external_<internal_type_name>`. **when** the internal Type is the Content Role's default, the derived name uses that registered default Type. a separately registered explicit external Type name is non-default **and** does **not** modify this derivation rule.

## Details
