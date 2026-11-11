---
atom_id: CA-R-1783
ref_id: CA-R-1783
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Observability <+ Logging"
tier: 3
status: Active
version: 14
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1783-PROJECT_CONFIGURATION-RULE--require-production-logging-lifecycle-settings.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1783-PROJECT_CONFIGURATION-RULE--require-production-logging-lifecycle-settings.md
  source_atom_id: CA-R-1783
  source_atom_revision: 14
  source_sha256: 921f1668a7545e9ce56cf3758efbc745cf1258e645cdda296440e96fb9d45c0b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Require production logging lifecycle settings

## Claim

### Prose Claim


production Logging Policies **and** their retention, access, sampling, rotation, maximum size, back-pressure, unavailable-sink, **and** disk-pressure conditions.


a production Logging Policy **must** define retention, access, sampling, rotation, maximum size, back-pressure, unavailable-sink behavior, **and** disk-pressure behavior.

## Details

these settings define the policy’s retention **and** delivery controls.
