---
subjects:
  governs: "Entity/Carrier/Directory Carrier.Name"
  depends_on:
    ["Entity/Continuant/Node/Scope Unit/Type: Ordered", "Entity/Continuant/Node/Scope Unit/Type: Unordered", "Entity/Continuant/Node/Scope Unit.Label", "Entity/Continuant/Node/Scope Unit.Local Order"]
version: 16
updated_at: "2026-10-18 07:12:35 +0400"
relations: {}
atom_id: "CA-D-298"
content_role: "Delivery"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize Local Order Only for Ordered Scope Unit Directories

## Scope

Scope Unit authority Directory Carrier Names that use the default Scope Unit directory convention.

## Claim

**when** the default Scope Unit directory convention is used, a Scope Unit authority Directory Carrier Name **must** serialize Local Order immediately **after** Label **only** for an Ordered Scope Unit **and** **must not** serialize Local Order for an Unordered Scope Unit. a declared native Carrier binding under CA-D-445-CORE_META_MODEL-GENERAL-DELIVERY--admit-explicit-scope-unit-carrier-bindings **must not** be reinterpreted through this default convention.

## Details
