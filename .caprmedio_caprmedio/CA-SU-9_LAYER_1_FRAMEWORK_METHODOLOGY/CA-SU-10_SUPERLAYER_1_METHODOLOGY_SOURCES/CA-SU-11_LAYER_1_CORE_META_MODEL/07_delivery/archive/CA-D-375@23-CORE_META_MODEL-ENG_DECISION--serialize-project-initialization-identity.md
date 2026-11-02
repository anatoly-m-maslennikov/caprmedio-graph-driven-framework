---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Project.Settings.Project Name
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Project.Settings.Project Name
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Engineering/Project Identity Binding
version: 23
updated_at: 2026-10-25 17:32:27 +0400
relations:
  child_of:
  - CA-D-366
atom_id: CA-D-375@23
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
