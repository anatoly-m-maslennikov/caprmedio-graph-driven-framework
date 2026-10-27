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
atom_id: CA-D-299
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Serialize Root Delivery Directory Names

## Scope

root Delivery Directory Carriers for non-Project Scope Units **when** the default Scope Unit directory convention is used.

## Claim

**every** root Delivery Directory Carrier **must** serialize the registered derived Scope Unit Path representation, Navigational Order Number, **and** Scope Unit Name **and** **must not** serialize Label **or** Local Order. no Structural Level field or token is required or authoritative. a declared native Carrier binding under CA-D-445 **must not** be reinterpreted through this default convention.

## Details
