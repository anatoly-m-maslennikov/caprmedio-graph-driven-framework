---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings.Name
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Governing Objects/Atom
version: 28
updated_at: 2026-10-30 17:21:56 +0400
relations:
  child_of:
  - CA-D-366
atom_id: CA-D-375@28
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 7
type: Decision
---
## Summary

Serialize Project initialization identity

## Claim scope

the Operator-selected Project Name in the Project Settings TOML Carrier.

## Claim

the Project Settings TOML Carrier **must** encode the Operator-selected Project Name as its exact nonempty lowercase TOML string value **in** `project.name`, **before** the first Project Atom **or** Implementation is created.

## Details

validation **must** preserve the selected value exactly; it **must not** trim **or** convert its case. the complete supported field signature is governed by CA-D-366.

### Current source provenance

Current source: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/CA-D-375-CORE_META_MODEL-ENG_DECISION--serialize-project-initialization-identity.md`, CA-D-375@27, SHA-256 `d86d451d292b2af19c799152c03940cf96f3693edad8f90fbca028d47f55303f`.
