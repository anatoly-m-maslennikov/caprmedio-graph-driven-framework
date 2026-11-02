---
subjects:
  governs: Entity/Carrier/Directory.Name
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Name
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Label
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Path
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Navigational Order Number
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Local Order
version: 28
updated_at: 2026-10-29 07:45:30 +0400
relations: {}
atom_id: CA-D-297@28
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Decision
---
## Summary

Serialize Scope Unit Authority Directory Names

## Claim scope

Project-internal Scope Unit authority Directory Carrier Names that use the default Scope Unit directory convention.

## Claim

**when** the default Scope Unit directory convention is used, **every** Project-internal Scope Unit authority Directory Carrier Name **must** serialize the registered derived Scope Unit Path representation, Navigational Order Number, Label, applicable Local Order, **and** Scope Unit Name **in** that order. no Structural Level field or token is required or authoritative. a declared native Carrier binding under CA-D-445-CORE_META_MODEL-GENERAL-DELIVERY--admit-explicit-scope-unit-carrier-bindings **must not** be reinterpreted through this default convention.

## Details
