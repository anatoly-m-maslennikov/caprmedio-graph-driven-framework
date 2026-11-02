---
subjects:
  active: Carrier/Directory.Name
  passive:
  - Scope Unit.Name
  - Scope Unit.Label
  - Scope Unit.Path
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Navigational Order Number
  - Scope Unit.Local Order
version: 30
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-299@30
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize Root Delivery Directory Names

## Claim scope

root Delivery Directory Carriers for non-Project Scope Units **when** the default Scope Unit directory convention is used.

## Claim

**every** root Delivery Directory Carrier **must** serialize the registered derived Scope Unit Path representation, Navigational Order Number, **and** Scope Unit Name **and** **must not** serialize Label **or** Local Order. no Structural Level field or token is required or authoritative. a declared native Carrier binding under CA-D-445 **must not** be reinterpreted through this default convention.
