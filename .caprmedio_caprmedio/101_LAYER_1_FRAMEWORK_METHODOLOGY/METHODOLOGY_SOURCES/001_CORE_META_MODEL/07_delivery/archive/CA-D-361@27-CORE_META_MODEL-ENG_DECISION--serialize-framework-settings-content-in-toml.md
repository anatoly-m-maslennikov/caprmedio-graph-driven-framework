---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  depends_on:
  - Entity/Aspect/Engineering/Data Handling/Serialization
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - Entity/Object/Continuant/Governing Objects/Governing Configuration
version: 27
updated_at: 2026-10-29 07:17:24 +0400
relations:
  child_of:
  - CA-D-359
atom_id: CA-D-361@27
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
