---
atom_id: CA-D-658
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 7
version: 4
updated_at: 2026-11-02 19:46:47 +0400
subjects:
  active: CAPRMEDIO <+ MODEL <+ Project.Settings.Prefix
  passive:
  - CAPRMEDIO <+ MODEL <+ Project.Settings
  - CAPRMEDIO <+ MODEL <+ Project
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO <+ MODEL <+ Atom
relations:
  child_of:
  - CA-D-366
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-658-CORE_META_MODEL-DECISION--serialize-project-prefix.md
  source_atom_id: CA-D-658
  source_atom_revision: 4
  source_sha256: befb09a2714d25403bf8043c3e8ee34b2b1d749c348581fcd031030c763b9805
  original_relations_sha256: 2a948e2a8ca98f226a4515239fa376af18890f07ccdd2ef7a0521257d70b6a6a
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

Replacement candidate for the historical Current source: `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-376-CORE_META_MODEL-ENG_DECISION--serialize-the-project-atom-prefix.md`, CA-D-376@25, SHA-256 `3b04a0bd6dfce9eec731a550edcdd86c6fdba8560255477bd4810f3c254bd614`. This role-only Draft allocates no canonical Delivery identity and does not rename CA-D-376.
