---
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Carrier/Directory Carrier.Name
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Scope Unit/Type: Ordered'
  - 'Subject/Graph Node/Domain/Continuant/Scope Unit/Type: Unordered'
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Label
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Local Order
version: 24
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-D-298@24
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Serialize Local Order Only for Ordered Scope Unit Directories

## Scope

Scope Unit authority Directory Carrier Names that use the default Scope Unit directory convention.

## Claim

**when** the default Scope Unit directory convention is used, a Scope Unit authority Directory Carrier Name **must** serialize Local Order immediately **after** Label **only** for an Ordered Scope Unit **and** **must not** serialize Local Order for an Unordered Scope Unit. a declared native Carrier binding under CA-D-445-CORE_META_MODEL-GENERAL-DELIVERY--admit-explicit-scope-unit-carrier-bindings **must not** be reinterpreted through this default convention.

## Details
