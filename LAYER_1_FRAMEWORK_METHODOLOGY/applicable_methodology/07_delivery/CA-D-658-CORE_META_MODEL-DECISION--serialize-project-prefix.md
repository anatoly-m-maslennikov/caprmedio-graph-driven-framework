---
atom_id: CA-D-658
ref_id: CA-D-658
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Prefix
  dependencies:
  - CAPRMEDIO_MODEL <+ Project.Settings
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Atom
tier: 7
relations:
  child_of:
  - CA-D-366
status: Active
version: 4
updated_at: 2026-11-02 19:46:47 +0400
carrier_destination:
  file:
    name: CA-D-658-CORE_META_MODEL-DECISION--serialize-project-prefix.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-658-CORE_META_MODEL-DECISION--serialize-project-prefix.md
  source_atom_id: CA-D-658
  source_atom_revision: 4
  source_sha256: b6a0009cb41088eeb69a9982730931b313d2e6f4cbb4016d00fde3ac3e530cbc
  original_relations_sha256: 2a948e2a8ca98f226a4515239fa376af18890f07ccdd2ef7a0521257d70b6a6a
---
## Summary

Serialize Project Prefix

## Claim

### Prose Claim


the Operator-selected Project Prefix in the Project Settings TOML Carrier.


the Project Settings TOML Carrier **must** encode the Operator-selected Project Prefix as its exact nonempty uppercase TOML string value under CA-D-378 **in** `artifacts.identity.project_prefix` **before** the first Project Atom is created.

## Details

validation **must** preserve the selected prefix exactly; it **must not** trim **or** automatically uppercase it. The complete supported field signature is governed by the pending [Project Settings Content Decision](CA-D-366@28-draft-CORE_META_MODEL-ENG_DECISION--serialize-project-settings-content-in-toml.md). This Decision preserves the existing storage contract and first-Atom timing; uses of the Prefix are outside this logical-property correction.

### Current source provenance

Replacement candidate for the historical Current source: `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-376-CORE_META_MODEL-ENG_DECISION--serialize-the-project-atom-prefix.md`, CA-D-376@25, SHA-256 `3b04a0bd6dfce9eec731a550edcdd86c6fdba8560255477bd4810f3c254bd614`. This role-only Draft allocates no canonical Delivery identity and does not rename CA-D-376.
