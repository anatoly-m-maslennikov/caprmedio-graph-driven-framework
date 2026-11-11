---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Governing Configuration
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Governing Configuration
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - CAPRMEDIO <+ MODEL <+ Carrier
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-D-407
atom_id: CA-D-408
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-408-CORE_META_MODEL-ENG_DECISION--reuse-framework-parameter-fields-in-default-settings.md
  source_atom_id: CA-D-408
  source_atom_revision: 24
  source_sha256: fa7a9fea513f7b749a5654662adbf7c120f9e5ecec8fbbd083ee15ecc964b3f7
  original_relations_sha256: 44e957705cab6ac31a8a6a7150c7b1eae1027df256679e7abcbc511b4699562c
---
## Summary

Reuse framework parameter fields in Default Settings

## Claim scope

parameter values in the Default Settings TOML Carrier.

## Claim

**every** parameter value **in** the Default Settings TOML Carrier **must** use the same registered section, field path, value type, **and** allowed domain as the corresponding explicit Framework Instance Settings parameter, **without** introducing a separate defaults-field schema.
