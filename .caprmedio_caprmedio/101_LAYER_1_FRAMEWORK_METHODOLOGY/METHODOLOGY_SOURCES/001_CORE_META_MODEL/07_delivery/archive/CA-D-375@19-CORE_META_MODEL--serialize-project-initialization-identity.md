---
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Settings.Project Name
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Settings
  - Subject/Domain/Node/Continuant/Project
  - Subject/Domain/Node/Continuant/Project.Settings.Project Name
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Engineering/Project Identity Binding
version: 19
updated_at: 2026-10-24 00:51:05 +0400
relations:
  child_of:
  - CA-D-366
atom_id: CA-D-375@19
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Serialize Project initialization identity

## Scope

the Operator-selected Project Name in the Project Settings TOML Carrier.

## Claim

the Project Settings TOML Carrier **must** encode the Operator-selected Project Name as its exact nonempty lowercase TOML string value **in** `project.name`, **before** the first Project Atom **or** Implementation is created.

## Details

validation **must** preserve the selected value exactly; it **must not** trim **or** convert its case. the complete supported field signature is governed by CA-D-366.
