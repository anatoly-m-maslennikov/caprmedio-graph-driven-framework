---
subjects:
  governs: Subject/Domain/Node.Type
  depends_on:
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - Subject/Engineering/Carrier
version: 14
updated_at: 2026-10-24 01:37:42 +0400
relations:
  child_of:
  - CA-R-1690
  - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
  - CAPRMEDIO-META-REQU-742--permit-one-internal-default-type-per-content-role
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
