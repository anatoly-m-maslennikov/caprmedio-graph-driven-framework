---
subjects:
  active: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Type
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - CAPRMEDIO_MODEL <+ Carrier
version: 23
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-1690
atom_id: CA-D-393
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Derive default external Type names

## Claim scope

external Type names derived from internal Types.

## Claim

**when** an external Type name is derived from an internal Type, the derivation uses `external_<internal_type_name>`. **when** the internal Type is the Content Role's default, the derived name uses that registered default Type. a separately registered explicit external Type name is non-default **and** does **not** modify this derivation rule.
