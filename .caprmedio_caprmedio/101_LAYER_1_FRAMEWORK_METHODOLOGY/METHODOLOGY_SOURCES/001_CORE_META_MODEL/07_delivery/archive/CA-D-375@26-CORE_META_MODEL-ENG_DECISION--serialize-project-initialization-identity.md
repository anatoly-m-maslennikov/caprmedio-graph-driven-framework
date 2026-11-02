---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings.Project Name
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings.Project Name
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Governing Objects/Atom
version: 26
updated_at: 2026-10-29 07:17:25 +0400
relations:
  child_of:
  - CA-D-366
atom_id: CA-D-375@26
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 7
type: Eng Decision
---
# Summary

Serialize Project initialization identity

## Scope

the Operator-selected Project Name in the Project Settings TOML Carrier.

## Claim

the Project Settings TOML Carrier **must** encode the Operator-selected Project Name as its exact nonempty lowercase TOML string value **in** `project.name`, **before** the first Project Atom **or** Implementation is created.

## Details

validation **must** preserve the selected value exactly; it **must not** trim **or** convert its case. the complete supported field signature is governed by CA-D-366.
