---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings.Atom Prefix
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Actor/Operator
version: 25
updated_at: 2026-10-29 07:45:30 +0400
relations:
  child_of:
  - CA-D-366
atom_id: CA-D-376@25
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 7
type: Decision
---
## Summary

Serialize the Project Atom prefix

## Claim scope

the Operator-selected Atom prefix in the Project Settings TOML Carrier.

## Claim

the Project Settings TOML Carrier **must** encode the Operator-selected Atom prefix as its exact nonempty uppercase TOML string value under CA-D-378 **in** `artifacts.identity.project_prefix` **before** the first Project Atom is created.

## Details

validation **must** preserve the selected prefix exactly; it **must not** trim **or** automatically uppercase it. the complete supported field signature is governed by CA-D-366.
