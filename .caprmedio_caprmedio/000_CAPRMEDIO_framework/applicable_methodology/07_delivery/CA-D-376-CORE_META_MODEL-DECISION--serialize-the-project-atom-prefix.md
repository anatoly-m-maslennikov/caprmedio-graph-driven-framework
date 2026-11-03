---
subjects:
  active: Project.Settings.Prefix
  passive:
  - Project.Settings
  - Atom
  - Entity/Object/Continuant/Actor/Operator
version: 28
updated_at: 2026-11-02 08:06:47 +0400
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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-376-CORE_META_MODEL-DECISION--serialize-the-project-atom-prefix.md
  source_atom_id: CA-D-376
  source_atom_revision: 28
  source_sha256: bbeee86536136ec0be17dbc739b98488193a26fe86a2910ea9e307c10a359bd5
  original_relations_sha256: 2a948e2a8ca98f226a4515239fa376af18890f07ccdd2ef7a0521257d70b6a6a
---
## Summary

Serialize the Project Atom prefix

## Claim scope

the Operator-selected Atom prefix in the Project Settings TOML Carrier.

## Claim

the Project Settings TOML Carrier **must** encode the Operator-selected Atom prefix as its exact nonempty uppercase TOML string value under CA-D-378 **in** `artifacts.identity.project_prefix` **before** the first Project Atom is created.

## Details

validation **must** preserve the selected prefix exactly; it **must not** trim **or** automatically uppercase it. the complete supported field signature is governed by CA-D-366.
