---
atom_id: CA-D-388
ref_id: CA-D-388
container:
  scope_unit: CA-SU-13
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier
  dependencies:
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Data Handling <+ Serialization
  - CAPRMEDIO_MODEL <+ Projection
tier: 3
status: Active
version: 24
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-D-388-PROJECT_CONFIGURATION-DECISION--serialize-generated-data-stage-prefixes-and-formats.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery/CA-D-388-PROJECT_CONFIGURATION-ENG_DECISION--serialize-generated-data-stage-prefixes-and-formats.md
  source_atom_id: CA-D-388
  source_atom_revision: 24
  source_sha256: cc3395de38b217b8b60687033a9489b985fcc691461fcc2d3d6fcc323a87ed7d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Generated Data Stage Prefixes and Formats

## Claim

### Prose Claim


Journal input and generated Projection Carriers.


Journal input **and** generated Projection Carriers **must** use these ordered stage prefixes: canonical Journal input `src`, deterministic lossless staging Projection `stg`, consumer-ready semantic Projection `mrt`, **and** aggregated metrics Projection `biz`. `src` **must** use canonical NDJSON Journal input; `stg` **must** use TOON. these prefixes classify Journal inputs **and** generated Projections **only**. unregistered stage prefixes remain available for later governed Extension.
