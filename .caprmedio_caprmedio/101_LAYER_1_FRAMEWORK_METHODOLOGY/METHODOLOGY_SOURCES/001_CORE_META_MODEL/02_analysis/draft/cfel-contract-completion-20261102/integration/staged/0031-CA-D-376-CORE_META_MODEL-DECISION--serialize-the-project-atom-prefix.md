---
subjects:
  active: Project.Settings.Prefix
  passive:
  - Project.Settings
  - Atom
  - Entity/Object/Continuant/Actor/Operator
version: 28
updated_at: 2026-11-02 07:52:54 +0400
relations:
  child_of:
  - CA-D-366
atom_id: CA-D-376
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 7
role: Delivery
form: Decision
---
## Summary

Serialize the Project Atom prefix

## Claim scope

the Operator-selected Atom prefix in the Project Settings TOML Carrier.

## Claim

the Project Settings TOML Carrier **must** encode the Operator-selected Atom prefix as its exact nonempty uppercase TOML string value under CA-D-378 **in** `artifacts.identity.project_prefix` **before** the first Project Atom is created.

## Details

validation **must** preserve the selected prefix exactly; it **must not** trim **or** automatically uppercase it. the complete supported field signature is governed by CA-D-366.
