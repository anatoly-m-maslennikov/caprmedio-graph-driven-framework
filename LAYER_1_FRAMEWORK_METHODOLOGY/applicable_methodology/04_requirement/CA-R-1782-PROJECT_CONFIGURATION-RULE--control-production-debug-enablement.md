---
atom_id: CA-R-1782
ref_id: CA-R-1782
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Observability <+ Logging
  dependencies:
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Observability <+ Logging
tier: 3
status: Active
version: 15
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1782-PROJECT_CONFIGURATION-RULE--control-production-debug-enablement.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1782-PROJECT_CONFIGURATION-RULE--control-production-debug-enablement.md
  source_atom_id: CA-R-1782
  source_atom_revision: 15
  source_sha256: af253332514496668d08e6cc87bb552c7ed410bc2bd8e5307fc1bdc42f2d7a22
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Control production DEBUG enablement

## Claim

### Prose Claim


logging Implementation for production DEBUG logging under Logging Policies.


logging Implementation **must** keep production DEBUG logging disabled by default. temporary enablement **must** be scoped by component, subject, run, entity, **or** another bounded selector, have an automatic expiry, **and** preserve the same redaction rules as **every** other level.

## Details

the selector **and** expiry bound temporary production DEBUG use while preserving its required redaction treatment.
