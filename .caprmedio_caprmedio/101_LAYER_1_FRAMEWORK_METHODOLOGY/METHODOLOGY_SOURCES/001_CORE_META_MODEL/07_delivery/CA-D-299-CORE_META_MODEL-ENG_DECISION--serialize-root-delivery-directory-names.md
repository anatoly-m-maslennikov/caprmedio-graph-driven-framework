---
subjects:
  governs: Subject/CAPRMEDIO/Carrier/Directory.Name
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Name
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Label
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Path
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Navigational Order Number
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Local Order
version: 26
updated_at: 2026-10-27 19:59:23 +0400
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
