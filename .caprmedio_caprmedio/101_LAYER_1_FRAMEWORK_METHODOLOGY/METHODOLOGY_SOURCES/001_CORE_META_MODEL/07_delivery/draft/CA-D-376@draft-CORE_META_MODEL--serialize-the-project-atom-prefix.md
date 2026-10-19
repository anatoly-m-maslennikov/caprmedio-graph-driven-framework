---
subjects:
  governs: "Entity/Node/Continuant/Project.Settings.Atom Prefix"
  depends_on:
    ["Entity/Node/Continuant/Project.Settings", "Entity/Node/Continuant/Atom", "Entity/Node/Continuant/Actor/Type: Operator"]
version: 15
updated_at: "2026-10-19 11:46:22 +0000"
relations:
  child_of:
    - "CA-D-366"
atom_id: "CA-D-376@draft"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize the Project Atom prefix

## Scope

the Operator-selected Atom prefix in the Project Settings TOML Carrier.

## Claim

the Project Settings TOML Carrier **must** encode the Operator-selected Atom prefix as its exact nonempty uppercase TOML string value under CA-D-378 **in** `artifacts.identity.project_prefix` **before** the first Project Atom is created.

## Details

validation **must** preserve the selected prefix exactly; it **must not** trim **or** automatically uppercase it. the complete supported field signature is governed by CA-D-366.
