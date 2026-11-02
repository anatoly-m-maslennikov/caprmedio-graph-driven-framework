---
subjects:
  governs: Subject/Engineering/Carrier/Directory Carrier.Name
  depends_on:
  - 'Subject/Domain/Node/Continuant/Scope Unit/Type: Ordered'
  - 'Subject/Domain/Node/Continuant/Scope Unit/Type: Unordered'
  - Subject/Domain/Node/Continuant/Scope Unit.Label
  - Subject/Domain/Node/Continuant/Scope Unit.Local Order
version: 21
updated_at: 2026-10-24 00:51:05 +0400
relations: {}
atom_id: CA-D-298@21
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Serialize Local Order Only for Ordered Scope Unit Directories

## Scope

Scope Unit authority Directory Carrier Names that use the default Scope Unit directory convention.

## Claim

**when** the default Scope Unit directory convention is used, a Scope Unit authority Directory Carrier Name **must** serialize Local Order immediately **after** Label **only** for an Ordered Scope Unit **and** **must not** serialize Local Order for an Unordered Scope Unit. a declared native Carrier binding under CA-D-445-CORE_META_MODEL-GENERAL-DELIVERY--admit-explicit-scope-unit-carrier-bindings **must not** be reinterpreted through this default convention.

## Details
