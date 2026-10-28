---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings.Project Name
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings.Project Name
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
version: 25
updated_at: 2026-10-27 19:59:24 +0400
relations:
  child_of:
  - CA-D-366
atom_id: CA-D-375
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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
