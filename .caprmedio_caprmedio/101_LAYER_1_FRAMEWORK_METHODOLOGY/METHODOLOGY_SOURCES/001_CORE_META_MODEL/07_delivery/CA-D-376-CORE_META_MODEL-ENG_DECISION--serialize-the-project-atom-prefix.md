---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings.Atom Prefix
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
version: 23
updated_at: 2026-10-27 19:59:24 +0400
relations:
  child_of:
  - CA-D-366
atom_id: CA-D-376
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 7
type: Eng Decision
---
# Summary

Serialize the Project Atom prefix

## Scope

the Operator-selected Atom prefix in the Project Settings TOML Carrier.

## Claim

the Project Settings TOML Carrier **must** encode the Operator-selected Atom prefix as its exact nonempty uppercase TOML string value under CA-D-378 **in** `artifacts.identity.project_prefix` **before** the first Project Atom is created.

## Details

validation **must** preserve the selected prefix exactly; it **must not** trim **or** automatically uppercase it. the complete supported field signature is governed by CA-D-366.
