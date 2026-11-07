---
atom_id: CA-R-1781
ref_id: CA-R-1781
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
version: 14
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1781-PROJECT_CONFIGURATION-RULE--bound-high-frequency-info-logging.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1781-PROJECT_CONFIGURATION-RULE--bound-high-frequency-info-logging.md
  source_atom_id: CA-R-1781
  source_atom_revision: 14
  source_sha256: 97ae123a7099095ba3007b8fa7ac298c1f5bd2a1ae39e15c75e7f16875d54278
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Bound high-frequency INFO logging

## Claim

### Prose Claim


logging Implementation for high-frequency success, polling, **and** progress events under production Logging Policies.


logging Implementation **must** bound high-frequency success, polling, **and** progress events through aggregation, sampling, **or** emission as `DEBUG` **where** appropriate rather than creating unbounded `INFO` noise.

## Details

the alternatives bound repeated normal-event volume; the severity taxonomy separately classifies material operational milestones.
