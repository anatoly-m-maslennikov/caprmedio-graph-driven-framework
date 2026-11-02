---
subjects:
  governs: Entity/Carrier/Directory.Name
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Name
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Label
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Path
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Local Order
version: 30
updated_at: 2026-10-31 19:26:58 +0400
relations: {}
atom_id: CA-D-297@30-draft
content_role: Delivery
form: Decision
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
tier: 3
---
## Summary

Serialize Scope Unit Authority Directory Names

## Claim scope

Project-internal Scope Unit authority Directory Carrier Names that use the default Scope Unit directory convention.

## Claim

When the default Scope Unit directory convention is used, every Project-internal Scope Unit authority Directory Carrier Name must serialize the registered derived Scope Unit Path representation, Label, applicable Local Order, and Scope Unit Name in that order. No Structural Level field or token is required or authoritative. A declared native Carrier binding under CA-D-445-CORE_META_MODEL-ENG_DECISION--admit-explicit-scope-unit-carrier-bindings must not be reinterpreted through this default convention.

This Draft does not rename existing paths or establish a new directory layout. It does not affect Step or P (Plan) Atom numbering.
