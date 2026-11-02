---
subjects:
  governs: "Entity/Node/Continuant/Project.Settings.Project Name"
  depends_on:
    ["Entity/Node/Continuant/Project.Settings", "Entity/Node/Continuant/Project", "Project Name", "Entity/Node/Continuant/Actor/Type: Operator", "Entity/Node/Continuant/Atom", "Implementation"]
version: 15
updated_at: "2026-10-19 15:55:37 +0400"
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
  source_atom_revision: 15
  source_sha256: a6502f03216f8d15cc10365f2783a62133533414039ff672a7be871d506474a9
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
