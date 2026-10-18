---
subjects:
  governs: "Entity/Continuant/Object/Project.Settings.Project Name"
  depends_on:
    ["Entity/Continuant/Object/Project.Settings", "Entity/Continuant/Object/Project", "Project Name", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/Object/Atom", "Implementation"]
version: 14
updated_at: "2026-10-18 07:39:42 +0400"
relations:
  child_of:
    - "CA-D-366"
atom_id: "CA-D-375"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize Project initialization identity

## Scope

the Operator-selected Project Name in the Project Settings TOML Carrier.

## Claim

the Project Settings TOML Carrier **must** encode the Operator-selected Project Name as its exact nonempty lowercase TOML string value **in** `project.name`, **before** the first Project Atom **or** Implementation is created.

## Details

validation **must** preserve the selected value exactly; it **must not** trim **or** convert its case. the complete supported field signature is governed by CA-D-366.
