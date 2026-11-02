---
subjects:
  governs: Entity/Carrier/Directory.Name
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Name
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Label
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Path
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Navigational Order Number
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Local Order
version: 29
updated_at: 2026-10-29 10:13:50 +0400
relations: {}
atom_id: CA-D-299@29
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Decision
---
## Summary

Serialize Root Delivery Directory Names

## Claim scope

root Delivery Directory Carriers for non-Project Scope Units **when** the default Scope Unit directory convention is used.

## Claim

**every** root Delivery Directory Carrier **must** serialize the registered derived Scope Unit Path representation, Navigational Order Number, **and** Scope Unit Name **and** **must not** serialize Label **or** Local Order. no Structural Level field or token is required or authoritative. a declared native Carrier binding under CA-D-445 **must not** be reinterpreted through this default convention.
