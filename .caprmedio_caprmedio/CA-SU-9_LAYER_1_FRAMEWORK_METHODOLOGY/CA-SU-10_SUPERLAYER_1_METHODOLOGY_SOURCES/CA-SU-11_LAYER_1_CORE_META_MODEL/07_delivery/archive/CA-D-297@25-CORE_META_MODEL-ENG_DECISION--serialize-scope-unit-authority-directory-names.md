---
subjects:
  governs: Subject/Graph Node/Carrier/Directory.Name
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Name
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Label
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Path
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Navigational Order Number
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Local Order
version: 25
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-D-297@25
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Serialize Scope Unit Authority Directory Names

## Scope

Project-internal Scope Unit authority Directory Carrier Names that use the default Scope Unit directory convention.

## Claim

**when** the default Scope Unit directory convention is used, **every** Project-internal Scope Unit authority Directory Carrier Name **must** serialize the registered derived Scope Unit Path representation, Navigational Order Number, Label, applicable Local Order, **and** Scope Unit Name **in** that order. no Structural Level field or token is required or authoritative. a declared native Carrier binding under CA-D-445-CORE_META_MODEL-GENERAL-DELIVERY--admit-explicit-scope-unit-carrier-bindings **must not** be reinterpreted through this default convention.

## Details
