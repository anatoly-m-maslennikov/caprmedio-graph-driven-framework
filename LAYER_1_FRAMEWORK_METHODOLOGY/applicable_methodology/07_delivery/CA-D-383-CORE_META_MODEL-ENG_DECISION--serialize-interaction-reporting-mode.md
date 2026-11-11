---
atom_id: CA-D-383
ref_id: CA-D-383
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Interaction.Reporting Mode
tier: 6
relations:
  child_of:
  - CA-D-361
  depends_on:
  - CA-R-1628
status: Active
version: 31
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-383-CORE_META_MODEL-DECISION--serialize-interaction-reporting-mode.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-383-CORE_META_MODEL-ENG_DECISION--serialize-interaction-reporting-mode.md
  source_atom_id: CA-D-383
  source_atom_revision: 31
  source_sha256: 4cffa18d76c79d3a1760882fd79bfaeed747cfa9ceee7ca267dffdfd0a0a81ca
  original_relations_sha256: 53d74772fdb461981b4e76418975fdc02f46377b9dd610d7cd45dbfb728e82d4
---
## Summary

Serialize Interaction Reporting Mode

## Claim

### Prose Claim


an explicit instance reporting default **in** the Framework Instance Settings TOML Carrier.


an explicit instance reporting default **in** the Framework Instance Settings TOML Carrier **must** use `reporting_mode` **in** the `[interaction]` section, using an allowed value governed by CA-R-1628-CORE_META_MODEL-RULE--allow-silent-and-verbose-reporting-modes.
