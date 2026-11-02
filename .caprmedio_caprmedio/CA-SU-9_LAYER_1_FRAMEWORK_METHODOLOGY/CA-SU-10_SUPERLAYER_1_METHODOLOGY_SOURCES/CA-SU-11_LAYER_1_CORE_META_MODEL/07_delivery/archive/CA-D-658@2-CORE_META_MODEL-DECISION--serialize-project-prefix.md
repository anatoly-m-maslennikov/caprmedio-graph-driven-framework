---
atom_id: CA-D-658@2
content_role: Delivery
type: Decision
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 7
version: 2
updated_at: 2026-10-30 14:22:38 +0400
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings.Prefix
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Governing Objects/Atom
relations:
  child_of:
  - CA-D-366
---
## Summary

Serialize Project Prefix

## Claim scope

the Operator-selected Project Prefix in the Project Settings TOML Carrier.

## Claim

the Project Settings TOML Carrier **must** encode the Operator-selected Project Prefix as its exact nonempty uppercase TOML string value under CA-D-378 **in** `artifacts.identity.project_prefix` **before** the first Project Atom is created.

## Details

validation **must** preserve the selected prefix exactly; it **must not** trim **or** automatically uppercase it. The complete supported field signature is governed by the pending [Project Settings Content Decision](CA-D-366@28-draft-CORE_META_MODEL-ENG_DECISION--serialize-project-settings-content-in-toml.md). This Decision preserves the existing storage contract and first-Atom timing; uses of the Prefix are outside this logical-property correction.

### Current source provenance

Replacement candidate for the historical Current source: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/CA-D-376-CORE_META_MODEL-ENG_DECISION--serialize-the-project-atom-prefix.md`, CA-D-376@25, SHA-256 `3b04a0bd6dfce9eec731a550edcdd86c6fdba8560255477bd4810f3c254bd614`. This role-only Draft allocates no canonical Delivery identity and does not rename CA-D-376.
