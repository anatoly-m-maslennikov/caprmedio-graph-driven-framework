---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Serialization
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Governing Configuration
version: 26
updated_at: 2026-10-27 19:59:23 +0400
relations:
  child_of:
  - CA-D-359
atom_id: CA-D-361
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
type: Eng Decision
tier: 5
---
# Summary

Serialize Framework Settings Content in TOML

## Scope

the Framework Instance Settings TOML Carrier.

## Claim

the Framework Instance Settings TOML Carrier **must** encode explicit Operator-selected instance choices through sections **and** fields specified by concrete settings-specification Atoms under its foundational content **and** authority boundaries **and** applicable shared settings specifications; it **must not** store Project initialization inputs **or** authoritative Project Structure declarations **or** derived structural values as independently editable settings.

## Details
