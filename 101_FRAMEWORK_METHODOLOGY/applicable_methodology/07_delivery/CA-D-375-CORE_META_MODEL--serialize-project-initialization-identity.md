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
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-375-CORE_META_MODEL--serialize-project-initialization-identity.md
  source_atom_id: CA-D-375
  source_atom_revision: 14
  source_sha256: c98f2cda50dd3a8d3812d890454df8a9194f13d77f7d2504772e1aa154d273b6
  original_relations_sha256: 60d285f0b5eadc5cfe0417918004395017eb1104d02fc3179cd56cf1f1493577
---
# Summary

Serialize Project initialization identity

## Scope

the Operator-selected Project Name in the Project Settings TOML Carrier.

## Claim

the Project Settings TOML Carrier **must** encode the Operator-selected Project Name as its exact nonempty lowercase TOML string value **in** `project.name`, **before** the first Project Atom **or** Implementation is created.

## Details

validation **must** preserve the selected value exactly; it **must not** trim **or** convert its case. the complete supported field signature is governed by CA-D-366.
