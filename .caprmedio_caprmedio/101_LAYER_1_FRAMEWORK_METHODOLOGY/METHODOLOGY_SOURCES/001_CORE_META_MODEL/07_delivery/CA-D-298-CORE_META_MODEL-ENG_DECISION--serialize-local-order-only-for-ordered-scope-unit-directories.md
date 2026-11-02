---
subjects:
  active: Carrier/Directory.Name
  passive:
  - 'Entity/Object/Continuant/Structural Unit/Scope Unit/Type: Ordered'
  - 'Entity/Object/Continuant/Structural Unit/Scope Unit/Type: Unordered'
  - Scope Unit.Label
  - Scope Unit.Local Order
version: 30
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-298
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize Local Order Only for Ordered Scope Unit Directories

## Claim scope

Scope Unit authority Directory Carrier Names that use the default Scope Unit directory convention.

## Claim

**when** the default Scope Unit directory convention is used, a Scope Unit authority Directory Carrier Name **must** serialize Local Order immediately **after** Label **only** for an Ordered Scope Unit **and** **must not** serialize Local Order for an Unordered Scope Unit. a declared native Carrier binding under CA-D-445-CORE_META_MODEL-GENERAL-DELIVERY--admit-explicit-scope-unit-carrier-bindings **must not** be reinterpreted through this default convention.
