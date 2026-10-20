---
subjects:
  governs: "Entity/Node/Continuant/Project.Settings.Atom Prefix"
  depends_on:
    ["Entity/Node/Continuant/Project.Settings", "Entity/Node/Continuant/Atom", "Entity/Node/Continuant/Actor/Type: Operator"]
version: 15
updated_at: "2026-10-19 15:55:38 +0400"
relations:
  child_of:
    - "CA-D-366"
atom_id: "CA-D-376"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-376-CORE_META_MODEL--serialize-the-project-atom-prefix.md
  source_atom_id: CA-D-376
  source_atom_revision: 15
  source_sha256: 061b76d5e76f109369c39bcba7003e559d3c8806ecfda87f5aae5820a6876118
  original_relations_sha256: 60d285f0b5eadc5cfe0417918004395017eb1104d02fc3179cd56cf1f1493577
---
# Summary

Serialize the Project Atom prefix

## Scope

the Operator-selected Atom prefix in the Project Settings TOML Carrier.

## Claim

the Project Settings TOML Carrier **must** encode the Operator-selected Atom prefix as its exact nonempty uppercase TOML string value under CA-D-378 **in** `artifacts.identity.project_prefix` **before** the first Project Atom is created.

## Details

validation **must** preserve the selected prefix exactly; it **must not** trim **or** automatically uppercase it. the complete supported field signature is governed by CA-D-366.
